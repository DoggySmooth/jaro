SHELL = /bin/sh

targetPLIM=$(shell find . -name '*.plim')
targetName=$(shell find . -name '*.plim' -exec basename \{} \;)
targetXML=$(patsubst %.plim,%.xml, $(targetPLIM))
targetJSON=$(patsubst %.plim,%.json, $(targetPLIM))
targetHTML=$(patsubst %.plim,%.html, $(targetName))
targetJSOName=$(patsubst %.plim,%.json, $(targetName))

dirName=$(patsubst %.plim,%, $(targetName))

all: xml json graph html output

xml : $(targetPLIM) 
	./bin/generateXML.py $(targetPLIM) $(targetXML)

json : $(targetXML)
	./bin/generateJSON.py $(targetJSON) $(targetXML)

	rm $(targetJSON)
	mv tmp.json $(targetJSON)


output: $(targetXML) $(targetJSON) 

	if ! [ -d "./output/$(dirName)" ]; then mkdir ./output/$(dirName) ; fi
	mv $(targetXML) output/$(dirName)
	mv $(targetJSON) output/$(dirName)	
	mv $(targetHTML) output/$(dirName)
	mv Graph.gv.svg output/$(dirName)

html: $(targetJSON)

	./bin/generateHTML.py $(targetJSON) $(targetHTML)
	rm $(targetHTML)
	mv tmp.html $(targetHTML)

graph: $(targetJSON)

	python3 ./bin/graph.py $(targetJSON) 
	rm Graph.gv
