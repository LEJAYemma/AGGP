import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import *
from math import *
from scipy import stats
from scipy.stats.stats import pearsonr
from scipy.stats import shapiro
from pylab import *
from graph import * 
from copy import deepcopy
from enthought.mayavi import mlab


#H=nx.cycle_graph(20)
G= nx.read_graphml("ntest17.graphml")



G=nx.convert_node_labels_to_integers(G)

# 3d spring layout
pos=nx.spring_layout(G,dim=3)

# numpy array of x,y,z positions in sorted node order
xyz=np.array([pos[v] for v in sorted(G)])

# scalar colors
scalars=np.array(G.nodes())+5


mlab.figure(1, bgcolor=(0, 0, 0))

mlab.clf()
pts = mlab.points3d(xyz[:,0], xyz[:,1], xyz[:,2],
                    scalars,
                    scale_factor=0.01,
                    scale_mode='none',
                    colormap='Blues',
                    resolution=20)

pts.mlab_source.dataset.lines = np.array(G.edges())

tube = mlab.pipeline.tube(pts, tube_radius=0.001)

mlab.pipeline.surface(tube, color=(0.8, 0.8, 0.8))


mlab.savefig('mayavi2_spring.png')



mlab.show() # interactive window
