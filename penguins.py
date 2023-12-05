import pandas as pd 
penguins_size = pd.read_csv('penguins_size.csv')
print(penguins_size)
species_island = penguins_size[['species', 'island']].drop_duplicates()
print(species_island)
species = penguins_size['species']
colour = []
for i in range(len(penguins_size)):
  if species[i] == 'Adelie':
      colour.append('red')
  elif species[i] == 'Gentoo':
      colour.append('blue')
  else:
    colour.append('olive')
penguins_size['colour'] = colour
same_graph = penguins_size.plot.scatter(x = 'flipper_length_mm', y = 'culmen_length_mm', c = 'colour').get_figure()
same_graph.savefig('same_graph.png')
for key, frame in penguins_size.groupby('species'):
  different_graphs = frame.plot.scatter(x = 'flipper_length_mm', y= 'culmen_length_mm', title = 'TEST', s = 100).get_figure()
  different_graphs.savefig('graph'+str(key)+'.png')