# clustering
Clustering techniques using Genetic Algorithms and Particle Swarm Optimization

# genetic algorithm
A genetic algorithm is based on Darwin's ideas of evolution. Basically, it takes a population of n individuals, initializes them as possible solutions to a problem, and through crossovers, mutations, and sometimes reproductions, evolves the population until some condition is satisfied.

In this approach, the algorithm aims to discover coordinates to some clusters. It assumes prior knowledge of the problem, i.e., the number of clusters. The population will be of n individuals, aimed to find the coordinates, with some probability of crossover and mutation (we recommend 0.85 and 0.01) until some given number of iterations. The data will be provided through an input file.

# execution of genetic algorithm
__$ python Genetic.py n\_individuals n\_clusters p\_crossover p\_mutation iterations input\_file__

# particle swarm optimization
PSO is a search algorithm that is based on birds behavior. A particle will be part of a population, and using its best position so far (cognitive factor), the best position in its neighbourhood (social factor), and its 'disposition to move' (inertia), it will move on the solution space looking for the place of minimum error.

The implementation of the algorithm uses a maximum and a minimum value for inertia (we suggest from 0.9 and 0.5), and cognitive and social factors are suggested to be 1.50 each. The input file will hold the data.

# execution of particle swarm optimization
__$ python PSO.py n\_particles n\_clusters inertia\_max inertia_min fcognitive fsocial iterations input\_file__
