import copy
from texttable import Texttable
import time

def printlist(state) :
	# print("from print list function")
	# print(state)
	t=Texttable()
	t.add_rows([[state[0][0],state[0][1],state[0][2]],[state[1][0],state[1][1],state[1][2]],[state[2][0],state[2][1],state[2][2]]])
	print(t.draw())
	print("\n")
def writelist(state,outputfile) :
	# print("from print list function")
	# print(state)
	t=Texttable()
	t.add_rows([[state[0][0],state[0][1],state[0][2]],[state[1][0],state[1][1],state[1][2]],[state[2][0],state[2][1],state[2][2]]])
	with open(outputfile,'a') as outfile :
		outfile.write(t.draw())
	print(t.draw())
	print("\n")
def find_null(state) :
	# print("find null")
	# print(state)
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
	# print("current state",state)
	neighbours=[]
	pos=find_null(state)
	i=pos[0]
	j=pos[1]
	if can_move_left(state) :
		# print("has neighbours to its left")
		temp=state[i][j-1]
		left_state=copy.deepcopy(state)
		left_state[i][j-1]=state[i][j]
		left_state[i][j]=temp
		# print("left neighbour : ",left_state)
		neighbours.append(left_state)

	if can_move_right(state) :
		# print("has neighbours to its right")
		temp=state[i][j+1]
		right_state=copy.deepcopy(state)
		right_state[i][j+1]=state[i][j]
		right_state[i][j]=temp
		# print("right neighbour : ",right_state)
		neighbours.append(right_state)

	if can_move_up(state) :
		# print("has neighbours to its up")
		temp=state[i-1][j]
		up_state=copy.deepcopy(state)
		up_state[i-1][j]=state[i][j]
		up_state[i][j]=temp
		# print("top neighbour : ",up_state)
		neighbours.append(up_state)
	if can_move_down(state) :
		# print("has neighbours to its down")
		temp=state[i+1][j]
		down_state=copy.deepcopy(state)
		down_state[i+1][j]=state[i][j]
		down_state[i][j]=temp
		# print("bottom neighbour : ",down_state)
		neighbours.append(down_state)

	# print("State :")	
	# printlist(state)
	# print("neighbours : ")
	# for state in neighbours :
	# 	printlist(state)
	return(neighbours)
#testing functions
state =[[1,2,3],[4,5,6],[7,8,0]]
state1 =[[1,0,3],[4,5,6],[7,8,1]]
state2 =[[0,2,3],[4,5,6],[7,8,1]]

# print("position of null (state): ",find_null(state))
# print("position of null (state 1): ",find_null(state1))
# print("position of null (state 2): ",find_null(state2))
# print("can move left (state): ",can_move_left(state))
# print("can move left (state 1): ",can_move_left(state1))
# print("can move left (state 2) : ",can_move_left(state2))
# print("can move right (state): ",can_move_right(state))
# print("can move right (state 1): ",can_move_right(state1))
# print("can move right (state 2) : ",can_move_right(state2))
# print("can move down (state): ",can_move_down(state))
# print("can move down (state 1): ",can_move_down(state1))
# print("can move down (state 2) : ",can_move_down(state2))
# print("can move up (state): ",can_move_up(state))
# print("can move up (state 1): ",can_move_up(state1))
# print("can move up (state 2) : ",can_move_up(state2))

# print("state")
# find_neighbours(state)
# print("state1")
# find_neighbours(state1)
# print("state2")
# find_neighbours(state2)

# initialstate = [[0,1,2],[4,5,3],[7,8,6]]
# initialstate = [[1,2,3],[7,8,0],[4,5,6]]
# initialstate = [[1,2,3],[4,0,5],[7,8,6]] 
# goalstate = [[1,2,3],[4,5,6],[7,8,0]]
# print("initialstate : ")
# printlist(initialstate)
# print("goalstate : ")
# printlist(goalstate)

def BFSsearch(initialstate,goalstate):
	time1=time.clock()
	visited = []
	toVisit = []
	#iteration 1

	if initialstate == goalstate :
		print("*Initial State is the Goal State*")

		return("Breadth First Search","0","-",False)
	print("initial state")
	printlist(initialstate)
	neighbours = find_neighbours(initialstate)
	# print("neighbours")
	for state in neighbours :
		toVisit.append(state)
		state1 = copy.deepcopy(state)
		# printlist(state1)
		
	visited.append(initialstate)
	# print(visited)
	# print(toVisit)

	currentState = toVisit[0]
	iteration = 1
	while len(toVisit)!=0 :
		if (time.clock()-time1 )>300 :
			# with open("output.txt",'a') as outfile :				
			# 	out2 ="\n" + "BFS Search Technique : "+"\n"+"nodes explored - " + str(iteration) +"\n" +"Terminated - exceeds more than 5 min" +"\n"
			# 	outfile.write(out2)
			return ("Breadth First Search",str(iteration,"-"),True)
		print("BFS search technique running .......")
		print("nodes explored : ",iteration)
		print("current state : "  )
		# time.sleep(.1)
		printlist(currentState)
		# printlist(currentState)
		# print("1")
		if currentState == goalstate :
			print("BFS search technique : ")
			print("Goal state reached ")
			time.sleep(1)
			# with open("output.txt",'r') as outfile :
			# 	out1=outfile.read()
			# with open("output.txt",'w') as outfile :
				
			# 	out2 =out1 +"\n" + "BFS Search Technique : "+"\n"+"nodes explored - " + str(iteration) +"\n"
			# 	outfile.write(out2)
			return ("Breadth First Search",str(iteration),"-",False)
		# print("2")
		if currentState in visited :
			del(toVisit[toVisit.index(currentState)])
			currentState=toVisit[0]
			continue
		# print("3")
		neighbours = find_neighbours(currentState)
		# print("4")
		visited.append(currentState)
		# print("4 1")
		del(toVisit[toVisit.index(currentState)])
		# print("4 2")
		currentState=toVisit[0]
		# print("5")
		# print("neighbours")
		print("neighboours : ")
		for state in neighbours :
			printlist(state)
			toVisit.append(state)
		# print("6")
		iteration=iteration+1
	# print(visited)

if __name__ == '__main__':
		initialstate = [[1,2,3],[4,0,5],[7,8,6]] 
		initialstate = [[1,3,0],[4,2,5],[7,8,6]]
		goalstate = [[1,2,3],[4,5,6],[7,8,0]]
		print("initialstate : ")
		printlist(initialstate)
		print("goalstate : ")
		printlist(goalstate)
		BFSsearch(initialstate,goalstate)