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
	buffer=""
	for line in lines.split("\n"):
	
		buffer+=str(start_line)
		for i in range(0,spaces): buffer+=(" ") 
		buffer+=str(line)+"\n"

		start_line+=1 
	return buffer
	


def replaceScriptInTex(script,buffer):
	r=re.compile(".*[.]tex$")
	
	files=os.listdir("./src")
	for file in files:
		if r.match(file):
			print file
			f=open("./src/" + file,"r")
			lines=f.readlines()
			f.close
			print "writing to " + file
			f=open("./tmp/" + file,"w")
			for line in lines:
				repl_string="$$replace_with_"+script+"$$"
				f.write(line.replace(repl_string,buffer))
			f.close()

if not os.path.isdir("./tmp"):
	os.mkdir("./tmp")
				
r=re.compile(".*[.]py$")
scripts=os.listdir("./examples")
for script in scripts:
	if r.match(script):
		replaceScriptInTex(script,numberScript("examples/"+script))

