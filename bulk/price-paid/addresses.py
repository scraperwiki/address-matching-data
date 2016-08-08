#!/usr/bin/env python3

import sys
import csv
import re

address_cols = range(7, 13)
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

# "{816D2B17-C653-4CCC-8B8A-3EDD66EB464F}","69000","1995-04-03 00:00","PO14 2QN","S","N","F","34","","HAROLD ROAD","FAREHAM","FAREHAM","FAREHAM","HAMPSHIRE","A","A"

if __name__ == '__main__':

    print(sep.join(fields))

    duplicates = 0
    seen = set()

    # read map
    for row in csv.reader(sys.stdin):
        hash_int = make_hash_int(row["text"])
        if hash_int in seen:
            duplicates += 1
            # raise RuntimeError("collision: {}, {}", hash_int, row["text"])
            continue
        seen.add(hash_int)

        item = {}
        item['test'] = "PP:{:9d}".format(hash_int)
        item['text'] = ",".join([row[col] for col in address_cols if row[col-1] != row[col]])
        item['text'] = re.sub(",+", ", ", item['text'])

        item['postcode'] = row[3]

        print(sep.join([item[field] for field in fields]))
