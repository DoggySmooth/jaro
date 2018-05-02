SHELL = /bin/sh

targetPLIM=$(shell find . -name '*.plim' -exec basename \{} \;)
targetXML=$(patsubst %.plim, %.xml, $(targetPLIM))
targetJSON=$(patsubst %.plim,%.json, $(targetPLIM))

all: xml json 

xml : $(targetPLIM) 
	plimc $(targetPLIM) -o $(targetXML)
	xmllint --format $(targetXML) -o $(targetXML)
	xmllint -schema s2extend $(targetXML) -noout

json : $(targetXML)
	xml2json.py -t xml2json -o $(targetJSON) $(targetXML) --strip_text
	python -c "import json, sys, collections; print json.dumps(json.load(open('$(targetJSON)'), object_pairs_hook=collections.OrderedDict), indent=4)" > tmp.json 	
	rm $(targetJSON)
	mv tmp.json $(targetJSON)
	jsonlint-php $(targetJSON)
