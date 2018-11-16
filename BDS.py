#BiDirectionalSearch
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

def BDSsearch(initialstate,goalstate):

	time1=time.clock()
	visited_front = []
	toVisit_front = []
	visited_back = []
	toVisit_back = []
	#iteration 1

	if initialstate == goalstate :
		print("*Initial State is the Goal State*")
		return ("BiDirectional Search",0,"-",False)

	print("initial state")
	printlist(initialstate)
	neighbours = find_neighbours(initialstate)
	print("neighbours")
	for state in neighbours :
		toVisit_front.append(state)
		state1 = copy.deepcopy(state)
		printlist(state1)
		
	visited_front.append(initialstate)
	# print(visited)
	# print(toVisit)

	print("goal state")
	printlist(goalstate)
	neighbours = find_neighbours(goalstate)
	print("neighbours")
	for state in neighbours :
		toVisit_back.append(state)
		state1 = copy.deepcopy(state)
		printlist(state1)
		
	visited_back.append(initialstate)

	for state in neighbours :
		if (state in visited_front) or (state in toVisit_front) :
			nodes_explored = len(visited_front)+len(visited_back)
			print("BiDirectional BFS search technique-goal state reached"+"\n"+"nodes explored - ",nodes_explored)
			return ("BiDirectional Search",2,"-",False)

	front_current_state = toVisit_front[0]
	back_current_state = toVisit_back[0]

	while len(toVisit_front)!=0 or len(toVisit_back)!=0 :

		if (time.clock()-time1 )>300 :
			# with open("output.txt",'a') as outfile :				
			# 	out2 ="\n" + "BiDirectional BFS Search Technique : "+"\n"+"nodes explored - " + str(len(visited_front)+len(visited_back)+1) +"\n"
			# 	outfile.write(out2)
			return ("BiDirectional Search",str(len(visited_front)+len(visited_back)),"-",True)

		print("BiDirectional BFS search technique running ......")
		print("nodes explored - ",str(len(visited_front)+len(visited_back)))
		print("current front state : ")
		printlist(front_current_state)
		# print(toVisit_front)
		# print("___________")
		if front_current_state == goalstate :
			print("BiDirectional BFS search technique :")
			print("goalstate reached ")	
			time.sleep(1)
			# with open("output.txt",'r') as outfile :
			# 	out1=outfile.read()
			# with open("output.txt",'w') as outfile :
				
			# 	out2 =out1 +"\n" + "BiDirectional BFS Search Technique : "+"\n"+"nodes explored - " + str(len(visited_front)+len(visited_back)+1) +"\n"
			# 	outfile.write(out2)
			return ("BiDirectional Search",str(len(visited_front)+len(visited_back)),"-",False)

		if front_current_state in visited_front :
			# print(toVisit_front[0])
			print("entering if block")
			del(toVisit_front[toVisit_front.index(front_current_state)])
			front_current_state=toVisit_front[0]

		else :
			neighbours_front = find_neighbours(front_current_state)
			visited_front.append(front_current_state)
			del(toVisit_front[toVisit_front.index(front_current_state)])
			# print("toVisit_front 0")
			# print(toVisit_front)
			front_current_state=toVisit_front[0]

			# print("front_current_state :",front_current_state)
			# print("to visit front 1")
			# print(toVisit_front)
			print("neighboours front : ")
			for state in neighbours_front :
				printlist(state)
				if state not in visited_front :
					toVisit_front.append(state)
					# print("toVisit_front 2")
					# print(toVisit_front)
					if state in visited_back or state in toVisit_back :
						print("goalstate reached  ")
						printlist(state)
						print("nodes_explored - ",str(len(visited_front)+len(visited_back)))
						# with open("output.txt",'a') as outfile :
							
						# 	out2 ="\n" + "BiDirectional BFS Search Technique : "+"\n"+"nodes explored - " + str(len(visited_front)+len(visited_back)+1) +"\n"
						# 	outfile.write(out2)
						return	("BiDirectional Search",str(len(visited_front)+len(visited_back)),"-",False)					
						

		print("current back state :")
		printlist(back_current_state)

		if back_current_state == goalstate :
			print("BiDirectional BFS search technique :")
			print("goalstate reached ")	
			time.sleep(1)
			# with open("output.txt",'r') as outfile :
			# 	out1=outfile.read()
			# with open("output.txt",'w') as outfile :
				
			# 	out2 =out1 +"\n" + "BiDirectional BFS Search Technique : "+"\n"+"nodes explored - " + str(len(visited_front)+len(visited_back)+1) +"\n"
			# 	outfile.write(out2)
			return ("BiDirectional Search",str(len(visited_front)+len(visited_back)),"-",False)
		if back_current_state in visited_back :
			del(toVisit_back[toVisit_back.index(back_current_state)])
			back_current_state=toVisit_back[0]

		else :
			neighbours_back = find_neighbours(back_current_state)
			visited_back.append(back_current_state)
			del(toVisit_back[toVisit_back.index(back_current_state)])
			back_current_state=toVisit_back[0]
			print("neighboours back : ")
			for state in neighbours_back :
				printlist(state)
				if state not in visited_back :
					toVisit_back.append(state)
					if state in visited_front or state in toVisit_front :
						print("goalstate reached  :")
						printlist(state)
						print("nodes_explored - ",str(len(visited_front)+len(visited_back)))
						# with open("output.txt",'a') as outfile :
							
						# 	out2 ="\n" + "BiDirectional BFS Search Technique : "+"\n"+"nodes explored - " + str(len(visited_front)+len(visited_back)) +"\n"
						# 	outfile.write(out2)
						return	 ("BiDirectional Search",str(len(visited_front)+len(visited_back)),"-",False)						
						


if __name__ == '__main__':
		initialstate = [[0,1,3],[7,2,6],[4,8,5]] 
		goalstate = [[1,2,3],[4,5,6],[7,8,0]]
		# print("initialstate : ")
		# printlist(initialstate)
		# print("goalstate : ")
		# printlist(goalstate)
		BDSsearch(initialstate,goalstate)