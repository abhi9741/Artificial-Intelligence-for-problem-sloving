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

	if can_move_down(state) :
		# print("has neighbours to its down")
		temp=state[i+1][j]
		down_state=copy.deepcopy(state)
		down_state[i+1][j]=state[i][j]
		down_state[i][j]=temp
		neighbours.append(down_state)
		# print("bottom neighbour : ",down_state)
	if can_move_up(state) :
		# print("has neighbours to its up")
		temp=state[i-1][j]
		up_state=copy.deepcopy(state)
		up_state[i-1][j]=state[i][j]
		up_state[i][j]=temp
		# print("top neighbour : ",up_state)
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

def DL_DFSsearch(initialstate,goalstate,depth_limit):
	time1=time.clock()
	visited = []
	toVisit = []
	toVisitHeight = []

	toVisitHeight.append(0)
	toVisit.append(0)
	#iteration 1

	if initialstate == goalstate :
		print("*Initial State is the Goal State*")
		return ("ID_DFSsearch",0,0,False,True)

	print("initial state")
	printlist(initialstate)
	neighbours = find_neighbours(initialstate)
	print("neighbours")


	for state in neighbours :
		toVisit.append(state)
		toVisitHeight.append(1)
		state1 = copy.deepcopy(state)
		printlist(state1)
		
	visited.append(initialstate)
	
	# print("to visit : ",toVisit)
	# print("visited : ",visited)
	currentState = toVisit.pop()
	height = toVisitHeight.pop()
	# print("currentState : ",currentState)
	# print("to visit : ",toVisit)
	iteration = 1
	limit=depth_limit
	
	while len(toVisit)!=0 :
		if (time.clock()-time1 )>300 :
			# with open("output.txt",'a') as outfile :				
			# 	out2 ="\n" + "ID_DFS Search Technique : "+"\n"+"goal state found at depth - "+str(height)+"\n"  +"nodes explored - " + str(iteration+1) +"\n"
			# 	outfile.write(out2)
			return  ("ID_DFSsearch",str(iteration),str(height),True,True)

		print("ID_DFS search technique : ")
		print("----------------current depth limit : --------------------",depth_limit)
		print("nodes explored : ",iteration)
		print("current height explored : ",height-1)
		print("current state : "  )
		# time.sleep(.1)
		printlist(currentState)
		# printlist(currentState)
		# print("1")
		if currentState == goalstate :
			print("ID_DFS search technique : ")
			print("Goal state reached ")
			time.sleep(1)
			# with open("output.txt",'r') as outfile :
			# 	out1=outfile.read()
			# with open("output.txt",'w') as outfile :
				
			# 	out2 =out1 +"\n" + "ID_DFS Search Technique : "+"\n"+"goal state found at depth - "+str(height)+"\n"  +"nodes explored - " + str(iteration+1) +"\n"
			# 	outfile.write(out2)
			return ("ID_DFSsearch",str(iteration),str(height),False,True)
		# print("2")
		if currentState in visited :
			# del(toVisit[toVisit.index(currentState)])
			# print("current state in visited block :",currentState)
			currentState=toVisit.pop()
			height = toVisitHeight.pop()
			# print("current state after popping",currentState)
			continue
		# print("3")
		# print("loop check height : ",height)
		# print("loop check limit : ",limit)
		if height<limit :
			# print("from inside the loop")
			neighbours = find_neighbours(currentState)
			print("neighbours : ")
			for state in neighbours :
				printlist(state)
				toVisit.append(state)
				toVisitHeight.append(height+1)

		# print("4")
		

		visited.append(currentState)

		# print("4 1")
		# del(toVisit[toVisit.index(currentState)])
		# print("4 2")
		
		# print("5")
		# print("neighbours")
		
		# print("6")
		iteration=iteration+1
		# print("to visit : ",toVisit)
		currentState=toVisit.pop()
		height=toVisitHeight.pop()
	# print(visited)
	if len(toVisit)==0:
		print("goal state doesnot exist at current depth limit ")
		return ("ID_DFSsearch",str(iteration),str(height),True,False)
def ID_DFSsearch(initialstate,goalstate):
	depth_limit = 1
	all_info = DL_DFSsearch(initialstate,goalstate,depth_limit)
	ini=all_info[4]
	print(ini)

	while not ini :
		depth_limit=depth_limit+1
		all_info = DL_DFSsearch(initialstate,goalstate,depth_limit)
		ini=all_info[4]

	name = all_info[0]
	nodes =all_info[1]
	height=all_info[2]
	flag1=all_info[3]

	return (name,nodes,height,flag1)

if __name__ == '__main__':
	# initialstate = [[4,1,2],[0,5,3],[7,8,0]] 
	# goalstate = [[1,2,3],[4,5,6],[7,8,0]]
	initialstate = [[4,1,2],[0,5,3],[7,8,6]] 
	goalstate = [[1,2,3],[4,5,6],[7,8,0]]
	depth_limit = 1
	ini = DL_DFSsearch(initialstate,goalstate,depth_limit)
	print(ini)
	while not ini :
		depth_limit=depth_limit+1
		ini = DL_DFSsearch(initialstate,goalstate,depth_limit)
	
	# if not ini :
	# 	print("depth limit 2 failed ")
	# 	while not ini :

	# 		depth_limit = depth_limit+1
	# 		print("----------------current depth limit : --------------------",depth_limit)
	# 		ini = DL_DFSsearch(initialstate,goalstate,depth_limit)
	# 		