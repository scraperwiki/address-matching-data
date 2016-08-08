#!/usr/bin/env python3

import csv
import hashlib
import struct
import sys

export_fields = ["test", "text", "postcode"]
sep = "\t"

def make_hash_int(text):
    text = text.encode("utf-8")
    text = text.lower()
    h = hashlib.sha256()
    h.update(text)
    number = 0
    while number < 1e9: # ensure 9 digits without leading zeroes.
        number, = struct.unpack("I", h.digest()[:4])
        h.update(b"0123456789") # add more rubbish to the hash state.
    return number

if __name__ == '__main__':

    print(sep.join(export_fields))

    seen = set()

    import re
    postcode_re = re.compile(r"^(.*),?(\s[A-Z]+[A-Z0-9]+\s+[0-9]+[A-Z]+),?$")

    duplicates = 0

    # read map
    for row in csv.DictReader(sys.stdin, delimiter=sep):
        hash_int = make_hash_int(row["text"])
        if hash_int in seen:
            duplicates += 1
            # raise RuntimeError("collision: {}, {}", hash_int, row["text"])
            continue
        seen.add(hash_int)

        row['test'] = "DCPS:{:9d}".format(hash_int)

        fields = row['text'].strip().split("\n")
        row['text'] = ", ".join(field for field in fields if field)
        row['postcode'] = ""

        match = postcode_re.match(row['text'])
        if match:
            text, postcode = match.groups()
            row['text'] = text.strip(", ")
            row['postcode'] = postcode

            # Check for a duplicate postcode
            if row['text'].endswith(postcode):
                row['text'] = row['text'][:-len(postcode)].strip(", ")

        assert not any("\t" in field for field in fields)

        print(sep.join(row[field] for field in export_fields))

    print("Skipped {} duplicate rows".format(duplicates), file=sys.stderr)
