#moduleForPlotting
#https://matplotlib.org/users/pyplot_tutorial.html

import matplotlib.pyplot as plt
import numpy as np
import glob
import moduleForDeconstructingTimelines as DT


def plot(listOfGoodTuples):

	listOfTxtFiles = []
	for file in glob.glob("Database/Summary/*.txt"):
		listOfTxtFiles.append(file)
	print(listOfTxtFiles)

	listOfApplyingFiles = []
	for file in glob.glob("Applying/*.txt"):
		listOfWords = file.split("\\")
		file2 = listOfWords[1][:-5]
		DT.userSummary(file2, "Applying/")
		
	for sumFile in glob.glob("Applying/Summary/*.txt"):
		listOfApplyingFiles.append(sumFile)
		
	print(listOfApplyingFiles)
	
	similiarList = []
	list = listOfApplyingFiles + listOfTxtFiles
	numList = [1,2,3]
	applierlist = [0,0,0]
	applierlist2 = [0,0,0]
	applierlistN = [0,0,0]
	passwordlist = [0,0,0]
	
	lineList = []
	for line in open(list[-1],"r").readlines():
		
		tuple = line.split(",")[0]#tuple
		if tuple in listOfGoodTuples:
			print(tuple, line.split(",")[3])
			passwordlist[listOfGoodTuples.index(tuple)] = float(line.split(",")[3])
	fileName = list[-1].split("\\")[-1][:-4]
	line1, = plt.plot(numList, passwordlist, label = fileName, linestyle='-', linewidth = 4)
	lineList.append(line1)
	i = 0
	for file in listOfApplyingFiles:
		fileName = file.split("\\")[-1][:-4]
		if(True):
			for line in open(file,"r").readlines():
				tuple = line.split(",")[0]#tuple
				if tuple in listOfGoodTuples:
					#print(tuple, line.split(",")[3])
					applierlistN[listOfGoodTuples.index(tuple)] = float(line.split(",")[3])
			line2, = plt.plot(numList, applierlistN, label = fileName, linestyle='--')
			lineList.append(line2)

		i+=1
	plt.xlabel('letter combination (int)')
	plt.ylabel('time (s)')
	plt.title('Difference Between Trials')
	plt.grid(True)
	#plt.plot(numList, passwordlist, 'r--', numList, applierlist, 'b--', numList, applierlist2, 'g--')
	plt.legend(handles=lineList, loc=4)
	#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.1)
	plt.show()			
	DT.clearSummaries()	
	
if __name__ == '__main__':
	import os
	os.chdir("judgeslib")
	plot(["his", "the","ing"])