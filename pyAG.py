from random import *
from graph import * 
from copy import deepcopy
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

class individu:
    def __init__(self,ge=None):
	if ge is None :
	    self.genome=alea_mat(100)
	    self.graph=nx.from_numpy_matrix(self.genome)
	    self.fit=-1
	else:
	    self.genome=ge[:]
	    self.graph=nx.from_numpy_matrix(self.genome)
            self.fit=-1
		
    def fitness(self):
        
        
        fit = 0
        fit += SPL_distribution(self.graph)[0]*10
        #fit += small_word(self.graph,0.8,0.2) *10
        fit += nx.is_connected(self.graph)*20
        fit += corr_clus_deg(self.graph)*10
        fit += scale_free(self.graph)*10
	#r=0
	#g = 0
	#for i,x in enumerate(self.genome[1,:]):
	#    r+= 2*x-1
	#    if i>1000:
	#	if r>4 or r<-4:
	#	    g+=1
 #           
	#return g
        return fit
	
    def maj_graphe(self):
	self.graph=nx.from_numpy_matrix(self.genome)



def index(N,x):
    ind = 0
    j=0
    while x>ind:
	ind += N-j
	j+=1
    return j-1

class population:
	
    def __init__(self,N,prod,txMut,txCross):
	self.N=N
	self.txMut=txMut
	self.txCross=txCross
        self.prod=prod
	self.pop=[prod() for i in range(N)]
	self.gen = 0

	
    def calc_fitness(self):
	self.f=[]
	self.fitm=0 ## moyenne
	self.fim=1000 ## min
 	for i,x in enumerate(self.pop):
	    fi=x.fitness()
	    self.fitm += fi
	    if self.fim>fi:
		self.fim=fi
	    self.f.append([fi,i])
	self.f.sort()
        #self.f.sort(reverse=True)
        #print "F",self.f
	self.fitm/=1.0*self.N
	
    def new_pop(self):
	self.npop=[]
	for x in range(self.N/2,self.N):
            self.npop.append(self.prod(self.pop[self.f[x][1]].genome))
            self.npop.append(self.prod(self.pop[self.f[x][1]].genome))
            #self.npop.append(self.prod(self.pop[self.f[x][1]].genome) for x in range(1,self.N/2))
            #self.npop.append(self.prod(self.pop[self.f[x][1]].genome) for x in range(1,self.N/2))
	    #r= randint(0,(self.N+1)*(self.N)/2)
	    #x=index(self.N,r)
	    #print x,self.f[x][0]
	    #self.npop.append(self.prod(self.pop[self.f[x][1]].genome))

    def mutation(self):
	for x in self.npop:
            g = deepcopy(x.genome)
            for i in range(len(g)):
                for j in range(i+1,len(g)):
                    if random()<self.txMut:
                        g[i+1,j]=1-g[i+1,j]
    
            x.genome=deepcopy(g)
        

    def cross(self):
        for x in self.npop:
            if random()<self.txCross:
                g = x.genome
                r1= self.pop[randint(0,self.N-1)].genome
                z= randint(0,len(g)-1)
                if random()<0.5:
                    g[0:z]=r1[0:z]
                else:
                    g[z:]=r1[z:]
                x.genome=g
    
    def update(self):
	self.pop=self.npop[:]
        for x in self.pop:
            x.maj_graphe()

    def genloop(self):
	ga.calc_fitness()
	self.new_pop()
	self.mutation()
	self.cross()
	self.update()
	self.gen += 1
        #print self.pop[1].genome
	print self.fitm,self.fim,'\n',[nx.is_connected(self.pop[i].graph) for i in range(len(self.pop))]
        print [nx.number_of_edges(self.pop[i].graph)*2.0/10000 for i in range(len(self.pop))]


nb_iter=20
seed()
y=[]
ga=population(100,individu,0.005,0.05)

# for i in range(10):
#     y.append(ga.pop[i].fitness())
#     print ga.pop[i].genome

# print y
#print ga.pop[1].genome
#ga.genloop()
#print ga.pop[1].genome

for i in range(nb_iter):
    ga.genloop()
    y.append(ga.fitm)
    
y=np.asarray(y)

#r=0
#f=open("btr2.dat","w")
#for x in ga.pop[ga.f[0][1]].genome:
#    r+=2*x-1
#    f.write("%d\n"%r)
#f.close()





# lines=open('coliInterNoAutoRegVec.txt',"r").readlines()
# liste=[line.split(" ")[0:2] for line in lines]

# G=nx.Graph()
# G.add_edges_from(liste)
# matrix=nx.to_numpy_matrix(G)
# copain2=individu(matrix)
# print "fit ECOLI:",copain2.fitness()


fig = plt.figure()
x=np.arange(0,nb_iter,1)
plot(x,y)
title("evolution de la fitness moyenne")
xlabel("nombre d'iterations")
ylabel("fitness")
show()
