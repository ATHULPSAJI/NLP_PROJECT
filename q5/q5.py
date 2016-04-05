#!/usr/bin/env python
import pickle


def main():
	lines = pickle.load( open( "save.p", "rb" ) )
	
	poslines=[]
	neglines=[]
	
	for line in lines:
		if line[0]=='+':
			poslines.append(line)
		elif line[0]=='-':
			neglines.append(line)
	
	i=j=0
	newlines=[]
		
	while i < len(poslines) or i < len(neglines):
		if i < len(poslines):
			newlines.append(poslines[i])
		if i < len(neglines):
			newlines.append(neglines[i])
		i=i+1
		
	lines=newlines
	reviewcount=len(lines)
	grpsize= int((reviewcount-1)/10)+1
	
	acsum=0
	
	for i in range(10):
	
		train=lines[0:grpsize*i]+lines[grpsize*(i+1):]
		trainlen=len(train)
		totalwordsinp=0
		totalwordsinn=0
		vocab=[]
		for line in train:
			line=line.strip().split(" ")
			if line[0] == '+':
				for word in line:
					totalwordsinp+=1
					if word not in vocab:
						vocab.append(word)
			elif line[0] == '-':
				for word in line:
					totalwordsinn+=1
					if word not in vocab:
						vocab.append(word)
					
		vocabulary=len(vocab)
	
		cp=cn=0
	    	for line in train:
	    		if line[0]=='+':
	    			cp=cp+1
	    		elif line[0]=='-':
	    			cn=cn+1
	    	
	    	priorp=float(cp)/trainlen
	    	priorn=float(cn)/trainlen
	    	
	    	#print priorp,priorn
	    	
	    	test=lines[grpsize*i:grpsize*(i+1)]
	    	#print test
	    	filestream=open("pewdie.txt", 'w')
	    	for line in test:
	    		uniwords=[]
	    		words=line.strip().split(" ")
	    		for word in words:
	    			if word not in uniwords:
	    				uniwords.append(word)
	    		probuwp=[]
	    		probuwn=[]
	    		i=0
	    		for word in uniwords:
	    			countwp=countwn=0
	    			for line2 in train:
	    				line2=line2.strip().split(" ")
					if line2[0] == '+':
						for word2 in line2:
							if word == word2:
								countwp+=1
					elif line2[0] == '-':
						for word2 in line2:
							if word == word2:
								countwn+=1
					 
	    			probuwp.append(float(countwp+1)/(totalwordsinp+vocabulary))
	    			probuwn.append(float(countwn +1)/(totalwordsinn+vocabulary))
	    			
	    			
	    		probp=priorp
	    		probn=priorn
	    		for word in words:
	    			ind=uniwords.index(word)
	    			probp*=float(probuwp[ind])
	    			probn*=float(probuwn[ind])
	    			#print probp,probn
	    		
	    		if probp < probn:
	    			filestream.write('- ')
	    			filestream.write(' '.join(words[1:]))
	    			filestream.write('\n')
	    		else:	
	    			filestream.write('+ ')
	    			filestream.write(' '.join(words[1:]))
	    			filestream.write('\n')
	    			
	    	filestream.close()
	    	#print test
	    	accuracy=tp=tn=fp=fn=0
	    	file1 = open('pewdie.txt', 'r')
	    	i=0
		for line1 in file1.readlines():
			line2=test[i].strip().split(" ")
			i+=1
	    		if line1[0]=='+' and  line2[0]=='+' :
				tp=tp+1
			if line1[0]=='-' and  line2[0]=='-' :
				tn=tn+1
			if line1[0]=='+' and  line2[0]=='-' :
				fp=fp+1
			if line1[0]=='-' and  line2[0]=='+' :
				fn=fn+1
			
		
		#print tp,tn,fp,fn
		accuracy=float((tp+tn))/(tp+tn+fp+fn)	
		#print accuracy
		acsum+=accuracy
		
	print "Average Accuracy: ", acsum/10
	
main()
    		
    	
    	
