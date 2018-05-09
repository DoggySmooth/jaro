#!/usr/bin/env python3

import sys, os, json, collections

json = sys.argv[1]
xml  = sys.argv[2]

os.system("lib/xml2json.py -t xml2json -o "+json+" "+xml+" --strip_text")
os.system("lib/jsonlint "+json)
os.system("python -m json.tool "+json+" > tmp.json")

print("Generatedd JSON Sucessfully!")
