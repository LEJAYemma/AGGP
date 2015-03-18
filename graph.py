#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy import stats

"""

ranking alternatif : 

((c-1)/(c^n -1))*c^(N-r)

r = rang
n = taille de pop
c = ]0;1[

"""

def alea_mat(length):
	mat=np.triu(np.matrix(np.random.randint(2,size=(length,length))))
	for i in range(length):
		mat[i,i]=0
	return mat
	
def deg_distribution(graph):
	plt.figure()
	l_dist={}
	for key in (nx.degree(graph)):
		if l_dist.has_key(nx.degree(graph)[key])==True:
			l_dist[nx.degree(graph)[key]]+=1
		
		else :
			l_dist[nx.degree(graph)[key]]=1
		
	x=range(len(l_dist))
	y=[l_dist[i] for i in sorted(l_dist)]

	plt.bar(x, y, align='center')
	plt.xticks(range(len(l_dist)), sorted(l_dist))
	plt.title("Distribution des degres des noeuds du graphe")

        return ((x,y))

def plot_graph(graph):
	
	pos=nx.spring_layout(G)
	pos2=nx.circular_layout(G)
	pos3=nx.random_layout(G)
	pos4=nx.shell_layout(G)
	pos5=nx.spectral_layout(G)

	plt.figure()
	# nodes
	nx.draw_networkx_nodes(G,pos,node_size=700)
	# edges
	nx.draw_networkx_edges(G,pos,alpha=0.5,edge_color='b')
	# labels
	nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
	plt.axis('off')
	plt.title("Graphe en position spring")

	plt.figure()
	# nodes
	nx.draw_networkx_nodes(G,pos2,node_size=700)
	# edges
	nx.draw_networkx_edges(G,pos2,alpha=0.5,edge_color='b')
	# labels
	nx.draw_networkx_labels(G,pos2,font_size=20,font_family='sans-serif')
	plt.axis('off')
	plt.title("Graphe en position circulaire")

	# plt.figure()
	# # nodes
	# nx.draw_networkx_nodes(G,pos3,node_size=700)
	# # edges
	# nx.draw_networkx_edges(G,pos3,alpha=0.5,edge_color='b')
	# # labels
	# nx.draw_networkx_labels(G,pos3,font_size=20,font_family='sans-serif')
	# plt.axis('off')
	# plt.title("Graphe en position random")

	plt.figure()
	# nodes
	nx.draw_networkx_nodes(G,pos4,node_size=700)
	# edges
	nx.draw_networkx_edges(G,pos4,alpha=0.5,edge_color='b')
	# labels
	nx.draw_networkx_labels(G,pos4,font_size=20,font_family='sans-serif')
	plt.axis('off')
	plt.title("Graphe en position shell")

	plt.figure()
	# nodes
	nx.draw_networkx_nodes(G,pos5,node_size=700)
	# edges
	nx.draw_networkx_edges(G,pos5,alpha=0.5,edge_color='b')
	# labels
	nx.draw_networkx_labels(G,pos5,font_size=20,font_family='sans-serif')
	plt.title("Graphe en position spectral")
	plt.axis('off')

#crée une mtrice aléatoire de 1 et 0 (que sur le triangle supérieur droit et pas sur la diagonale)
mat=alea_mat(500)
#Fait de cette matrice un graph
G=nx.Graph()
edges=[]
f=open('ColiNet-1.0/coliInterNoAutoRegVec.txt','r')
for line  in f.readlines():
        edges.append((int(line.split(' ')[0]),int(line.split(' ')[1])))
G.add_edges_from(edges)
f.close()


#calcul et plot la distribution des degrée des noeuds du graph
#deg_distribution(G)

#Représente le graph avec différentes position pour les noeuds
#plot_graph(G)
#plt.show() # display



#Scale-free
def scale_free(G):
        P=nx.degree_histogram(G)
        x=[]
        y=[]
        for k in range(len(P)):
                if P[k]!=0 :
                        x.append(log(k))
                        y.append(log(1.0*P[k]/G.number_of_nodes()))
        slope,intercept,r_value,p_value, std_err=stats.linregress(x,y)
        print r_value**2 #0.7988
        print slope #-1.5
        plt.plot(x,y)
        plt.show()


#Test scale-free graphe random
G2=nx.from_numpy_matrix(mat)
scale_free(G2)



