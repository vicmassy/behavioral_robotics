# Exercise 2
 - The robot with this simple algorithm manages to solve the problem always with a population size of 20, 100 episodes and 200 steps. 
 - By decreasing the population size, on average the solution is found later in the number of generations, as compared to a bigger number since the higher the number the more search space it is covered at the initialization step. However a bigger population size increases the execution time. 
 - By changing the number of hidden neurons seems to not affect the behavior of the robot (I tried up to having 2 neurons or even 10 neurons, the default is set to 5)
 - By increasing the the variance of the perturbation, the algorithm converges far more later than usual since every time the best chromosomes are copied, are modificated too much. On the other hand by decreasing the parameter there is no evolution at all since the modifications made to the "best" chromosomes are too small.
 - The smaller the number of steps the faster the problem is solved since it needs to hold the pendulum up for a shorter period of time.
 - The algorithm was tested also with the Pendulum-v0 environment. Not even modifying the parameters such as size of the population, it was able to solve the task in a relative short amount of time. 
