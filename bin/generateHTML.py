#!/usr/bin/env python3

import sys, os
from html5print import HTMLBeautifier

json = sys.argv[1]
html = sys.argv[2]

file = open("tmp.html","w")

os.system("python3 ./bin/htmlPython.py "+json+" > "+html)
file.write(HTMLBeautifier.beautify(open(html), 4))
