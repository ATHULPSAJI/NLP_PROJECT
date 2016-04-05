#!/usr/bin/env python
import sys
def main():
	with open('mod.txt') as f:
    		lines = f.readlines()
    	onetime=[]
    	twotime=[]
    	
    	target=open("vocabulary.txt", 'w')
    	
    	for line in lines:
    		line = line.strip().split(" ")
    		for word in line:
    			if word.isalpha():
	    			if word not in onetime:
	    				onetime.append(word)
	    			elif word not in twotime:
	    				twotime.append(word)
	    				target.write(word)
	    				target.write("\n")
    	target.close()
main()
