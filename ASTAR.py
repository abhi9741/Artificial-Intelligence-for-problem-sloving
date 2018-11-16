import copy
from texttable import Texttable
import time

def find_pos(state,num) :
	for list in state :
		if num in list :
			i=state.index(list)
			j=list.index(num)
	return i,j
def manhattan_distance(state1,goalstate) : 
	i=1
	m_dist=0
	while i<=8:
		i1,j1=find_pos(state1,i)
		i2,j2=find_pos(goalstate,i)
		# print(abs(i1-i2)+abs(j1-j2))
		m_dist=m_dist+abs(i1-i2)+abs(j1-j2)
		i=i+1
	print(m_dist)
	return m_dist
def printlist(state) :	
	t=Texttable()
	t.add_rows([[state[0][0],state[0][1],state[0][2]],[state[1][0],state[1][1],state[1][2]],[state[2][0],state[2][1],state[2][2]]])
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
def find_index(listl,elem) :
	i=listl.index(elem)
	try :
		elem1 = listl[i+1]
	except :
		return i
	if elem1 == elem :
		try :
			while elem1==elem :
				i=i+1
				elem1=listl[i]
			return i
		except :
			return i
	else :
		return i

def ASTARsearch(initialstate,goalstate):
	time1=time.clock()
	if initialstate == goalstate :
		print("*Initial State is the Goal State*")
		return	("ASTARsearch",0,"-",False)

	print("initial state : ")
	printlist(initialstate)
	print("goal state : ")
	printlist(goalstate)

	visited = []
	toVisit = []
	heuristic = []
	heights={0:0}

	print("neighbours : ")

	neighbours = find_neighbours(initialstate)
	for state in neighbours :
		m_dist=manhattan_distance(state,goalstate)
		heuristic.append(m_dist)
		heuristic.sort()
		i=find_index(heuristic,m_dist)
		print("find index : ",str(i))
		toVisit.insert(i,state)
		heights[str(state)]=1
		printlist(state)
	
	visited.append(initialstate)


	# print("to visit ")
	# print(toVisit)
	# print("heuristic ")
	# print(heuristic)

	currentState = toVisit[0]
	height = heights[str(currentState)]
	iteration = 1
	while len(toVisit)!=0 :

		if (time.clock()-time1 )>300 :
			# with open("output.txt",'a') as outfile :				
			# 	out2 ="\n" + "ASTAR Search Technique : "+"\n"+"nodes explored - " + str(iteration) +"\n"
			# 	outfile.write(out2)
			return ("ASTARsearch",str(iteration),"-",True)

		print("ASTAR search technique running .......")
		print("nodes explored : ",iteration)
		print("current state : "  )
		print("height : ",height)
		# time.sleep(.1)
		printlist(currentState)
		# printlist(currentState)
		# print("1")
		if currentState == goalstate :
			print("ASTAR search technique : ")
			print("Goal state reached ")
			time.sleep(1)
			# with open("output.txt",'r') as outfile :
			# 	out1=outfile.read()
			# with open("output.txt",'w') as outfile :
				
			# 	out2 =out1 +"\n" + "ASTAR Search Technique : "+"\n"+"nodes explored - " + str(iteration) +"\n"
			# 	outfile.write(out2)
			return ("ASTARsearch",str(iteration),"-",False)
		# print("2")
		if currentState in visited :
			# print("current state before deletion : ",currentState)
			visited.append(currentState)
			# del(heights[str(currentState)])
			del(heuristic[toVisit.index(currentState)])
			del(toVisit[toVisit.index(currentState)])
			
			currentState=toVisit[0]
			# print("current state after deletion : ",currentState)
			print("visited node already : ")
			continue
		# print("3")
		neighbours = find_neighbours(currentState)
		# print("4")
		visited.append(currentState)
		# print("4 1")
		# del(heights[str(currentState)])
		del(heuristic[toVisit.index(currentState)])
		del(toVisit[toVisit.index(currentState)])
		
		# print("4 2")
		currentState=toVisit[0]
		# print(currentState)
		# print(currentState)
		# print(heights)
		height = heights[str(currentState)]
		# print("5")
		# print("neighbours")
		print("neighbours : ")
		# for state in neighbours :
		# 	printlist(state)
		# 	toVisit.append(state)

		for state in neighbours :
			m_dist=manhattan_distance(state,goalstate)
			heuristic.append(m_dist+height+1)
			heuristic.sort()
			i=find_index(heuristic,m_dist+height+1)
			print("find index : ",str(i))
			toVisit.insert(i,state)
			print("height : ",height+1)
			heights[str(state)] = height+1
			printlist(state)
		# print("6")
		iteration=iteration+1
	# print(visited)

if __name__ == '__main__':
		initialstate = [[1,3,0],[4,2,5],[7,8,6]] 
		# initialstate = [[0,1,2],[4,5,3],[7,8,6]] 

		goalstate = [[1,2,3],[4,5,6],[7,8,0]]

		print("initialstate : ")
		printlist(initialstate)
		print("goalstate : ")
		printlist(goalstate)
		ASTARsearch(initialstate,goalstate)
		# manhattan_distance([[1,0,3],[4,2,5],[7,8,6]],goalstate)
		# l=[[[1, 2, 3], [4, 5, 0], [7, 8, 6]], [[1, 2, 3], [0, 4, 5], [7, 8, 6]], [[1, 0, 3], [4, 2, 5], [7, 8, 6]], [[1, 2, 3], [4, 8, 5], [7, 0, 6]]]
		# heuristic=[1, 3, 3, 3]
		# m_dist=manhattan_distance(initialstate,goalstate)
		# heuristic.append(m_dist)
		# heuristic.sort()
		# i=find_index(heuristic,m_dist)
		# l.insert(i,initialstate)
		# print(l)
		# print(heuristic)
		# l=[1,2,3,4,4,4,4,5,6]
		# i=find_index(l,4)
		# l.insert(i,7)
		# print(l)