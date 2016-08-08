#
#  extract addresses from Companies House open data
#
#  http://download.companieshouse.gov.uk/en_output.html
#
DATE:=$(shell date +"%Y-%m-01")
URL_PREFIX=http://download.companieshouse.gov.uk/BasicCompanyData-$(DATE)-part
URL_SUFFIX=_5.zip

ZIPS=\
	cache/part1.zip\
	cache/part2.zip\
	cache/part3.zip\
	cache/part4.zip\
	cache/part5.zip

all:	addresses.tsv

addresses.tsv:	addresses.py $(ZIPS)
	for f in $(ZIPS) ; do funzip $$f | ./addresses.py ; done > $@


#
#  download data
#
cache/part1.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)1$(URL_SUFFIX)" > $@
cache/part2.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)2$(URL_SUFFIX)" > $@
cache/part3.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)3$(URL_SUFFIX)" > $@
cache/part4.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)4$(URL_SUFFIX)" > $@
cache/part5.zip:;	mkdir -p cache && curl -s "$(URL_PREFIX)5$(URL_SUFFIX)" > $@

prune::
	rm -rf cache
