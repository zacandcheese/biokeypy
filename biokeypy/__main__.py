#cmd /K "$(FULL_CURRENT_PATH)"

#cd ~/Documents/GitHub/Keyboard-Biometric-Project/Project_Tuples
#sudo python -m pip install statistics
#python analyzeData.py

"""
Author: Zachary Nowak and Matthew Nowak
Date: 2/8/2018

Program Description: This code can record the
Press Time and Flight Time of a tuple as a user
types a passage and it saves a matrix to a file.
"""
__version__ = '1.0'
__author__ = 'Zachary Nowak'

"""STANDARD LIBRARY IMPORTS"""
import json
import platform

"""LOCAL LIBRARY IMPORTS"""

import moduleForSavingTimelines as ST
import moduleForRecordingWithGUI as GUI
import moduleForCreatingPasswordSentence as PS
import moduleForDeconstructingTimelines as DT
import moduleForAuthenticatingUsers as AU
import moduleForFindingTuples as FT

"""FOLDER IMPORTS"""
infile = "data/textGoldenBird.txt"# passage for training people.
tupleList = ["ca","ener"]#ACCOUNT FOR EVERYBODY (MATTS SPREAD SHEET)MAKE A MODULE

if(platform.system() == "Darwin"):
	name = raw_input("What is your name: ")#MAC
	location = raw_input("What is the location: ")
   
if(platform.system() == "Windows"):#WINDOWS
	name = input("What is your name: ")
	location = input("What is your location: ")

if(location != ""):
	location = "Applying/"
	passage = (PS.makeSentence(tupleList)).split(".")
	
else:
	location = "Database/"
	passage = open(infile,"r").readlines()


"""TYPE THE PASSAGE AND RECORD THE TIME LINE"""
pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine = GUI.start_recording(passage)
ST.saveTimeLine(pressTimeLine,pressCharTimeLine,name,location)
DT.userSummary(name,location)
if(location == "Applying/"):
	AU.newData(tupleList)
	