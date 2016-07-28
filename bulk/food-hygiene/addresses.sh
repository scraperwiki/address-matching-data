#!/bin/sh

echo "test	name	text	postcode	food-authority	point"
find ./cache -name FHRS*.xml |
  xargs xsltproc addresses.xsl |
  sed -e 's/, [, ]*/, /g' -e 's/, *	/	/' -e 's/\\//g'
