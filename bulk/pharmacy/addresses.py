#!/usr/bin/env python3

import sys
import csv
import re

# OrganisationID	OrganisationCode	OrganisationType	SubType	OrganisationStatus	IsPimsManaged	IsEPSEnabled	OrganisationName	Address1	Address2	Address3	City	County	Postcode	Latitude	Longitude	ParentODSCode	ParentName	Phone	Email	Website	Fax

address_fields = ["Address1", "Address2", "Address3", "City", "County"]
fields = [ "test", "name", "text", "postcode", "point" ]
sep = "\t"

if __name__ == '__main__':

    print(sep.join(fields))

    # read map
    for row in csv.DictReader(sys.stdin, delimiter=sep):
        item = {}
        item['test'] = "pharmacy:" + row['OrganisationID']
        item['name'] = row['OrganisationName']

        item['text'] = ",".join([row[field] for field in address_fields])
        item['text'] = re.sub(",+", ", ", item['text'])
        item['text'] = item['text'].strip(", ")

        item['postcode'] = row['Postcode']
        item['point'] = "[%.5f,%.5f]" % (float(row['Longitude']), float(row['Latitude']))

        print(sep.join([item[field] for field in fields]))
