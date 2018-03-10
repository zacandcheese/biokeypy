import glob
import os
import json
import statistics
import string
import platform

def clearSummaries():
	print("In clear summaries")
	for file in glob.glob("Applying/Summary/*.txt"):
		print(file)
		os.remove(file)
	print("Done clear summaries\n")
def clearAll():
	print("In clear all")
	for file in glob.glob("Applying/*.txt"):
		os.remove(file)
	for file in glob.glob("Applying/Summary/*.txt"):
		os.remove(file)
	for file in glob.glob("Database/*.txt"):	
		os.remove(file)
	for file in glob.glob("Database/Summary/*.txt"):
		os.remove(file)
def makeTable(intDict, charDict, location, person):

	"""
	list of all tuples found in what the person typed
	# of appearances, median, variance
	"""
	totalSentence = ""
	for i in range(len(charDict)):
		totalSentence += charDict[str(i)]
		
	print(totalSentence)

	filename = location + person + ".txt"#GREEN computer
	
	listOfTuples = []
	#cycle all letters
	for i in ([""]+list(string.ascii_lowercase)):
		for j in ([""]+list(string.ascii_lowercase)):
			for k in (list(string.ascii_lowercase)):
				for l in (list(string.ascii_lowercase)):
					tuple = i+j+k+l
					
					if(tuple not in listOfTuples):
						
						if tuple in totalSentence.lower():
							allTimes = []
							for m in range(len(totalSentence)-len(tuple)):
								pTuple = ""
								for n in range(len(tuple)):
									pTuple += totalSentence[(m+n)].lower()
								if (pTuple == tuple):
									allTimes.append(intDict[str(m+len(tuple)-1)]-intDict[str(m)])
									
							#ADD IT TO FILE
							if len(allTimes)>=3:
								listOfTuples.append(tuple)
								print(tuple,len(allTimes),statistics.mean(allTimes),statistics.median(allTimes), statistics.variance(allTimes))
								dummyFile = open(filename, 'a')
								dummyFile.write(str(tuple)+","+str(len(allTimes))+","+str(statistics.mean(allTimes))+","+str(statistics.median(allTimes))+","+str(statistics.variance(allTimes))+"\n")
						#The entire sentence of what they wrote
						#list of every appearances, time for each
	

def userSummary(fileName, location):
	#clearSummaries()
	listOfTxtFiles = []
	for file in glob.glob(location+"/*.txt"):#CHANGE
		listOfTxtFiles.append(file)

	listOfTxtFiles = sorted(listOfTxtFiles, key=str.lower)
	print(listOfTxtFiles)
	
	newListOfTxtFiles = []
	for file in listOfTxtFiles:
		if(fileName in file):
			newListOfTxtFiles.append(file)
	
	numFiles = round(len(newListOfTxtFiles)/2)
	print(newListOfTxtFiles)
	for num in range(int(numFiles)):
		intDict = json.load(open(newListOfTxtFiles[num*2],'r'))
		charDict = json.load(open(newListOfTxtFiles[num*2+1],'r'))
		makeTable(intDict, charDict,(location+"/Summary/"), fileName)
		print("\n")
		
if __name__== '__main__':
	os.chdir("judgeslib/")
	userSummary("Test","Applying/")