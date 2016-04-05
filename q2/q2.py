#!/usr/bin/env python
import sys
def main():
	with open('data.txt') as f:
    		lines = f.readlines()
    	
    	with open('stopwords.txt') as g:
    		stopwt = g.readlines()
    	
    	stopw=[]
    	for wrd in stopwt:
    		tmp=wrd.rstrip()
    		stopw.append(tmp)
    	
    	target=open("mod.txt", 'w')
    	for line in lines:
    		line=line.lower()
    		line = line.strip().split(" ")
    		target.write(line[0])
    		target.write(" ")
    		for word in line:
    			if word not in stopw:
    				if word.isalpha():
    					target.write(word)
    					target.write(" ")
    		target.write("\n")
    	target.close()
main()
