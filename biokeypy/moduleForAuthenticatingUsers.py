"""
Author:
Date:

Program description:

"""
"""STANDARD LIBRARY IMPORTS"""
import glob
import os
import statistics
import json

def newData(listOfGoodTuples):
	#os.chdir("lib/")

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
		num = 0#NEW
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
							if((abs(dummyList[0]-float(line2.split(",")[3])))<.1):#.01 is the threshold
								num += 1;
		similiarDict["name"] = file
		similiarDict["number"] = num
		similiarList.append(similiarDict)
		print("\n")
	#Sorted
	newlist = sorted(similiarList, key=lambda k: k['number'], reverse = True)
	for i in [0,1,2,3]:
		print("#", i+1, newlist[i]["name"], newlist[i]['number'], " " )
		
	os.remove(listOfApplyingFiles[0])

"""
find the tuple for all .txt files
if there is multiple of each, then
compare each of the text files 
print the tuple and variance
"""