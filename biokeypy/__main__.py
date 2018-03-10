#cmd /K "$(FULL_CURRENT_PATH)"

#cd ~/Documents/GitHub/Keyboard-Biometric-Project/Project_Tuples
#sudo python -m pip install statistics
#python analyzeData.py

"""
Author: Zachary Nowak and Matthew Nowak
Date: 2/20/2018

Program Description: This code can record the
Press Time and Flight Time of a tuple as a user
types a passage and it saves a matrix to a file.
"""
__version__ = '1.0'
__author__ = 'Zachary Nowak'

"""STANDARD LIBRARY IMPORTS"""
import json
import platform
import os

"""LOCAL LIBRARY IMPORTS"""
import moduleForSavingTimelines as ST
import moduleForRecordingWithGUI as GUI
import moduleForCreatingPasswordSentence as PS
import moduleForDeconstructingTimelines as DT
import moduleForAuthenticatingUsers as AU
import moduleForFindingTuples as FT
import moduleForGettingSentence as GS

"""FOLDER IMPORTS"""
infile = "data/textGoldenBird.txt"# passage for training people.
#tupleList = FT.allPeople()
#tupleList = ["ca", "ow","ery"]
location = ""

if(platform.system() == "Darwin"):
	name = raw_input("What is your name: ")#MAC
	while(not(location == "y" or location == "n")):
		location = raw_input("Is this training data?(y/n) ")
   
if(platform.system() == "Windows"):#WINDOWS
	name = input("What is your name: ")
	while(not(location == "y" or location == "n")):
		location = input("Is this training data?(y/n) ")
#FIND TUPLES
tupleList = FT.personalCombos(name)
		
if(location == "n"):
	location = "Applying/"
	#passage = (PS.makeSentence(tupleList)).split(".")
	try:
		passage = GS.manuel(name).split(".")
	except:
		pass
else:
	location = "Database/"
	passage = open(infile,"r").readlines()


"""TYPE THE PASSAGE AND RECORD THE TIME LINE"""
pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine = GUI.start_recording(passage)
os.chdir("lib/")
ST.saveTimeLine(pressTimeLine,pressCharTimeLine,name,location)
DT.clearSummaries()#CHANGED
DT.userSummary(name,location)

if(location == "Applying/"):
	#AU.newData(tupleList)
	print("Now to verify")
	AU.verify(tupleList,name)
	