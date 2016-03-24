from Aux import *

class Particle (object):
	def __init__(self,x,k):
		self.position = []
		for i in range (0,k):
			point = x[randint(0,len(x)-1)]
			while point in self.position:
				point = x[randint(0,len(x)-1)]
			self.position.append(point)
		self.velocity = [[0 for coord in cluster] for cluster in self.position]
		self.best = deepcopy(self.position)
		self.bestfit = 0

	def assign(self,x):
		output = []
		for point in x:
			distance = []
			for index,cluster in enumerate(self.position):
				distance.append(np.linalg.norm(np.array(point)-np.array(cluster)))
			output.append(np.argmin(distance))
		return output

	def elements (self,cluster,output):
		return np.where(np.array(output)==cluster)[0]

	def intracluster (self,x,output):
		intra = []
		for index,cluster in enumerate(self.position):
			xi = self.elements(index,output)
			dmax = 0
			for m,point1 in enumerate(xi):
				for point2 in xi[m+1:]:
					d = np.linalg.norm(np.array(x[point1])-np.array(x[point2]))
					if d > dmax:
						dmax = d
			intra.append(dmax)
		return intra

	def intercluster (self):
		inter = []
		for index,cluster1 in enumerate(self.position):
			for cluster2 in self.position[index+1:]:
				inter.append(np.linalg.norm(np.array(cluster1)-np.array(cluster2)))
		return inter

	def fitness (self,x):
		return min(self.intercluster())/max(self.intracluster(x,self.assign(x)))

def PSOPopulationInit (npart,x,k):
	return [Particle(x,k) for i in range (0,npart)]

def PSO (npart,k,in_max,in_min,c1,c2,maxit,arqStr):
	x,y = Inputs(arqStr)
	swarm = PSOPopulationInit(npart,x,k)
	fit = [particle.fitness(x) for particle in swarm]
	for particle,value in zip(swarm,fit):
		particle.bestfit = deepcopy(value)
	rho1 = [uniform(0,1) for i in range(0,len(x[0]))]
	rho2 = [uniform(0,1) for i in range(0,len(x[0]))]
	for i in range (0,maxit):
		inertia = (in_max-in_min)*((maxit-i+1)/maxit)+in_min
		print "Iteracao %s" % (i+1) ,
		fit = [particle.fitness(x) for particle in swarm]
		#if min(fit) < gbest.fitness(x,gbest.assign(x)):
		gbest = deepcopy(swarm[np.argmax(fit)])
		#update best
		for index,particle in enumerate(swarm):
			if fit[index] > particle.bestfit:
				particle.best = deepcopy(particle.position)
				particle.bestfit = deepcopy(fit[index])
		#update velocity and position
		for particle in swarm:
			particle.velocity = [map(float,j) for j in inertia*np.array(particle.velocity) + c1*np.array(rho1)*np.array(np.array(particle.best)-np.array(particle.position)) + c2*np.array(rho2)*np.array(np.array(gbest.position)-np.array(particle.position))]
			particle.position = [map(float,j) for j in np.array(particle.position)+np.array(particle.velocity)]
	fit = [particle.fitness(x) for particle in swarm]
	#best so far
	if max(fit) > gbest.fitness(x):
		gbest = swarm[np.argmax(fit)]
	print "\nFitness = %s" % gbest.fitness(x)
	#return best cluster
	return gbest.position

if __name__ == '__main__':
	print PSO(int(argv[1]),int(argv[2]),float(argv[3]),float(argv[4]),float(argv[5]),float(argv[6]),int(argv[7]),argv[8])