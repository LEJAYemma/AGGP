#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy import stats
from scipy.stats.stats import pearsonr
from scipy.stats import shapiro

"""

ranking alternatif : 

((c-1)/(c^n -1))*c^(N-r)

r = rang
n = taille de pop
c = ]0;1[

"""

def alea_mat2(length):
        liste=[]
        for i in range(length*length):
                n=np.random.rand()
                if n >0.9:
                        liste.append(1)
                else:
                        liste.append(0)
        
        matrix=[]
        while liste!=[]:
                matrix.append(liste[:length])
                liste=liste[length:]
                
        
        mat=np.triu(matrix)
        
	for j in range(length):
		mat[j,j]=0
	#print mat
	return mat

def alea_mat(length):
	mat=np.triu(np.matrix(np.random.randint(2,size=(length,length))))
	for i in range(length):
		mat[i,i]=0
	return mat
	
def deg_distribution(graph):
	#plt.figure()
	l_dist={}
	dico_degre=nx.degree(graph)
	for key in (dico_degre):
		if l_dist.has_key(dico_degre[key])==True:
			l_dist[dico_degre[key]]+=1
		
		else :
			l_dist[dico_degre[key]]=1
		
	x=range(len(l_dist))
	y=[l_dist[i] for i in sorted(l_dist)]

	#plt.bar(x, y, align='center')
	#plt.xticks(range(len(l_dist)), sorted(l_dist))
	#plt.title("Distribution des degres des noeuds du graphe")

        return ((x,y))

def SPL_distribution(graph):
	#plt.figure()
	l_dist={}
	liste=[]

	SPLdico=nx.shortest_path_length(graph)
	for key in (SPLdico):
		liste.append(SPLdico[key].values())	

	C = [item for sublist in liste for item in sublist]
	
	#plt.hist(C,histtype='stepfilled',facecolor='green')
	#plt.title('Main Plot Title',fontsize=25,horizontalalignment='right')
	#plt.ylabel('Count',fontsize=20)
	#plt.yticks(fontsize=15)
	#plt.xlabel('X Axis Label',fontsize=20)
	#plt.xticks(fontsize=15)
	#plt.show()
	#print 'normalite : \n',(shapiro(C)),"\n"
	return (shapiro(C))
	
def plot_graph(G):
	
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
        plt.show()

def corr_clus_deg(graph):

	x=[nx.clustering(graph)[key] for key in nx.clustering(graph).keys()]
        #print x
	y=[nx.degree(graph)[key] for key in nx.degree(graph).keys()]
	#a,b= pearsonr(x,y)
	#print pearsonr(x,y)#print "correlation clustering avec degres: \n",(a,b),"\n"
	return pearsonr(x,y)
	
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
        print "scale free r-value: \n",r_value**2,"\n" #0.7988,
        print "scale free slope: \n",slope, "\n" #-1.5
        #plt.plot(x,y)
        #plt.show()
        return r_value**2

def small_word(graph,coeff_SPL,coeff_connectivite):
	assert (coeff_SPL + coeff_connectivite == 1),"Coefficient sum not equal to 1"
	clus=int(nx.is_connected(graph))	
	if clus==1:
		ASPL=nx.average_shortest_path_length(graph)
	else :
		liste_ASPL=[]
		liste_nb_edges=[]
		for g in nx.connected_component_subgraphs(G):
			liste_ASPL.append(nx.average_shortest_path_length(g))
			liste_nb_edges.append(g.number_of_edges())
		ASPL=np.average(a=liste_ASPL,weights=liste_nb_edges)
	res=coeff_SPL*ASPL + coeff_connectivite*clus*1.0
	#print "Coeff small world ",res
	return (res)
	
	
############################################################################


#crée une mtrice aléatoire de 1 et 0 (que sur le triangle supérieur droit et pas sur la diagonale)

mat=alea_mat(500)
mat2=alea_mat2(100)

#graphe de reference

lines=open('coliInterNoAutoRegVec.txt',"r").readlines()
liste=[line.split(" ")[0:2] for line in lines]

G=nx.Graph()
G.add_edges_from(liste)

#G=nx.erdos_renyi_graph(1000,0.5)  : random graph

#calcul et plot la distribution des degrée des noeuds du graph
#deg_distribution(G)

#Représente le graph avec différentes position pour les noeuds
#plot_graph(G)

#plt.show() # display

#Fait de cette matrice un graph
#G2=nx.from_numpy_matrix(mat2)

#teste le scale free
#scale_free(G)
#teste si le coeff de clusterinf est dependant du degré
#corr_clus_deg(G)
#distribution des shortest path lengths: distribution normale? (shapiro)
#SPL_distribution(G)

#print (G.number_of_nodes())
#print (G.number_of_edges())

#print(nx.clustering(G))
#print(nx.degree(G))
#print(nx.average_clustering(G))

#print(nx.shortest_path_length(G))

#print(nx.shortest_path_length(G)['5'])

#plt.show()
#print("Graph aleatoire")
#small_word(G2,0.5,0.5)
#print("Graph biologique")
#small_word(G,0.5,0.5)

