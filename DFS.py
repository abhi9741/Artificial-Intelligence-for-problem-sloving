import copy
from texttable import Texttable
import time

def printlist(state) :
	t=Texttable()
	t.add_rows([[state[0][0],state[0][1],state[0][2]],[state[1][0],state[1][1],state[1][2]],[state[2][0],state[2][1],state[2][2]]])
	print(t.draw())
	print("\n")
def find_null(state) :
	s1=state[0]
	s2=state[1]
	s3=state[2]
	if 0 in s1 :
		i=0
		j=s1.index(0)
		pos=[i,j]
	if 0 in s2 :
		i=1
		j=s2.index(0)
		pos=[i,j]
	if 0 in s3 :
		i=2
		j=s3.index(0)
		pos=[i,j]
	return pos
def can_move_left(state) :
	pos=find_null(state)
	if pos[1]!=0 :
		return True
	else :
		return False
def can_move_right(state) :
	pos=find_null(state)
	if pos[1]!=2 :
		return True
	else :
		return False
def can_move_up(state) :
	pos=find_null(state)
	if pos[0]!=0 :
		return True
	else :
		return False
def can_move_down(state) :
	pos=find_null(state)
	if pos[0]!=2 :
		return True
	else :
		return False
def find_neighbours(state) :
	neighbours=[]
	pos=find_null(state)
	i=pos[0]
	j=pos[1]

	if can_move_down(state) :
		temp=state[i+1][j]
		down_state=copy.deepcopy(state)
		down_state[i+1][j]=state[i][j]
		down_state[i][j]=temp
		neighbours.append(down_state)
	if can_move_up(state) :
		temp=state[i-1][j]
		up_state=copy.deepcopy(state)
		up_state[i-1][j]=state[i][j]
		up_state[i][j]=temp
		neighbours.append(up_state)
		

	if can_move_right(state) :
		# print("has neighbours to its right")
		temp=state[i][j+1]
		right_state=copy.deepcopy(state)
		right_state[i][j+1]=state[i][j]
		right_state[i][j]=temp
		# print("right neighbour : ",right_state)
		neighbours.append(right_state)

	if can_move_left(state) :
		# print("has neighbours to its left")
		temp=state[i][j-1]
		left_state=copy.deepcopy(state)
		left_state[i][j-1]=state[i][j]
		left_state[i][j]=temp
		# print("left neighbour : ",left_state)
		neighbours.append(left_state)



	# print("State :")	
	# printlist(state)
	# print("neighbours : ")
	# for state in neighbours :
	# 	printlist(state)
	return(neighbours)

def DFSsearch(initialstate,goalstate):
	time1=time.clock()
	visited = []
	toVisit = []
	if initialstate == goalstate :
		print("*Initial State is the Goal State*")
		return ("Depth First Search",0,"-",False)
	neighbours = find_neighbours(initialstate)
	for state in neighbours :
		toVisit.append(state)
		state1 = copy.deepcopy(state)
		printlist(state1)	
	visited.append(initialstate)
	currentState = toVisit.pop()
	iteration = 1
	while len(toVisit)!=0 :

		if (time.clock()-time1 )>300 :
			# with open("output.txt",'a') as outfile :				
			# 	out2 ="\n" + "DFS Search Technique : "+"\n"+"nodes explored - " + str(iteration) +"\n" +"Terminated - exceeds more than 5 min" +"\n"
			# 	outfile.write(out2)
			return ("Depth First Search",str(iteration),"-",True)

		print("DFS search technique : ")
		print("nodes explored : ",iteration)
		print("current state : ")
		printlist(currentState)

		if currentState == goalstate :
			print("DFS search technique : ")
			print("Goal state reached ")
			time.sleep(1)
			# with open("output.txt",'r') as outfile :
			# 	out1=outfile.read()
			# with open("output.txt",'w') as outfile :
				
			# 	out2 =out1 +"\n" + "DFS Search Technique : "+"\n"+"nodes explored - " + str(iteration+1) +"\n"
			# 	outfile.write(out2)
			return ("Depth First Search",str(iteration),"-",False)
		if currentState in visited :
			currentState=toVisit.pop()
			continue
		neighbours = find_neighbours(currentState)
		visited.append(currentState)
		print("neighbours : ")
		for state in neighbours :
			toVisit.append(state)
			printlist(state)
		iteration=iteration+1
		currentState=toVisit.pop()

if __name__ == '__main__':
	initialstate = [[1,2,3],[0,4,5],[7,8,6]] 
	goalstate = [[1,2,3],[4,5,6],[7,8,0]]
	DFSsearch(initialstate,goalstate)