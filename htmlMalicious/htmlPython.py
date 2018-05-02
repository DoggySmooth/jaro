import json

j = json.load(open('adwo.json'))

print('<html lang="en"><head><meta charset="utf-8"><title>Smoothin</title><meta name="description" content="Login"><meta name="Smooth" content="SitePoint"><link rel="stylesheet" href="style.css" type="text/css"><script>function toggle(attr) {var choice = document.getElementById(attr).style.display; if (choice == "block"){document.getElementById(attr).style.display = "none"; } else {document.getElementById(attr).style.display = "block"; }}</script></head><body><div class="horizontal-menu"><a class="search"> Teeeeeeeeeeeeeeeeeeeeest </a></div><div class="vertical-menu"><a class="logo">Jaro</a><a>Link 1</a><a>Link 2</a><a>Link 3</a><a> Link 4 </a></div><div class="content"><div class="box"><div class="box-header"><a> App </a></div><div class="box-content"><table><tr><td>Constructor</td></tr><tr><td>android.permission.ACCESS_COARSE_LOCATION</td></tr></table></div>')

def writePKG(var):

	print('<div class="box-header"><a> Package '+var+' </a><button onclick="toggle('+"'"+'packageContent'+var+"'"+')">ClickMe</button></div><div class="box" id="packageContent'+var+'">')

def writeClass(var):

	print('<div class="box-header"><a> Class '+var+'</a><button onclick="toggle('+"'"+'classContent'+var+"'"+')">ClickMe</button></div><div class="box-ar" id="classContent'+var+'">')

def classAddDesc(className,var):
	print('<div class="box-body" id="descContent'+className+'" ><table><tr><td>'+var+'</td></tr></table></div>')
	
def writeImports(className, imps):

	print('<div class="box-header"><a> Imports </a><button type="button" onclick="toggle('+"'"+'importsContent'+className+"'"+')">ClickMe</button></div>')

	print('<div class="box-body" id="importsContent'+className+'" ><table>')
	for imports in imps:
		print('<tr><td>'+imports+'</td></tr>')
	print('</table></div>')

def writeAttributes(className, attrs):

	print('<div class="box-header"><a> Attributes </a></div>')
	print('<div class="box-body"><table>')
	for attributes in attrs:
        	print("<tr><td>Name</td><td>"+attributes['name']+"</td><td>Type</td><td>"+attributes['type']+"</td></tr>")
	print('</table></div>')
	
def writeDicMethods(className, meths):

	print('<div class="box-header"><a> Methods </a></div>')
	print('<div class="box-header"><a>'+meths['name']+'</a></div>')
	print('<div class="box-body"><table>')
	print("<tr><td>Description</td><td>"+str(meths['description'])+"</td></tr></table></div></div>")

def writeMethods(className, meths):
	
	print('<div class="box-header"><a> Methods </a></div>')
	for methods in meths:
		print('<div class="box-header"><a>'+methods['name']+'</a></div>')
		print('<div class="box-body"><table>')
		if mal in methods:
			print('malicious')
		if 'parameters' in methods:
			if isinstance(methods['parameters'], dict):
				print("<tr><td>Parameter</td><td>"+str(methods['parameters']['parameter']['param'])+"</td>")
				print("<td>Output</td><td>"+str(methods['parameters']['parameter']['output'])+"</td></tr>")
				print("<tr><td>Description</td><td>"+str(methods['parameters']['parameter']['description'])+"</td></tr>")
				if 'return' in methods['parameters']['parameter']:
					print(methods['parameters']['parameter']['return'])	
					for key in methods['parameters']['parameter']['return']:
						print("<tr><td>Return</td><td>"+key +"</td><td>"+methods['parameters']['parameter']['return'][key]+"</td></tr>")
	
				if 'sha256' in methods:
					print("<tr><td>SHA256 </td><td>"+str(methods['sha256'])+"</td>")
		if 'calls' in methods:
			if isinstance(methods['calls']['call'], list):
				for x in range(len(methods['calls']['call'])):
					print("<tr><td> Calls </td><td>"+methods['calls']['call'][x]+"</td></tr>")
			else:
				print("<tr><td> Calls </td><td>"+methods['calls']['call']+"</td></tr>")
		if 'description' in methods:
					print("<tr><td>Description</td><td>"+str(methods['description'])+"</td></tr>")
		print('</table></div>')
	print('</div>')


path = j['app']['analisis']['packages']
mal = 'malicious'
classes = j['app']['analisis']['packages']['pkg']['classes']

def malicious():
	
	print('<div class="box-header"><a> Malicious artefacts </a></div>')
	for i in path:
		if mal in path[i]:
			print('<div class="box-body"><table><tr><td>Package</td><td>'+path[i]['name']+'</td><td>'+path[i]['malicious']+'</td></tr></table></div>')
		for className in path[i]['classes']['class']:
			if mal in className:
				print('<div class="box-body"><table><tr><td>Class</td><td>'+path[i]['name']+'.<a style="color: red;">'+className['name']+'</a></td><td>'+className['malicious']+'</td></tr></table></div>')
			if (className['attributes'] and not isinstance(className['attributes']['attribute'], dict)):
				for attr in className['attributes']['attribute']:
					if mal in attr:
						print('<div class="box-body"><table><tr><td>Attribute</td><td>'+path[i]['name']+'.'+className['name']+' <a style="color: red;">'+attr['name']+'</a></td><td>'+attr['malicious']+'</td></tr></table></div>')

			if (className['methods'] and not isinstance(className['methods']['method'], dict)):					
				for method in className['methods']['method']:
					if mal in method:	
						print('<div class="box-body"><table><tr><td>Method</td><td>'+path[i]['name']+'.'+className['name']+' <a style="color: red;">'+method['name']+'</a></td><td>'+method['malicious']+'</td></tr></table></div>')
malicious()

for i in path:
	writePKG(path[i]['name'])
	
	for className in path[i]['classes']['class']:
		writeClass(className['name'])
		if 'description' in className:
			classAddDesc(className['name'], className['description'])

		if (className['imports'] and not isinstance(className['imports']['import'], dict)):
			writeImports(className['name'], className['imports']['import'])

		if (className['attributes'] and not isinstance(className['attributes']['attribute'], dict)):
			writeAttributes(className['name'], className['attributes']['attribute'])
		if (className['methods'] and not isinstance(className['methods']['method'], dict)):
			writeMethods(className['name'], className['methods']['method'])

		elif (className['methods'] and isinstance(className['methods']['method'], dict)):
			writeDicMethods(className['name'], className['methods']['method'])	
			
print('</div></div></html>')



