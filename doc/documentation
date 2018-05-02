			---	JARO DOCUMENTATION	---


Title:		JARO
Author:		Smooth
Year:		2018


JARO defines an standart format for reverse engineer reports of applications. The advantage of JARO is a clear defined data structure allowing users to generate graphs for easy analisis as allowing them to create tools to manipulate the data. Using XML as main format makes it known to the most of people out there and its extensible structure makes changes fast.

There are unlimited manners to write a report of an analisis based on what the reverse
engineer thinks its relevant. The reports layout needs to be understood first and if 
we want to do M2M manipulations we need to adapt/write tools to work with that 
particular report. It's useless to tell that this is inefficient. That's where JARO
comes into the screen. By defining rules and formats as also providing tools to easily
query and manipulate reports, JARO speeds up the whole reverse engineering process and 
in the same time makes it easier for someone else to understand the analisis. As the
format and layout is defined, JARO provides extensibility to the reports and also to the tools that manipulate the data. JARO users could collaborate on some reverse engineering of an application and easily merge their output.

This is the main idea behind JARO.

JARO could so implement a whole bunch of features manipulating the data.

Features:

	1.Graph generation
	
	Easy graph generation showing how the package is structured and which nodes are
	malicious.

	2.JSON generation
	
	Maschine to Maschine data transfer and manipulation using well known JSON format	
	3.HTML 

	Displaying analisis in an easy to read format displaying the malicious behaviour of classes, packages or methods with an description.


Architecture:

The main file JARO is using XML format, from which is generated all the files
described in "Features". As XML is a verbose and annoying language, we use a python library to generate the XML: PLIM.

PLIM -> XML <-> JSON -> HTML


Technical data
______________


1.Graph Generation

The structured JSON file allows to do data manipulation in an well known manner.
GraphViz's library for python helps to structure the data and generate the graph.
JSON's library is used to import the json generated file from the XML.


2.JSON Generation

For the generation of the JSON file a tool is being used. Called xml2json, it lets easily generate the data. JSONLINT is used to format the data and finally JSONLINT to validate the data structure of the JSON file.

3.HTML generation

A self written python script generates the files inculding an intuitive layout. 
The html generation is based on the generated json file.

4.XML generation

PLIM tool is included in the package and with the help of plim compiler "plimc" it generates an XML file from its plimfile. The generated XML goes trough a formating phase with the help of xmllint and then a written XSD file validates the structure of the generated xml.



HOW TO
______


Files creation

All the tools are included in this package token from github.
A file with an name with the SHA256 of the analised file and a plim extension can be pasted in the root of this project. Executing "make" automatically takes the .plim extension and generate all the data. The output directory paste the result of the above explained features.


Graph Generation

In the directory "pythonGrap" there is the python script called pythonGraph.py
Run ./pythonGraph.py jsonfile         to generate the graph of the .json file.
