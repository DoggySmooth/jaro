import json
import sys

j = json.load(open(sys.argv[1]))

print('<!DOCTYPE html><html lang="en"><head><title>Smoothin</title><meta name="description" content="Login"><meta name="Smooth" content="SitePoint"><link rel="stylesheet" href="../lib/styles/style.css" type="text/css"><script type="application/javascript">function toggle(attr) {var choice = document.getElementById(attr).style.display; if (choice == "block"){document.getElementById(attr).style.display = "none"; } else {document.getElementById(attr).style.display = "block"; }}</script></head><body><div class="horizontal-menu"><a class="search"> Teeeeeeeeeeeeeeeeeeeeest </a></div><div class="vertical-menu"><a class="logo">Jaro</a><a>Link 1</a><a>Link 2</a><a>Link 3</a><a> Link 4 </a></div><div class="content"><div class="box"><div class="box-header"><a> App </a></div><div class="box-content"><table summary="app content"><tr><td>Constructor</td></tr><tr><td>android.permission.ACCESS_COARSE_LOCATION</td></tr></table></div>')

def writePKG(var):

	print('<div class="box-header"><a> Package '+var+' </a><button onclick="toggle('+"'"+'packageContent'+var+"'"+')">ClickMe</button></div><div class="box" id="packageContent'+var+'">')

def writeClass(var):

	print('<div class="box-header"><a> Class '+var+'</a><button onclick="toggle('+"'"+'classContent'+var+"'"+')">ClickMe</button></div><div class="box-ar" id="classContent'+var+'">')

def classAddDesc(className,var):
	print('<div class="box-body" id="descContent'+className+'" ><table summary="Class content"><tr><td>'+var+'</td></tr></table></div>')
	
def writeImports(className, imps):

	print('<div class="box-header"><a> Imports </a><button type="button" onclick="toggle('+"'"+'importsContent'+className+"'"+')">ClickMe</button></div>')

	print('<div class="box-body" id="importsContent'+className+'" ><table summary="Import Content">')
	if isinstance(imps, list):
		for imports in imps:
			print('<tr><td>'+imports+'</td></tr>')
	else:
		print('<tr><td>'+imps+'</td></tr>')
	print('</table></div>')

def writeAttributes(className, attrs):

	print('<div class="box-header"><a> Attributes </a></div>')
	print('<div class="box-body"><table summary="Attributes Content">')
	if isinstance(attrs, list):
		for attributes in attrs:
        		print("<tr><td>Name</td><td>"+attributes['name']+"</td><td>Type</td><td>"+attributes['type']+"</td></tr>")
	else:
		print("<tr><td>Name</td><td>"+attrs['name']+"</td><td>Type</td><td>"+attrs['type']+"</td></tr>")

	print('</table></div>')
	
def writeDicMethods(className, meths):

	print('<div class="box-header"><a> Methods </a></div>')
	print('<div class="box-header"><a>'+meths['name']+'</a></div>')
	print('<div class="box-body"><table summary="l">')
	print("<tr><td>Description</td><td>"+str(meths['description'])+"</td></tr></table></div></div>")

def writeMethods(className, meths):
	
	print('<div class="box-header"><a> Methods </a></div>')
	for methods in meths:
		print('<div class="box-header"><a>'+methods['name']+'</a></div>')
		print('<div class="box-body"><table summary="Methods Content">')
		if 'parameters' in methods:
			if isinstance(methods['parameters']['parameter'], dict):
				print("<tr><td style='width: 25%;'>Parameter</td><td style='width: 25%;'>"+str(methods['parameters']['parameter']['param'])+"</td>")
				print("<td style='width: 25%;'>Output</td><td style='width: 25%;'>"+str(methods['parameters']['parameter']['output'])+"</td></tr>")
				print("<tr><td style='width: 25%;'>Description</td><td>"+str(methods['parameters']['parameter']['description'])+"</td></tr>")
				if 'return' in methods['parameters']['parameter']:
					for key in methods['parameters']['parameter']['return']:
						print("<tr><td style='width: 25%;'>Return</td><td style='width: 25%;'>"+key +"</td><td>"+methods['parameters']['parameter']['return'][key]+"</td></tr>")
	
			else:
				for p in methods['parameters']['parameter']:
					print("<tr><td style='width: 25%;'>Parameter</td><td style='width: 25%;'>"+str(p['param'])+"</td>")
					print("<td style='width: 25%;'>Output</td><td style='width: 25%;'>"+str(p['output'])+"</td></tr>")
					print("<tr><td style='width: 25%;'>Description</td><td>"+str(p['description'])+"</td></tr>")
					if 'return' in p:
						for key in p['return']:
                                                	print("<tr><td style='width: 25%;'>Return</td><td style='width: 25%;'>"+key +"</td><td>"+p['return'][key]+"</td></tr>")
        
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


path = j['app']['analisis']['packages']['pkg']
mal = 'malicious'

if isinstance(path, dict):
	path = [path]
	

def malicious(path):
	
	print('<div class="box-header"><a> Malicious artefacts </a></div>')
	for i in path:
		if mal in i:
			print('<div class="box-body"><table summary="malicious"><tr><td style="width: 10%;">Package</td><td style="width: 40%;">'+i['name']+'</td><td>'+i['malicious']+'</td></tr></table></div>')
		if isinstance(i['classes']['class'], dict):
			i['classes']['class'] = [i['classes']['class']]
		for className in i['classes']['class']:
			if mal in className:
				print('<div class="box-body"><table summary="malicious"><tr><td style="width: 10%;">Class</td><td style="width: 40%;">'+i['name']+'.<a style="color: red;">'+className['name']+'</a></td><td>'+className['malicious']+'</td></tr></table></div>')
			if (className['attributes']):
				if isinstance(className['attributes']['attribute'],list):
					for attr in className['attributes']['attribute']:
						if mal in attr:
							print('<div class="box-body"><table summary="malicious"><tr><td style="width: 10%;">Attribute</td><td style="width: 40%;">'+i['name']+'.'+className['name']+' <a style="color: red;">'+attr['name']+'</a></td><td>'+attr['malicious']+'</td></tr></table></div>')
				else:
					if mal in className['attributes']['attribute']:
						print('<div class="box-body"><table summary="malicious"><tr><td style="width: 10%;">Attribute</td><td style="width: 40%;">'+i['name']+'.'+className['name']+' <a style="color: red;">'+className['attributes']['attribute']['name']+'</a></td><td>'+className['attributes']['attribute']['malicious']+'</td></tr></table></div>')


			if (className['methods'] and not isinstance(className['methods']['method'], dict)):					
				for method in className['methods']['method']:
					if mal in method:	
						print('<div class="box-body"><table summary="malicious"><tr><td style="width: 10%;">Method</td><td style="width: 40%;">'+i['name']+'.'+className['name']+' <a style="color: red;">'+method['name']+'</a></td><td>'+str(method['malicious'])+'</td></tr></table></div>')
malicious(path)

for i in path:
	writePKG(i['name'])
	
	for className in i['classes']['class']:
		writeClass(className['name'])
		if 'description' in className:
			classAddDesc(className['name'], className['description'])

		if (className['imports']):
			writeImports(className['name'], className['imports']['import'])

		if (className['attributes'] ):
			writeAttributes(className['name'], className['attributes']['attribute'])
		if (className['methods'] and not isinstance(className['methods']['method'], dict)):
			writeMethods(className['name'], className['methods']['method'])

		elif (className['methods'] and isinstance(className['methods']['method'], dict)):
			writeDicMethods(className['name'], className['methods']['method'])	
			
print('</div></div></div></html>')



