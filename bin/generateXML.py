#!/usr/bin/env python3

import sys, os

os.system("lib/plimc "+sys.argv[1]+" -o "+sys.argv[2])
os.system("lib/xmllint -schema res/schema/s2extend "+sys.argv[2]+" -noout")
os.system("lib/xmllint --format "+sys.argv[2]+" -o "+sys.argv[2])

print('XML Generated Sucessfully!')
