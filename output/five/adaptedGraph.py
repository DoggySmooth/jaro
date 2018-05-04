import json, graphviz as gv, sys

g = gv.Graph(format='svg')

j = json.load(open(sys.argv[1]))

if isinstance(j['app']['analisis']['packages']['pkg'], dict):

	way = [j['app']['analisis']['packages']['pkg']]
else:
	way = j['app']['analisis']['packages']['pkg']

g.node('packages', shape='square')
for l in range(len(way)):
	
	if 'malicious' in way[l]:
		g.node(way[l]['name'], style='filled', fillcolor='red')

	else:
		g.node(way[l]['name'])

	g.edge('packages', way[l]['name'])
	g.node('class'+way[l]['name'], 'class', shape='square')
	g.edge(way[l]['name'], 'class'+way[l]['name'])
	if isinstance(way[l]['classes']['class'], dict):
		path = [way[l]['classes']['class']]
	else:
		path = way[l]['classes']['class']


	for i in range(len(path)):
		print(i)
		if 'malicious' in path[i]:
			g.node(path[i]['name'],style='filled', fillcolor="red")
		else:
			g.node(path[i]['name'])

		g.edge('class'+way[l]['name'], path[i]['name'])
		g.node('imports'+path[i]['name'], 'imports')
		g.edge(path[i]['name'], 'imports'+path[i]['name'])
		if 'imports' in path[i] and path[i]['imports'] is not None:
			if isinstance(path[i]['imports']['import'], list):
				for elements in path[i]['imports']['import']:
					g.node( elements)
					g.edge('imports'+path[i]['name'], elements)
	
			else:
				g.node(path[i]['imports']['import'])
				g.edge('imports'+path[i]['name'], path[i]['imports']['import'])
		
		g.node('methods'+path[i]['name'], 'methods')
		g.edge(path[i]['name'], 'methods'+path[i]['name'])
		if 'methods' in path[i] and path[i]['methods'] is not None:
			if isinstance(path[i]['methods']['method'], list):
				for elements in path[i]['methods']['method']:
					if 'malicious' in elements:
						g.node(elements['name']+path[i]['name'],elements['name'], style="filled", fillcolor="red")
					else:
						g.node(elements['name']+path[i]['name'] , elements['name'])
					g.edge('methods'+path[i]['name'], elements['name']+path[i]['name'])
			else:
				if 'malicious' in path[i]['methods']['method']:
					g.node(path[i]['methods']['method']['name'], style='filled', fillcolor='red')
				else:
					g.node(path[i]['methods']['method']['name'])
				g.edge('methods'+path[i]['name'], path[i]['methods']['method']['name'])
		g.node('attributes'+path[i]['name'], 'attributes')
		g.edge(path[i]['name'], 'attributes'+path[i]['name'])
		if 'attributes' in path[i] and path[i]['attributes'] is not None:
			if isinstance(path[i]['attributes']['attribute'], list):
				for elements in path[i]['attributes']['attribute']:
					if 'malicious' in elements:
						g.node( elements['name'], style="filled", fillcolor="red")
					g.edge('attributes'+path[i]['name'], elements['name'])
			else:
				if 'malicious' in path[i]['attributes']['attribute']:
					g.node(path[i]['attributes']['attribute']['name'], style="filled", fillcolor="red")
				else:
					g.node(path[i]['attributes']['attribute']['name'])
				g.edge('attributes'+path[i]['name'], path[i]['attributes']['attribute']['name'])
g.render()
		
