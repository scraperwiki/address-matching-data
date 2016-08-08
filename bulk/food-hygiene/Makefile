INDEX_URL="http://ratings.food.gov.uk/open-data/"

addresses.tsv:	addresses.sh addresses.xsl
	./addresses.sh > $@

download:
	mkdir -p cache
	./download.sh $(INDEX_URL) cache/

clean:
	rm -rf cache

clobber:
	rm addresses.tsv
