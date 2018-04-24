SHELL = /bin/sh

targetPLIM=$(shell find . -name '*.plim' -exec basename \{} \;)
targetXML=$(patsubst %.plim,%.xml, $(targetPLIM))
targetJSON=$(patsubst %.plim,%.json, $(targetPLIM))
dirName=$(patsubst %.plim,%, $(targetPLIM))

all: xml json output 

xml : $(targetPLIM) 
	./bin/plimc $(targetPLIM) -o $(targetXML)
	./bin/xmllint --format $(targetXML) -o $(targetXML)
	./bin/xmllint -schema ./lib/schema/s2extend $(targetXML) -noout

json : $(targetXML)
	./bin/xml2json.py -t xml2json -o $(targetJSON) $(targetXML) --strip_text
	python -c "import json, sys, collections; print json.dumps(json.load(open('$(targetJSON)'), object_pairs_hook=collections.OrderedDict), indent=4)" > tmp.json 	
	rm $(targetJSON)
	mv tmp.json $(targetJSON)
	./bin/jsonlint $(targetJSON)

output: $(targetXML) $(targetJSON)

	mv $(targetXML) output
	mv $(targetJSON) output	

