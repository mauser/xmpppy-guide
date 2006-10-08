#!/usr/bin/python

# replace the placeholders in tex files with our real scripts and number the lines
import os
import sys
import re

def numberScript(inFile):

	f=open(inFile,"r")
	lines=f.read()
	f.close()

	start_line=1
	spaces=2
	pbuffer=""
	for line in lines.split("\n"):
		if(len(str(start_line))<2):
			sline = "0" + str(start_line)
		else:
			sline=str(start_line)

		pbuffer+=sline
		for i in range(0,spaces): pbuffer+=(" ")
		pbuffer+=str(line)+"\n"

		start_line+=1
	return pbuffer


def replaceScriptInTex(container):
	r=re.compile(".*[.]tex$")

	files=os.listdir("./src")
	for file in files:
		if r.match(file):
			#print file
			f=open("./src/" + file,"r")
			lines=f.readlines()
			f.close
			print "writing to " + file


			f=open("./tmp/" + file,"w")

			for line in lines:
				for replacement in scriptContainer:
					line=line.replace(replacement,scriptContainer[replacement])
				f.write(line)
			f.close()

if not os.path.isdir("./tmp"):
	os.mkdir("./tmp")

#holds the replacestring for every script and the content
scriptContainer={}
r=re.compile(".*[.]py$")
scripts=os.listdir("./examples")
for script in scripts:
	if r.match(script):
		replaceScriptString="$$replace_with_" + script +"$$"
		scriptContainer[replaceScriptString]=numberScript("examples/"+script)

replaceScriptInTex(scriptContainer)