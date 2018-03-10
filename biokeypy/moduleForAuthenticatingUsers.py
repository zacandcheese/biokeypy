import glob
import os
import statistics
import json

def newData(listOfGoodTuples):

	listOfTxtFiles = []
	for file in glob.glob("Database/Summary/*.txt"):
		listOfTxtFiles.append(file)
	print(listOfTxtFiles)

	listOfApplyingFiles = []
	for file in glob.glob("Applying/Summary/*.txt"):
		listOfApplyingFiles.append(file)
	print(listOfApplyingFiles)

	#listOfGoodTuples = ["that","tch","tc","nig","ight","one","feat","ery","ca","atch","hat","be","then","very","king","ener"]
	
	similiarList = []
	applying, list = listOfApplyingFiles,listOfTxtFiles
	for file in list:
		similiarDict = {}#NEW
		num = []#NEW
		megaList = []
      
		for line in open(file,"r").readlines():
			megaList.append(line)
         
		tuplesSeen = []
      
		for line in megaList:
			tuple = line.split(",")[0]#tuple
			if tuple not in tuplesSeen:
				tuplesSeen.append(tuple)
				if tuple in listOfGoodTuples:
					dummyList = []
					tuple2 = line.split(",")[0]
					if(tuple == tuple2):
						dummyList.append(float(line.split(",")[3]))#MEDIAN
					for line2 in open(applying[0],"r").readlines():
						appTuple = line2.split(",")[0]
						if (appTuple == tuple):
							print(tuple + " " + file + ": " + str(dummyList[0]) + " APPLIER: " + str(line2.split(",")[3]))
							print("The difference is " + str(abs(dummyList[0]-float(line2.split(",")[3]))))
							if((abs(dummyList[0]-float(line2.split(",")[3])))<.05):#.1 is the threshold #CHANGED 2/26/2018
								num.append(abs(dummyList[0]-float(line2.split(",")[3])));
							else:
								num.append(0)#CHANGED 2/26/2018
		similiarDict["name"] = file
		similiarDict["number"] = num
		similiarList.append(similiarDict)
		print("\n")
	#Sorted
	allPeople = []
	retry = False #Retry
	for term in range(len(listOfGoodTuples)):
		
		newlist = sorted(similiarList, key=lambda k: k['number'][term], reverse = False)
		listOfGoodTuples.sort()
		listOfGoodTuples.sort(key = lambda s: len(s))
		print(listOfGoodTuples[term])
		
		counter = 0
		for i in range(len(newlist)):
			if(not newlist[i]["number"][term] == 0):#CHANGED 2/26/2018
				counter += 1
				print("#", counter, newlist[i]["name"], newlist[i]['number'][term], " " )
				if(counter == 1):
					allPeople.append(newlist[i]["name"])

		#RETRY
		if(len(allPeople) == len(listOfGoodTuples)):
			currentMax = 0
			currentName = ""
			for i in range(len(allPeople)):
				if((allPeople).count(allPeople[i])>currentMax):
					currentMax = allPeople.count(allPeople[i])
					currentName = allPeople[i]
			if currentMax >= 2:
				print("You are ", currentName)
			else:
				retry = True
		elif(term == len(listOfGoodTuples)):
			print("True")
			retry = True
	#if not __name__ == '__main__':	
	#os.close(listOfApplyingFiles[0])
	os.remove(listOfApplyingFiles[0])
	if(retry):
		print("RETRY!!!")
		import moduleForSavingTimelines as ST
		import moduleForRecordingWithGUI as GUI
		import moduleForCreatingPasswordSentence as PS
		import moduleForDeconstructingTimelines as DT
		import moduleForAuthenticatingUsers as AU
		import moduleForFindingTuples as FT
		import moduleForGettingSentence as GS

		#More specific combinations
		location = "Applying/"
		data = FT.newData(allPeople)
		print(data)
		passage = GS.getSentence(data).split(".")
		pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine = GUI.start_recording(passage)
		ST.saveTimeLine(pressTimeLine,pressCharTimeLine,"RETRY",location)
		DT.userSummary("RETRY",location)
		AU.newData(data)
		os.remove('Applying/Summary\\RETRY.txt')
		

def verify(listOfGoodTuples, name):

	listOfTxtFiles = []
	for file in glob.glob("Database/Summary/*.txt"):
		listOfTxtFiles.append(file)
	print(listOfTxtFiles)

	listOfApplyingFiles = []
	for file in glob.glob("Applying/Summary/*.txt"):
		listOfApplyingFiles.append(file)
	print(listOfApplyingFiles)
	
	similiarList = []
	applying, list = listOfApplyingFiles,listOfTxtFiles
	for file in list:
		similiarDict = {}#NEW
		num = []#NEW
		megaList = []
      
		for line in open(file,"r").readlines():
			megaList.append(line)
         
		tuplesSeen = []
      
		for line in megaList:
			tuple = line.split(",")[0]#tuple
			if tuple not in tuplesSeen:
				tuplesSeen.append(tuple)
				if tuple in listOfGoodTuples:
					dummyList = []
					tuple2 = line.split(",")[0]
					if(tuple == tuple2):
						dummyList.append(float(line.split(",")[3]))#MEDIAN
					for line2 in open(applying[0],"r").readlines():
						appTuple = line2.split(",")[0]
						if (appTuple == tuple):
							print(tuple + " " + file + ": " + str(dummyList[0]) + " APPLIER: " + str(line2.split(",")[3]))
							print("The difference is " + str(abs(dummyList[0]-float(line2.split(",")[3]))))
							if((abs(dummyList[0]-float(line2.split(",")[3])))<1):#.1 is the threshold #CHANGED 2/26/2018
								num.append(abs(dummyList[0]-float(line2.split(",")[3])));
							else:
								num.append(0)#CHANGED 2/26/2018
		num = sum(num)
		similiarDict["name"] = file
		similiarDict["number"] = num
		similiarList.append(similiarDict)
		print("\n")
	#Sorted
	allPeople = []
	retry = False #Retry
	newlist = sorted(similiarList, key=lambda k: k['number'], reverse = False)
	print(newlist)
	for i in newlist:
		print(i['name'], ":", i['number'])
			
	if not __name__ == '__main__':	
		os.remove(listOfApplyingFiles[0])
	print("")	
	num = len(newlist)
	for i in range(num):
		if (num > 1):
			if(name in newlist[i]['name']):
				if (newlist[i]['number']<.2):
					print("You are the person")
				else:
					print("You are not the person")
		else:
			if (newlist[i]['number']<.2):
				print("You are " + newlist[i]['name'].split('\\')[-1][:-4])
			elif (newlist[i]['number']>.2 and newlist[i]['number']<.3):
				print("You may be " + newlist[i]['name'].split('\\')[-1][:-4])
			else:
				print("You are not "+ newlist[i]['name'].split('\\')[-1][:-4])
"""
find the tuple for all .txt files
if there is multiple of each, then
compare each of the text files 
print the tuple and variance
"""
if __name__ == '__main__':
	
	import moduleForDeconstructingTimelines as DT
	import moduleForFindingTuples as FT
	
	os.chdir("judgeslib/")
	name = "Test"
	DT.userSummary(name,"Applying/")
	#list = FT.personalCombos(name)
	list = ["his","the","ing"]
	print("This is the list: ",list,"\n")
	verify(list, name)
	DT.clearSummaries()