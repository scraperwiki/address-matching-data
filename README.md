# Address matching data

Test cases and other data for training and testing address matching algorithms.

# Test case format

Test cases are held in tab-separated format files with the following columns:

- test — an identifier for the test case which should be unique across all tests
- name — the addressee or name of the business (if separable)
- text — address text to be matched, newlines should be encoded as '\n' (only include name or postcode if can't be stored in separate field)
- postcode — an optional, separate postcode (if separable)
- uprns — one or more UPRN values in decimal which could match the address, separated by semicolon ';'
- notes — an explanation of the test

A test case may contain additional fields for information.

# Bulk datasets

The [bulk](bulk) directory contains addresses found in bulk in open data, to be matched.

- [charity-commission](bulk/charity-commission) — 345k addresses from [Charity Commission](http://data.charitycommission.gov.uk/)
- [companies-house](bulk/companies-house) — 3.8 million addresses from [Companies House](http://download.companieshouse.gov.uk/en_output.html)
- [democracy-club-polling-stations](bulk/democracy-club-polling-stations) – 5k polling stations from [Democracy Club](https://wheredoivote.co.uk/)
- [edubase](bulk/edubase) — 44k schools from [Department of Education](http://www.education.gov.uk/edubase/home.xhtml)
- [food-hygiene](bulk/food-hygiene) — 360k food establishments from [Food Standards Agency](http://ratings.food.gov.uk/open-data/)
- [general-medical-practices](bulk/general-medical-practices) 13k practices from [HSCIC](https://data.gov.uk/dataset/general-medical-practices)
- [pharmacy](bulk/pharmacy) — 11k pharmacies from [NHS Choices](https://data.gov.uk/dataset/pharmacies)
- [price-paid](bulk/price-paid) — 21 million residential properties from [Land Registry](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads)
- [voa](bulk/voa) – scripts to process the 1.9 million [VOA business-rates valuations](http://www.2010.voa.gov.uk/rli/) (not openly available)

Few bulk datasets currently contain resolved UPRNs, but can form the basis of test cases as we build registers.

# Licence

The software in this project is open source, covered by [LICENSE](LICENSE) file.

The data held in this repository is [© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.

Data downloaded by the build process may be covered by different copyright and terms.
