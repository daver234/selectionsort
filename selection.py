import random
import time

start_time = time.time()

def randomlist(amount):
	list3 = []
	for i in range(0,amount):
		new = random.randint(0,10000)
		list3.append(new)
	selectionsort(list3)
	


def selectionsort(list):
	#print(list)
	for num in range (len(list)-1,0,-1):
		pmax = 0
		for i in range(1, num+1):
			#print "print i", i, "printing pmax", pmax
			if list[i] > list[pmax]:
				pmax = i		
		temp = list[num]
		list[num] = list[pmax]
		list[pmax] = temp
	print(list)			

list =[3,1,5,6,9,7]
selectionsort(list)


randomlist(100)

print "I am done"
print("--- %s seconds ---" % (time.time() - start_time))