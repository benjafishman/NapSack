###############################
#quaraNapSack
#Ben Fishman
#7/7/2014
###############################
# Takes STDIN of value,weight pairs and outputs the optimal subset of pairs
# constrained by a given value
###############################

import fileinput

count = 1
Items = [[0,0,0]]
N = 0
W = 0
MAX_HEIGHT = 0 
DP = []
bag = []
sack_score = 0;

def napSack():
	print("IN NAPSACK")
	for i in range(1,count):
		for w in range(1,MAX_HEIGHT+1):
			i_height = Items[i][1]

			i_score = Items[i][2]

			val1 = DP[i-1][w]
			if(w - i_height >= 0):
				val2 = DP[i - 1][w - i_height] + i_score
				DP[i][w] = max(val1,val2)
			else:
				DP[i][w] = val1

def get_bag():
	i = len(Items)-1
	w = MAX_HEIGHT
	while(i > 0 and w > 0):
		print(i,w)
		if(DP[i][w] != DP[i-1][w]):
			bag.append(i)
			i = i - 1
			w = w - Items[i][1]
		else:
			i = i - 1

for line in fileinput.input():

	data = line.split(" ")

	if(data[0] != 'R' and data[0] != 'S'):
		N = int(data[0])
		W = int(data[1])
		MAX_HEIGHT = int(data[2])
		DP = [[0 for x in range(MAX_HEIGHT+1)] for x in range(len(Items))]

	if(data[0] == "S"):
		#get all elements in data except first
		#put in Items list
		itm = [int(i) for i in data[1:]]
		Items.append(itm)
		DP.append([0 for x in range(MAX_HEIGHT+1)])
		count = count+1
		napSack()


print("DISPLAYING OPTIMAL SET:")		
get_bag()
	
print(bag)









