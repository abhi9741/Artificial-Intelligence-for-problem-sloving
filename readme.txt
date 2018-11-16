*please enlarge the video if the tables are not visible properly*

Problem Statement :

Tiles are numbered, 1 through 8 for the 8-puzzle and an empty tile (for programming we consider this as tile numbered 0), so that each tile can be uniquely identified. The aim of the puzzle is to achieve a given configuration of tiles from a given (different) configuration by sliding the individual tiles around the grid. The possible moves are 
1)moving the tile numbered 0 to its left
2)moving the tile numbered 0 to its right
3)moving the tile numbered 0 up
4)moving the tile numbered 0  down

for example - 

initial state : 
+---+---+---+
| 1 | 0 | 2 |
+===+===+===+
| 4 | 5 | 3 |
+---+---+---+
| 7 | 8 | 6 |
+---+---+---+

goal state : 
+---+---+---+
| 1 | 2 | 3 |
+===+===+===+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 0 |
+---+---+---+

by moving tile numbered 0 in initial state in the following way up>up>left goal state can be attained

for executing the algorithms please  run the main.py file.If you wish to change any parameters (initial state ,goal state ,depth limit for depth limit search) you can change them in this file itself.Each algorithm will terminate if it runs for more than 300 seconds (5 minutes)

For finding the path /moves we search through the state space using different algorithms.we construct a tree where each node denotes a state and its children denote the possible states that can be generated from current node by moving the tile numbered 0.We traverse/search this tree in different ways in different algorithms.

UNINFORMED SEARCH TECHNIQUES 

In these techniques the algorithm has no idea how far the goal state is from current node i.e, they do not know the direction of goal state hence do not know the best direction to search for.

Breadth First Search :

file containing this algorithm - BFS.py
we search the nodes based on first in first out queue , i.e, we explore all the nodes at current depth and then move on to the nodes at next depth.It may be faster than DFS but it is not memory efficeint.

Depth First search :

file containing this algorithm - DFS.py
we search the nodes based on last in first out queue (stack),i.e, we explore the nodes starting from root to leaf with out considering their siblings.we explore root then its first children (namely child 1) then children of child 1 and so on .(example we go left left left until there is no left  possible).Its time complexity is very bad but is memory efficient.

Uniform Cost Search :

file containing this agorithm - UCS.py
Uniform Cost Search is the best algorithm for a search problem in uninformed search algorithms.Uniform Cost Search as it sounds searches branches which are more or less the same in cost i.e, it explores based on the ascending order of costs but since in this particular problem the cost for each move is same hence ucs behaves like bfs. Uniform Cost Search again demands the use of a priority queu

Depth Limit Depth First Search :

file containing this algorithm - DL_DFS.py
In this algorithm we give a limit for the depth limit search.It follows the same procedure but instead of going from root to leaf it goes from root to node at the depth given in the same fashion of how a normal dfs algorithm would explore.

Iterative Deepining Depth First Search :

file containing  this algorithm - ID_DFS.py
In this algorithm we increase the limit of depth limit search from 1 to until we find the solution or search the  entire state space.This algorithm has advantages of both DFS and BFS. Its time complexity is significantly small compared to DFS (even BFS has small time complexity) and at the same time it has  linear memory/space  complexity.

Informed Searches :

GREEDY Search :

file containing this algorithm - GREEDY.py
In this algorithm we explore nodes based on the increasing order of g(n) where g(n) is the distance/cost of neeighbouring nodes.The assumption is that if we select optimum in each step locally we get an global optimum solution.

ASTAR Search :

file containing this algorithm - ASTAR.py
In this algorithm we explore nodes based on the increasing order of f(n)+h(n) where h(n) is the heuristic (the distance from current state to goal state) and f(n) is the cost for reaching that sttate from initial state (which is equivalent to depth of that node in our case).

