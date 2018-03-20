def getSentence(tupleList):
	import nltk
	import random
	bigList = []
	list = nltk.corpus.gutenberg.fileids()
	try:
		list.remove("bible-kjv.txt")#Removes the Bible text
	except:
		pass
	sentence = ""
	count = 0;
	for tuple in tupleList:
		for name in list:	
			file = nltk.corpus.gutenberg.sents(name)
		
			oldLine = ""
			olderLine = ""
			for newLine in file:
				#line = cat jumps do
				tempLine = ""
				for i in newLine:
					exceptionList = [".",";",",",":"]
					if(i in exceptionList):
						tempLine += i
					elif(i == "'"):
						tempLine += "'"
					elif(i == "-"):
						tempLine += ""
					else:
						tempLine += (" "+i)
				newLine = tempLine
				line = olderLine + oldLine + newLine
				count = 0
			
				if tuple in line.lower():
					string = line.lower()
					substring = tuple
				
					if(string.count(substring)>3 and len(string)<500):#30wpm * 5char/1word *3 min
						bigList.append(line)
				olderLine = oldLine
				oldLine = newLine
			
      
		if(len(bigList) > 0):
			sentence += random.choice(bigList).lower()
			bigList = []
			count+=1
		if(count > 3):
			break
		#print(name)  
	#print("\n")
	
	print ("Done with passage making")
	print(sentence)
	return(sentence)
	
def manuel(name):
	import moduleForFindingTuples as FT
	"""
	if name in "Zachary Nowak":
		#ered:  0.032782316207830065
		#rden:  0.030201792717398424
		#arde:  0.028679966926574707
		return("The very blind man reached over his very leathery bath to grab a feather. "+
			   "He wanted to record the weather. "+
			   "However he took his last breath, which lead to death.")
		
		return("The triggered, hardened gardener worked in his garden. "+
			   "The mad warden put this pampered burden on the gardener. "
			   "The gardener worked hard regardless at gardening. "+
			   "He ordered a layered, towered cake.")
	if name in "Zachary M":
		#very:  0.05450201034500002
		#gard:  0.052145957945999966
		#rden:  0.04934477806093851
		return("The very hardened gardener worked in his garden. "+
			   "The very mad warden put this burden on the gardener. "
			   "The work was like slavery but, he made a discovery and learned everything. ")
	if name in "David Grinstead2":
		#ery:  0.23817110061700003
		#very:  0.20316743851000008
		#ene:  0.09084820747328176
		return("Every man everywhere created energy."+
			   "The genes in everybody were omened to regenerate everyday. " +
			   "The discovery by the delivery man was opened by the opener. ")
		
		return("The triggered, hardened gardener worked in his garden. "+
			   "The mad warden put this pampered burden on the gardener. "
			   "The gardener worked hard regardless at gardening. "+
			   "He ordered a layered, towered cake.")
		
	if name in "Ethan Saari":
		#gard:  0.24579930305510012
		#arde:  0.2061315774922139
		#rde:  0.18516099452972412
		return("The very hardened gardener worked in his garden. "+
			   "The very mad warden put this burden on the gardener. "
			   "The gardener worked hard regardless at gardening")
	if name in "Matthew Nowak":
		#but:  0.06161534786299999
		#rde:  0.04439198970800001
		#rden:  0.040439367293999995
		return("The hardened gardener worked harder but, the warden did not agree. "+
			   "He was burdened to make butter and kill butterflies." +
			   "His butler had a big butt.")
	if name in "Madeleine Houser":
		#ered:  0.14625239372253418
		#appl:  0.11326599121088965
		#ples:  0.1025527715683403
		return("He ordered a layered, towered cake."+
			   "He ate pampered apples."+
			   "Green apples, red apples, blue apples, orange apples.")
	"""
	if(True):
		tupleList = FT.personalCombos(name)
		reducedList = []
		for i in tupleList:
			if i in "garden":
				reducedList.append("garden")
			elif(i in "apples"):
				reducedList.append("apples")
			elif(i in "very"):
				reducedList.append("very")
			else:
				reducedList.append(i)
				
		moreReducedList = []
		for i in reducedList:
				if(not i in moreReducedList):
					moreReducedList.append(i)
		
		sentence = ""
		for tuple in moreReducedList:
			"""LIST OF TUPLES HERE"""
			#ered:  0.032782316207830065
			#very:  0.05450201034500002
			#gard:  0.052145957945999966
			#but:  0.06161534786299999
			#appl:  0.11326599121088965

			if tuple == "ered":
				sentence += "The tiered cake was sheered to be tapered to the top and was ushered to the altered table."
			elif tuple == "very":
				sentence += "Everyday, every woman that was a delivery person showed bravery when faced with the very shivery cold."
				
			elif tuple == "garden":
				sentence += "In the garden there was a gardening gardener, who gardened everyday and liked gardening."
			elif tuple == "but":
				sentence += "There will be no buts about it, the butler will take his butt to the bute by the butter and button shop."
				
			elif tuple == "apples":
				sentence += "He dapples with apples, pineapples, crabapples, and applesauce after he scrapples."
			elif tuple == "eath":
				sentence += "The meathead's breath weathered when the weather was nice and that lead to his death."
			elif tuple == "ther":
				sentence += "I bothered my mother and brother about the other ethers."
			else:
				for i in range(6):
					sentence += tuple +" "
				sentence +=  "."
		return sentence
if __name__ == '__main__':
	#getSentence(["ath", "ver","gard"])#ath", "ver",
	print(manuel("Zachary Nowak"))