import glob
import os
import statistics



"""CHECKS TO SEE IF EVERYONE USED IT"""
def isComplete(line):
	arr = []
	try:
		for i in range(len(line)-3):
			arr.append(float(line[2+i]))
	except ValueError:
		return False
	return True

def allPeople():

	listOfTxtFiles = []
	for file in glob.glob("lib/Database/Summary/*.txt"):
		listOfTxtFiles.append(file)
	tuples = newData(listOfTxtFiles)
	print("Done with getting combination")
	return(tuples)
"""START OF THE METHOD"""
def newData(list):
	#os.chdir("lib/Database")
	megaList = []
	for file in list:
		for line in open(file,"r").readlines():
			megaList.append(line)
    #HAVE EVERYBODIES DATA
	filename = "unique" + ".txt"#name
	if(not os.path.exists(filename)):#not
		tuplesSeen = []
	
		for line in megaList:
			tuple = line.split(",")[0]
			if tuple not in tuplesSeen:
				tuplesSeen.append(tuple)
				#GIVES ALL TUPLES
				tupleList = []
				#Check all people
				numList = []
				for name in list:
					i = 0
					flag = False
					for line2 in open(name,"r").readlines():
						i+= 1
						if(line2.split(",")[0] == tuple):
							flag = True
							tupleList.append(float(line2.split(",")[3]))#Median
							numList.append(int(line2.split(",")[1]))#NUM
						elif(i==(len(open(name,"r").readlines())-1) and not flag):
							tupleList.append(" ")
						
						#if(len(dummyList)>=3):
						#	tupleList.append(statistics.median(dummyList))
					
				if(len(tupleList)>=3):
					dummyFile = open(filename, 'a')
					pString = str(tuple)+", "+str(statistics.median(numList))+", "
					for person in tupleList:
						pString += str(person)+", "
					pString += "\n"
				
					dummyFile.write(pString)
					dummyFile.close()
		#FILE FOR EVERY TUPLE CALLED unique
	"""LOOKS AT EVERYONES DOCUMENTS TO FIND THE AVERAGE DISTANCE"""	
	
	list = []
	for tuple in open(filename,"r").readlines():
		arr = tuple.split(",")		
		if(isComplete(arr)):#CHANGE ME TO BE SO IT IS EVERYONE
			dict = {}
			numArr = []
			for i in range(len(arr)-3):
				numArr.append(float(arr[2+i]))
		
			mean = statistics.mean(numArr)
			sumOfDifferences = 0
			for i in (numArr):
				sumOfDifferences += abs(i-mean)
			dict["time"] = sumOfDifferences/len(numArr)
			dict["name"] = arr[0]
			list.append(dict)
	"""FINDS MAX AVG DIFF FROM ^^^"""	
	newlist = sorted(list, key=lambda k: k['time'], reverse = True)
	listTuple = []
	for i in range(10):
		#print("#", i+1, newlist[i]["name"], newlist[i]['time'], " " )
		listTuple.append(newlist[i]["name"])
	os.remove(filename)
	return(listTuple)

def getAvgTolerance(name):
	None
def personalCombos(name):
	print(name)
	list = []
	for file in glob.glob("lib/Database/Summary/*.txt"):
		list.append(file)
	print("List of People: ", list)#FIXME
	megaList = []
	compareList = []
	flag = True #print if name is not in list.
	for file in list:
		if(name in file):
			for line in open(file,"r").readlines():
				compareList.append(line)
			flag = False 
		else:
			for line in open(file,"r").readlines():
				megaList.append(line)
	if(flag):
		print("You are not in the system. Try again")
		return
	print("Finished making the megaList")
	
	#Check all the people for every single tuple in Zachary
	#if not all have it then return
	#rank the ones that are left by highest difference from the actual value.
	mainList = []
	for line in compareList:
		#All of my tuples
		compareToTuple = line.split(",")[0]
		flag = False #Flag when everyone doesn't have it
		numInstances = 0
		listOfDifferences = []
		for line2 in megaList:
			tuple = line2.split(",")[0]
			if(tuple == compareToTuple):
				numInstances += 1
				listOfDifferences.append(abs(float(line2.split(",")[3])-float(line.split(",")[3])))#One person minus the expected
		if(numInstances<len(list)-1):
			pass
		else:
			dict = {}
			dict['name'] = compareToTuple
			#dict['diff'] = statistics.median(listOfDifferences)
			dict['diff'] = min(listOfDifferences)
			mainList.append(dict)
	newlist = sorted(mainList, key=lambda k: k['diff'], reverse = True)
	returnList = []
	counter = 0
	for i in range(10):
		if (len(newlist[i]['name'])<3):
			pass
		elif(counter<3):
			counter += 1
			print(newlist[i]['name']+": ", newlist[i]['diff'])
			returnList.append(newlist[i]['name'])
	return returnList
			
	
"""
find the tuple for all .txt files
if there is multiple of each, then
compare each of the text files 
print the tuple and variance
"""
if __name__ == "__main__":
	#os.chdir("lib/Database")
	"""
	listOfTxtFiles = []
	for file in glob.glob("Summary/*.txt"):
		listOfTxtFiles.append(file)
	#print(listOfTxtFiles)
	what = []
	for i in range(len(listOfTxtFiles)-1):
		what.append(listOfTxtFiles[i+1])
	print(what)
	"""
	#os.chdir("lib/")
	personalCombos("Madeleine H")

