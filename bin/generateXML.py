#!/usr/bin/env python3

import sys, os
from lxml import etree

os.system("lib/plimc "+sys.argv[1]+" -o "+sys.argv[2])

file = open("tmp.xml","w")

print('XML Generated Sucessfully!')


xmlschema_doc = etree.parse("res/schema/s2extend")
xmlschema = etree.XMLSchema(xmlschema_doc)

xml_doc = etree.parse(sys.argv[2])
result = xmlschema.validate(xml_doc)

xml_doc.write("tmp.xml", encoding="utf-8", pretty_print=True)
file.close()

if result:
	print("XML file is valid!")
else:
	print("XML Schema is invalid!")
