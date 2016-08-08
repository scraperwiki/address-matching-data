# probably not a very cool URL, linked to from https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads
PP_COMPLETE_URL='http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv'

addresses.tsv:	cache/pp-complete.csv addresses.py
	./addresses.py < cache/pp-complete.csv > $@

# download price paid dataset
# - contains invalid UTF-8 characters ..
cache/pp-complete.csv:
	mkdir -p cache
	curl -s -L $(PP_COMPLETE_URL) | iconv -f ISO-8859-1 -t UTF-8 > $@

clean:
	rm -rf cache
