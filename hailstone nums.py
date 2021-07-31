import matplotlib.pyplot as plt
import networkx as nx

class Hailstone():
  frequency= {}
  g = nx.DiGraph()
  def __init__(self,num):
    Hailstone.g.add_node(num)
    hsnums = Hailstone.hailstonenums(num)
    keys = set(hsnums)
    for key in keys:
      if key in Hailstone.frequency:
        Hailstone.frequency[key] += hsnums.count(key)
      else:
        Hailstone.frequency[key] = hsnums.count(key)
  def hailstonenums(seed):
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
    keys = Hailstone.frequency.keys()
    values = Hailstone.frequency.values()
    plt.bar(keys, values)
  def tree():
    x = nx.DiGraph(set(Hailstone.g.edges()))
    nx.draw(x,with_labels=1)
for i in range(1,15):
  x = Hailstone(i)
Hailstone.bardisplay()