#moduleForShowingJudges
#cmd /K "$(FULL_CURRENT_PATH)"

#cd ~/Documents/GitHub/Keyboard-Biometric-Project/Project_Tuples
#sudo python -m pip install statistics
#python analyzeData.py

"""
Author: Zachary Nowak and Matthew Nowak
Date: 3/09/2018

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
import moduleForPlotting as P
"""FOLDER IMPORTS"""
infile = "data/451.txt"# passage for training people.
#tupleList = FT.allPeople()
tupleList = ["his", "the","ing"]
location = ""

 
if(platform.system() == "Windows"):#WINDOWS
	name = input("What is your name: ")
	while(not(location in ["y","n","z","c"])):
		location = input("Is this training data?(y/n) ")
	
if(location == "n"):
	location = "Applying/"
	passage = ("The thing likes learning his history.There the thing sings.This is what the thing sings.").split(".")
elif(location == "z"):
	os.chdir("judgeslib")
	P.plot(tupleList)
elif(location == "c"):
	os.chdir("judgeslib")
	DT.clearAll()
else:
	location = "Database/"
	passages = open(infile,"r").read().split(".")
	passage2 = passages[1].split(",")
	passage = passages + passage2
	passage.remove(passages[1])


"""TYPE THE PASSAGE AND RECORD THE TIME LINE"""
pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine = GUI.start_recording(passage)
os.chdir("judgeslib/")
ST.saveTimeLine(pressTimeLine,pressCharTimeLine,name,location)
DT.userSummary(name,location)

if(location == "Applying/"):
	#AU.newData(tupleList)
	print("Now to verify")
	AU.verify(tupleList,name)
	#IMPLIMENT MATPLOTLIB
	#IMPLIMENT CLEAR FEATURE
	
	
	