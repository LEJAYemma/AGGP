#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.stats import pearsonr

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
	dico_degre=nx.degree(graph)
	for key in (dico_degre):
		if l_dist.has_key(dico_degre[key])==True:
			l_dist[dico_degre[key]]+=1
		
		else :
			l_dist[dico_degre[key]]=1
		
	x=range(len(l_dist))
	y=[l_dist[i] for i in sorted(l_dist)]

	plt.bar(x, y, align='center')
	plt.xticks(range(len(l_dist)), sorted(l_dist))
	plt.title("Distribution des degres des noeuds du graphe")

def SPL_distribution(graph):
	plt.figure()
	l_dist={}
	liste=[]

	SPLdico=nx.shortest_path_length(graph)
	for key in (SPLdico):
		liste.append(SPLdico[key].values())	

	C = [item for sublist in liste for item in sublist]
	
	plt.hist(C,histtype='stepfilled',facecolor='green')
	plt.title('Main Plot Title',fontsize=25,horizontalalignment='right')
	plt.ylabel('Count',fontsize=20)
	plt.yticks(fontsize=15)
	plt.xlabel('X Axis Label',fontsize=20)
	plt.xticks(fontsize=15)
	plt.show()
	
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

#	plt.figure()
	# nodes
#	nx.draw_networkx_nodes(G,pos2,node_size=700)
	# edges
#	nx.draw_networkx_edges(G,pos2,alpha=0.5,edge_color='b')
	# labels
#	nx.draw_networkx_labels(G,pos2,font_size=20,font_family='sans-serif')
#	plt.axis('off')
#	plt.title("Graphe en position circulaire")

#	plt.figure()
	# nodes
#	nx.draw_networkx_nodes(G,pos3,node_size=700)
	# edges
#	nx.draw_networkx_edges(G,pos3,alpha=0.5,edge_color='b')
	# labels
#	nx.draw_networkx_labels(G,pos3,font_size=20,font_family='sans-serif')
#	plt.axis('off')
#	plt.title("Graphe en position random")

#	plt.figure()
	# nodes
#	nx.draw_networkx_nodes(G,pos4,node_size=700)
	# edges
#	nx.draw_networkx_edges(G,pos4,alpha=0.5,edge_color='b')
	# labels
#	nx.draw_networkx_labels(G,pos4,font_size=20,font_family='sans-serif')
#	plt.axis('off')
#	plt.title("Graphe en position shell")

#	plt.figure()
	# nodes
#	nx.draw_networkx_nodes(G,pos5,node_size=700)
	# edges
#	nx.draw_networkx_edges(G,pos5,alpha=0.5,edge_color='b')
	# labels
#	nx.draw_networkx_labels(G,pos5,font_size=20,font_family='sans-serif')
#	plt.title("Graphe en position spectral")
#	plt.axis('off')

def corr_clus_deg(graph){
	x=[nx.clustering(graph)[key] for key in nx.clustering(graph).keys()]
	y=[nx.degree(graph)[key] for key in nx.degree(graph).keys()]
	print (pearsonr(x,y))
}



#crée une mtrice aléatoire de 1 et 0 (que sur le triangle supérieur droit et pas sur la diagonale)
#mat=alea_mat(1000)


#Fait de cette matrice un graph
#G=nx.from_numpy_matrix(mat)

#G=nx.erdos_renyi_graph(1000,0.5)

#calcul et plot la distribution des degrée des noeuds du graph
#deg_distribution(G)

#Représente le graph avec différentes position pour les noeuds
#plot_graph(G)
#display

lines=open('coliInterNoAutoRegVec.txt',"r").readlines()
liste=[line.split(" ")[0:2] for line in lines]

G=nx.Graph()
G.add_edges_from(liste)


#print (G.number_of_nodes())
#print (G.number_of_edges())

#print(nx.clustering(G))
#print(nx.degree(G))
#print(nx.average_clustering(G))

#print(nx.shortest_path_length(G))

#print(nx.shortest_path_length(G)['5'])

corr_clus_deg(G)

SPL_distribution(G)
#plt.show()




