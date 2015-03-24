from random import *
from graph import * 
import copy
class individu:
    def __init__(self,ge=None):
	if ge is None :
	    self.genome=alea_mat2(100)
	    self.graph=nx.from_numpy_matrix(self.genome)
	    self.fit=-1
	else:
	    self.genome=ge[:]
	    self.graph=nx.from_numpy_matrix(self.genome)
            self.fit=-1
		
    def fitness(self):
        
        graph=self.graph
        fit = 0
        fit += SPL_distribution(graph)[0]*10
        fit += small_word(graph,0.8,0.2) *10
        fit -= corr_clus_deg(graph)[0] *10
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
	self.fitm=0
	self.fim=1000
	for i,x in enumerate(self.pop):
	    fi=x.fitness()
	    self.fitm += fi
	    if self.fim>fi:
		self.fim=fi
	    self.f.append([fi,i])
	self.f.sort()
	self.fitm/=1.0*self.N
	
    def new_pop(self):
	self.npop=[]
	for i in range(self.N):
	    r= randint(0,(self.N+1)*(self.N)/2)
	    x=index(self.N,r)
	    ##print x,self.f[x][0]
	    self.npop.append(self.prod(self.pop[self.f[x][1]].genome))

    def mutation(self):
	for x in self.npop:
            g = x.genome
            for i in range(len(g[1,:])):
                for j in range(i+1,len(g[1,:])):
                    if random()<self.txMut:
                        g[i+1,j]=1-g[i+1,j]
            x.genome=copy.deepcopy(g)

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
	print self.fitm,self.fim

seed(11)

#ga=population(10,individu,0.0001,0.5)
#print ga.pop[1].genome
#ga.genloop()
#print ga.pop[1].genome

#for i in range(1000):
#    ga.genloop()

#r=0
#f=open("btr2.dat","w")
#for x in ga.pop[ga.f[0][1]].genome:
#    r+=2*x-1
#    f.write("%d\n"%r)
#f.close()


## Ca c'est juste pour tester la fitness sur 1 individu
## et voir comment elle evolue sur 1 pas de temps
copain =individu()
g = copain.genome
print g
#plot_graph(copain.graph)
print copain.fitness()


for i in range(len(g[1,:])):
    for j in range(i+2,len(g[1,:])):
        if random()<0.5:
            g[i+1,j]=1-g[i+1,j]
copain.genome=copy.deepcopy(g)
copain.maj_graphe()
print copain.genome

print copain.fitness()
