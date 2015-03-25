#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy import stats
from scipy.stats.stats import pearsonr
from scipy.stats import shapiro
from pylab import *

"""

ranking alternatif : 

((c-1)/(c^n -1))*c^(N-r)

r = rang
n = taille de pop
c = ]0;1[

"""

# def alea_mat2(length):
#         liste=[]
#         # sum_mat=0
#         # while sum_mat==0:
#         for i in range(length*length):
#                 n=np.random.rand()
#                 if n >0.99:
#                         liste.append(1)
#                 else:
#                         liste.append(0)
                
#         matrix=[]
#         #matrix=np.matrix(liste)
#         while liste!=[]:
#                 matrix.append(liste[:length])
#                 liste=liste[length:]
                
                
#         mat=np.triu(matrix)
        
    #         for j in range(length):
    #                 mat[j,j]=0
                    
#                 #sum_mat=np.matrix.sum(np.matrix(mat))
# 	print mat
# 	return mat



def alea_mat(length):
	mat=np.triu(np.matrix(np.random.choice(2,size=(length,length),p=[0.95,0.05])))
	for i in range(length):
		mat[i,i]=0
        graph=nx.from_numpy_matrix(mat)
        connected_comp=list(nx.connected_component_subgraphs(graph))
        print len(connected_comp)
        print mat
        nodes=[]
        for j in range(len(connected_comp)-1):
            print connected_comp[j].nodes()
            nodes.append((connected_comp[j].nodes()[0],connected_comp[j+1].nodes()[0]))
            
        graph.add_edges_from(nodes)
        mat=nx.to_numpy_matrix(graph)
        print nx.is_connected(graph)
        
            
            #nx.to_numpy_matrix(connected_comp[j])
            
        #print "nombre de connex", len(connected_comp)
                
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
    
        dic={}
        #print nx.degree(graph)
        #for i in range(len(nx.degree(graph))):
        #    for x in range(G.number_of_nodes()):
        #        liste=[]
        #        if G.degree(graph.nodes(x))==i:
        #            liste.append(G.degree(graph.nodes(x)))              
        #    dic[i]=nx.average_clustering(liste)
            
        liste=[]
        print nx.degree(graph)
        for j in range(len(nx.degree(graph))):
            liste.append([i for i in graph.nodes() if graph.degree(i)==j])
            print "liste[j]:",liste[j],"\n"
            #dic[j]=nx.average_clustering(graph,liste[j])
        ##print list
        #
        x= dic.keys()
        y=dic.values()
        print x,y
        plot(x,y)
        show() 
        ##clust=nx.clustering(graph)
        #degree=nx.degree(graph)
	#x=[clust[key] for key in clust.keys()]
	#y=[degree[key] for key in degree.keys()]
	#a,b= pearsonr(x,y)
	#print "coeff pearson",pearsonr(x,y)
        #print "correlation clustering avec degres: \n",(a,b),"\n"
	#return pearsonr(x,y)
	return 1
	#Scale-free
def scale_free(G):
        P=nx.degree_histogram(G)
        x=[]
        y=[]
        nb_nodes=G.number_of_nodes()
        for k in range(len(P)):
                if P[k]!=0 and k!=0:
                        x.append(log(k))
                        y.append(log(1.0*P[k]/nb_nodes))
        slope,intercept,r_value,p_value, std_err=stats.linregress(x,y)
        #print "scale free r-value: \n",r_value**2,"\n" #0.7988,
        #print "scale free slope: \n",slope, "\n" #-1.5
        #plt.plot(x,y)
        #plt.show()
        return r_value**2-0.1*abs(1.5+slope)

def small_word(graph,coeff_SPL,coeff_connectivite):
	assert (coeff_SPL + coeff_connectivite == 1),"Coefficient sum not equal to 1"
	clus=int(nx.is_connected(graph))	
	if clus==1:
		ASPL=nx.average_shortest_path_length(graph)
	else :
		liste_ASPL=[]
		liste_nb_edges=[]
                connected_comp=nx.connected_component_subgraphs(graph)
                
		for g in connected_comp:
                        if g.number_of_nodes()==1:
                                liste_ASPL.append(0)
                                liste_nb_edges.append(0)
                        else:
                                liste_ASPL.append(nx.average_shortest_path_length(g))
                                liste_nb_edges.append(g.number_of_edges())
		ASPL=np.average(a=liste_ASPL,weights=liste_nb_edges)
	res=coeff_SPL*ASPL + coeff_connectivite*clus*1.0
        
	#print "Coeff small world ",res
	return (res)
	
	
############################################################################


#crée une mtrice aléatoire de 1 et 0 (que sur le triangle supérieur droit et pas sur la diagonale)

mat=alea_mat(500)
#mat2=alea_mat2(100)

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

#print("Description du graph biologique")
#print "Nombre de noeuds : ",G.number_of_nodes()
#print "Nombre de liens : ",G.number_of_edges()
#print "Est-il connexe ? ",nx.is_connected(G)
#print "Nombre de composante connexe : ",nx.number_connected_components(G),"\n"

connected_subgraph=nx.connected_component_subgraphs(G)
i=1
for graph in connected_subgraph:
	if i==1:
		Gbis=graph.copy()
	#print "Description du sous-graph biologique ",i
	#print "Nombre de noeuds : ",graph.number_of_nodes()
	#print "Nombre de liens : ",graph.number_of_edges()
	#print "Est-il connexe ? ",nx.is_connected(graph)
	#print "Nombre de composante connexe : ",nx.number_connected_components(graph),"\n"
	i+=1

#print "Conclusion il faut prendre le plus grand des sous-graph connexe biologique pour faire notre modele"

#deg_distribution(Gbis)
#SPL_distribution(Gbis)
#corr_clus_deg(Gbis)
#scale_free(Gbis)
#small_word(Gbis,0.5,0.5)

#plt.show()


