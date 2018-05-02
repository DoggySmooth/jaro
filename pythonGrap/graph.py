import json
import graphviz as gv
import sys

g = gv.Graph(format='svg')


j = json.load(open(sys.argv[1]))


path = j['app']['analisis']['packages']['pkg']['classes']['class']

for i in range(len(path)):

	g.node('class', shape='square')

	if 'malicious' in path[i]:
	
		g.node(path[i]['name'],style='filled', fillcolor="red")
	else:
		g.node(path[i]['name'])


	
	g.edge('class', path[i]['name'])
	
	if (path[i]['imports'] and not isinstance(path[i]['imports']['import'],dict)):
 
		g.node('imports'+path[i]['name'], 'imports',  shape='egg')
		g.edge(path[i]['name'], 'imports'+path[i]['name'])	
		for x in range(len(path[i]['imports']['import'])):
			g.node(path[i]['imports']['import'][x]+path[i]['name'], path[i]['imports']['import'][x], shape='egg')
			g.edge('imports'+path[i]['name'], path[i]['imports']['import'][x]+path[i]['name'])
			
	elif (path[i]['imports']):
		g.node('imports'+path[i]['name'], 'imports')	
		g.edge(path[i]['name'], 'imports'+path[i]['name'])

		g.node(path[i]['imports']['import'][0]+path[i]['name'], path[i]['imports']['import'][0])
		g.edge('imports'+path[i]['name'], path[i]['imports']['import'][0]+path[i]['name'])


	if (path[i]['attributes']) and not isinstance(path[i]['attributes']['attribute'],dict):
		
		g.node('attributes'+path[i]['name'], 'attributes',  shape='egg')
		g.edge(path[i]['name'], 'attributes'+path[i]['name'])
		for x in range(len(path[i]['attributes']['attribute'])):
			
			if 'malicious' in path[i]['attributes']['attribute'][x]:
				g.node(path[i]['attributes']['attribute'][x]['name']+path[i]['name'], path[i]['attributes']['attribute'][x]['name'], style="filled", fillcolor="red")

			else:
				g.node(path[i]['attributes']['attribute'][x]['name']+path[i]['name'], path[i]['attributes']['attribute'][x]['name'])
			
			g.edge('attributes'+path[i]['name'], path[i]['attributes']['attribute'][x]['name']+path[i]['name'])	
	elif (path[i]['attributes']):
		g.node('attributes'+path[i]['name'], 'attributes')	
		g.edge(path[i]['name'], 'attributes'+path[i]['name'])
		if 'malicious' in path[i]['attributes']['attribute']:
			g.node(path[i]['attributes']['attribute']['name']+path[i]['name'], path[i]['attributes']['attribute']['name'], style="filled", fillcolor="red")

		else:
			g.node(path[i]['attributes']['attribute']['name']+path[i]['name'], path[i]['attributes']['attribute']['name'])
		
		g.edge('attributes'+path[i]['name'], path[i]['attributes']['attribute']['name']+path[i]['name'])


	if (path[i]['methods'] and not isinstance(path[i]['methods']['method'],dict)):
		g.node('methods'+path[i]['name'], 'methods')	
		g.edge(path[i]['name'], 'methods'+path[i]['name'])
		for x in range(len(path[i]['methods']['method'])):
			if 'malicious' in path[i]['methods']['method'][x]:
				g.node(path[i]['methods']['method'][x]['name']+path[i]['name'], path[i]['methods']['method'][x]['name'], style="filled", fillcolor="red")

			else:
				g.node(path[i]['methods']['method'][x]['name']+path[i]['name'], path[i]['methods']['method'][x]['name'])
			g.edge('methods'+path[i]['name'], path[i]['methods']['method'][x]['name']+path[i]['name'])
	elif (path[i]['methods']):
		g.node('methods'+path[i]['name'], 'methods')	
		g.edge(path[i]['name'], 'methods'+path[i]['name'])
		if 'malicious' in path[i]['methods']['method']:
			g.node(path[i]['methods']['method']['name']+path[i]['name'], path[i]['methods']['method']['name'], style="filled", fillcolor="red")

		else:
			g.node(path[i]['methods']['method']['name']+path[i]['name'], path[i]['methods']['method']['name'])
		g.edge('methods'+path[i]['name'], path[i]['methods']['method']['name']+path[i]['name'])

print('------------------------------------------')


print('------------------------------------------')

if g.render():
	print('Graph Generated')
