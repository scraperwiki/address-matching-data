#!/usr/bin/env python3

import sys
from datetime import datetime
import re
import csv


def iso_date(s):
    if not s:
        return ''
    day, month, year = s.rsplit('/', 3)
    return datetime(
        int(year), int(month), int(day)
        ).isoformat().strip('T00:00:00')


address_fields = [
    "RegAddress.CareOf",
    "RegAddress.POBox",
    "RegAddress.AddressLine1",
    "RegAddress.AddressLine2",
    "RegAddress.PostTown",
    "RegAddress.County",
    "RegAddress.Country"
]

fields = ["test", "name", "text", "postcode", "start-date", "end-date"]
sep = "\t"

countries = [
    '',
    'ENGLAND',
    'ENGLAND - UK',
    'ENGLAND AND WALES',
    'ENGLAND UK',
    'GREAT BRITAIN',
    'GREAT BRITAIN (UK)',
    'GREAT BRITAIN UK',
    'GREAT BRITAIN, UK',
    'NORTHERN IRELAND',
    'SCOLAND UK',
    'SCOTALND UK',
    'SCOTLAD UK',
    'SCOTLAND',
    'SCOTLAND  UK',
    'SCOTLAND (U.K.)',
    'SCOTLAND GREAT BRITAIN',
    'SCOTLAND UK',
    'SCOTLAND UNITED KINGDO',
    'SCOTLAND UNITED KINGDOM',
    'SCOTLAND UNITED KINGODM',
    'SCOTLAND, UK',
    'SCOTLAND, UNITED KINGDOM',
    'U.K.',
    'UNITED KINGDOM',
    'UNITED KINGDON',
    'UNITED KINGODM',
    'UNITED KINGSOM'
]

print(sep.join(fields))

reader = csv.DictReader(sys.stdin)
reader.fieldnames = [field.strip() for field in reader.fieldnames]

for row in reader:

    if row['RegAddress.Country'] in countries:
        item = {}
        item['test'] = row['CompanyNumber']
        item['name'] = row['CompanyName']

        item['text'] = ",".join([row[field] for field in address_fields])
        item['text'] = item['text'].strip(", ")
        item['text'] = re.sub(",+", ", ", item['text'])

        item['postcode'] = row['RegAddress.PostCode']

        item['start-date'] = iso_date(row['IncorporationDate'])
        item['end-date'] = iso_date(row['DissolutionDate'])

        print(sep.join([item[field] for field in fields]))
