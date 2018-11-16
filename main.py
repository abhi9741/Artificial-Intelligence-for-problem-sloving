import  BFS
import DFS
import UCS
import DL_DFS
import ID_DFS
import BDS
import GREEDY
import ASTAR

import time
import os
from texttable import Texttable

# initialstate = [[1,2,3],[4,5,6],[7,0,8]] 
# goalstate = [[1,2,3],[4,5,6],[7,8,0]]


# initialstate = [[7,8,6],[0,1,2],[4,5,3]]

# initialstate = [[4,1,3],[0,2,5],[7,8,6]] 

# initialstate = [[2,5,3],[1,0,6],[4,7,8]]  

initialstate = [[1,4,5],[7,2,8],[6,0,3]]  

# initialstate = [[1,2,3],[7,8,0],[4,5,6]]
 
initialstate = [[1,3,0],[4,2,5],[7,8,6]]
# initialstate = [[4,1,2],[0,5,3],[7,8,6]] 
# initialstate = [[1,3,0],[4,2,5],[7,8,6]]  
# initialstate = [[0,1,2],[4,5,3],[7,8,6]] 
# initialstate = [[1,2,3],[4,0,5],[7,8,6]]
# initialstate = [[1,2,3],[0,4,5],[7,8,6]]

goalstate = [[1,2,3],[4,5,6],[7,8,0]]




print("initialstate : ")
BFS.printlist(initialstate)
print("goalstate : ")
BFS.printlist(goalstate)

with open("output.txt","w") as outfile :
	outfile.write("initial state : "+"\n")
BFS.writelist(initialstate,"output.txt")
with open("output.txt","a") as outfile :
	outfile.write("\n"+"\n")
# with open("output.txt","a") as outfile :
# 	outfile.write("\n"+"\n")
with open("output.txt","a") as outfile :
	outfile.write("\n"+"goal state : "+"\n")
BFS.writelist(goalstate,"output.txt")
with open("output.txt","a") as outfile :
	outfile.write("\n"+"\n")

# with open("output.txt","a") as outfile :
# 	outfile.write("\n"+"\n")


# def printlist(state) :
# 	# print("from print list function")
# 	# print(state)
# 	t=Texttable()
# 	t.add_rows([[state[0][0],state[0][1],state[0][2]],[state[1][0],state[1][1],state[1][2]],[state[2][0],state[2][1],state[2][2]]])
# 	print(t.draw())
# 	print("\n")
	
	# use tempoutput

t=Texttable()



#BFS search technique
start=time.clock()
info1 = BFS.BFSsearch(initialstate,goalstate)
info1 = list(info1)
time1=time.clock()-start
if info1[3] :
	info1[3] = "Exceeds 5 min"
else :
	info1[3] = time1

# with open("output.txt","a") as outfile :
# 	outfile.write("TimeTaken - "+str(time1)+"\n")



# #UCS search technique
start=time.clock()
info2=UCS.UCSsearch(initialstate,goalstate)
info2 = list(info2)
info2[3]
time1=time.clock()-start
if info2[3] :
	info2[3] = "Exceeds 5 min"
else :
	info2[3] = time1
# with open("output.txt","a") as outfile :
# 	outfile.write("TimeTaken - "+str(time1)+"\n"+"\n")

# #Depth Limit DFS search technique
# limit = int(input("enter depth limit for Depth Limit Depth First Search :"))
limit =10
start=time.clock()
info3=DL_DFS.DL_DFSsearch(initialstate,goalstate,limit)
info3 = list(info3)
info3[3]
time1=time.clock()-start
if info3[3] :
	info3[3] = "Exceeds 5 min"
else :
	info3[3] = time1
# with open("output.txt","a") as outfile :
# 	outfile.write("TimeTaken - "+str(time1)+"\n")

# #Iterative Deepening DFS search technique
start=time.clock()
info4=ID_DFS.ID_DFSsearch(initialstate,goalstate)
info4[3]
info4 = list(info4)
time1=time.clock()-start
if info4[3] :
	info4[3] = "Exceeds 5 min"
else :
	info4[3] = time1
# with open("output.txt","a") as outfile :
# 	outfile.write("TimeTaken - "+str(time1)+"\n")

# print("BDS search")

start=time.clock()
info5=BDS.BDSsearch(initialstate,goalstate)
info5[3]
info5 = list(info5)
time1=time.clock()-start
if info5[3] :
	info5[3] = "Exceeds 5 min"
else :
	info5[3] = time1
# with open("output.txt","a") as outfile :
# 	outfile.write("TimeTaken - "+str(time1)+"\n")

start=time.clock()
info6=GREEDY.GREEDYsearch(initialstate,goalstate)
info6[3]
info6 = list(info6)
time1=time.clock()-start
if info6[3] :
	info6[3] = "Exceeds 5 min"
else :
	info6[3] = time1
# with open("output.txt","a") as outfile :
# 	outfile.write("TimeTaken - "+str(time1)+"\n")

start=time.clock()
info7=ASTAR.ASTARsearch(initialstate,goalstate)
info7[3]
info7 = list(info7)
time1=time.clock()-start
if info7[3] :
	info7[3] = "Exceeds 5 min"
else :
	info7[3] = time1
# with open("output.txt","a") as outfile :
# 	outfile.write("TimeTaken - "+str(time1)+"\n")

# #DFS search technique
start=time.clock()
info8=DFS.DFSsearch(initialstate,goalstate)
info8[3]
info8 = list(info8)
time1=time.clock()-start
if info8[3] :
	info8[3] = "Exceeds 5 min"
else :
	info8[3] = time1
# with open("output.txt","a") as outfile :
# 	outfile.write("TimeTaken - "+str(time1)+"\n")

t.add_rows([["Search technique	","	Nodes Explored","		TimeTaken		"],[info1[0],info1[1],info1[3]],[info8[0],info8[1],info8[3]],[info2[0],info2[1],info2[3]],[info3[0],info3[1],info3[3]],[info4[0],info4[1],info4[3]],[info5[0],info5[1],info5[3]],[info6[0],info6[1],info6[3]],[info7[0],info7[1],info7[3]]])                                                   
with open("output.txt","a") as outfile :
	outfile.write(t.draw())
os.system("gedit output.txt")
