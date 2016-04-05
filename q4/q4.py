#!/usr/bin/env python
import pickle
def main():
	            		
        with open('mod.txt') as f:
    		lines = f.readlines()
    	reviewcount=len(lines)
    	cp=cn=0
    	for line in lines:
    		if line[0]=='+':
    			cp=cp+1
    		elif line[0]=='-':
    			cn=cn+1
    	
    	priorp=float(cp)/reviewcount
    	priorn=float(cn)/reviewcount
    	
    	print priorp,priorn
    	
    	pickle.dump(lines,open( "save.p", "wb" ) )
    	
    		
    	
main()
