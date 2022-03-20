# NP-algorithm-research
Research on NP problem, and algorithms implementation
# Topic: *Travelling salesman problem*
**Travelling salesman problem** is an optimization problem that consists in determining, given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?
## Complexity
The problem is NP-hard.
## Example
### Consider cities A, B, C, D and distances between them.<br/>
<img src="https://upload.wikimedia.org/wikipedia/commons/1/19/Tsp_instance.png?uselang=fr" alt="drawing" width="200"/><br/>
### Here we have a path that crosses all cities exactly once.
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Tsp_solution_debile.png/185px-Tsp_solution_debile.png" alt="drawing" width="200"/><br/>
### The optimal path
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Tsp_opt.png/186px-Tsp_opt.png" alt="drawing" width="200"/><br/>
## Algorithms
There are two main category of algorithms to solve the problem.<br/>
**Exact algorithms** these algorithms find the optimal solution but require more time if the problem is more complex.<br/>
**Heuristic algorithms**(Aka approximation) these algorithms find a solution fast butt they don't guarantee optimality.<br/>
## Applications
**Travelling salesman problem** has a lot of applications, motivated by some concrete problems, like school bus route.<br/> 
A classic application is in logistics(deliveries, post office etc..).<br/> 
It's also used in biology(genome sequencing for example).<br/>
