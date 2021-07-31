import matplotlib.pyplot as plt
import networkx as nx
from tabulate import tabulate

class Hailstone():
  frequency= {}
  g = nx.DiGraph()
  seeder = []
  
  def __init__(self,num):
    Hailstone.g.add_node(num)
    hsnums = Hailstone.hailstonenums(num)
    Hailstone.seeder.append((num,hsnums))
    keys = set(hsnums)
    for key in keys:
      if key in Hailstone.frequency:
        Hailstone.frequency[key] += hsnums.count(key)
      else:
        Hailstone.frequency[key] = hsnums.count(key)
  
  def hailstonenums(seed):
    '''The theory logic'''
    hsnums = []
    prev = seed
    while seed != 1:
      if seed%2 == 0:
        seed = int(seed/2)
      else:
        seed = 3*seed + 1
      hsnums.append(seed)
      Hailstone.g.add_node(seed)
      Hailstone.g.add_edge(prev,seed)
    return(hsnums)
  
  def bardisplay():
    '''A Bar distribution of Hailstone numbers'''
    keys = Hailstone.frequency.keys()
    values = Hailstone.frequency.values()
    plt.bar(keys, values)
  
  def tree():
    '''
    Network structure of the relationship.
    P.S. Only compatible with small range of inputs.
    '''
    x = nx.DiGraph(set(Hailstone.g.edges()))
    nx.draw(x,with_labels=1)
  
  def data():
    '''Table display of the data'''
    mydata = Hailstone.seeder
    header = ["Number", "Hailstone List"]
    print(tabulate(mydata, headers=header, tablefmt="grid"))
  
#Input numbers
for i in range(1,15):
  x = Hailstone(i)
#Method Calls
Hailstone.bardisplay()
Hailstone.data()
