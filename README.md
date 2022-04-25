# NP-algorithm-research
Research on NP problem, and algorithms implementation
# Topic: *Travelling salesman problem*
**Travelling salesman problem** is an optimization problem that consists in determining, given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city.
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
- **Exact algorithms** these algorithms find the optimal solution but require more time if the problem is more complex.<br/>
- **Heuristic algorithms**(Aka approximation) these algorithms find a solution fast butt they don't guarantee optimality.<br/>
### Brute-force (Exact algorithms)
Generating all possible routes and take the cheapest using brute-force search.<br/>
This solution's running time is O(n!), where <strong>n</strong> represents the number of cities.<br/>
This solution becomes unfeasible for even 20 cities.<br/>
If a computing a path takes 10<sup>-6</sup> second, for 25 cities the running time exceeds the age of universe(14 billion years).<br/>

#### Execution time graph for brute force solution
<img src="https://raw.githubusercontent.com/teyalite/NP-algorithm-research/main/images/brute-force-graph.png" alt="drawing"/><br/>

### Dynamic programming solution
The algorithm used here is <strong>Held-Karp algorithm</strong>.<br/>
Dynamic programming reduces the time complexity from super exponential time to exponential time O(n<sup>2</sup>2<sup>n</sup>).<br/>

#### Execution time graph for dynamic programming solution
<img src="https://raw.githubusercontent.com/teyalite/NP-algorithm-research/main/images/dynamic-programming.png" alt="drawing"/><br/>

#### Solution of the previous example drawing using networkx and the brute force implementation
<img src="https://raw.githubusercontent.com/teyalite/NP-algorithm-research/main/images/favorite-example.png" alt="drawing"/><br/>
## Applications
**Travelling salesman problem** has a lot of applications, motivated by some concrete problems, like school bus route.<br/> 
A classic application is in logistics(deliveries, post office etc..).<br/> 
It's also used in biology(genome sequencing for example).<br/>

[//]: # (# [Solutions implementations on Colab google]&#40;https://colab.research.google.com/drive/1Hh2Ug0jHpwvuJbXVs4iDskGIWhfzmVjH#scrollTo=XM2HSF7jhYeE&#41;)
