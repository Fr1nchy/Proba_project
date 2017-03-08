import time	#debug
from math import log
import random
data = {}
def readfile(file) :
	f = open(file, "r")
	for line in f :
		# parsing lines with whitespaces
		ligne = line.split(" ")
		# stocking the first element of the line
		classe=int(ligne[0])
		del(ligne[0])
		# first time that we find this class
		if classe not in data.keys() :
			data[classe] = []	# dictionary (key : value) = (class : list of docs)
		data[classe].append({})	# doc = dictionary(word : nb of occurrences)
		for element in ligne :
			couple = element.split(":")
			if (element != '\n' ) :
				data[classe][-1][int(couple[0])] = int(couple[1])		# add in last


	#for each word detected through all the docs, listing the number of docs containing it.
	wordpresence = {}	#dictionary(class : dictionary(word : nb of docs containing it))
	nbdocs = {}			#number of documents in each class
	baseapprentissage = [] #Liste des mots dans le texte
	onfaitbazap=True
	wordtest=[]
	for k, v in data.items() :
		rng=random.randint(1,100)
		if rng < 31 : 
			wordtest.append((k,[]))
			onfaitbazap=False
		else : 
			wordpresence[k] = {}
			onfaitbazap=True
		for elem in v :
			for k2 in elem.keys() :
				#print(k2, "\n")
				if onfaitbazap :							
					if k2 not in baseapprentissage :		# if the current word is not known yet
						baseapprentissage.append(k2)
					if k2 not in (wordpresence[k]).keys() :	
						(wordpresence[k])[k2] = 1
						if k not in nbdocs :
							nbdocs[k] = 3
						else :
							nbdocs[k] += 1
					else :
						(wordpresence[k])[k2] += 1
				else :
					if k2 not in wordtest[-1][1] :
						wordtest[-1][1].append(k2)
	print("WT", wordtest)					
	#for i in baseapprentissage :
	#	print(i)
	#for i,j in wordpresence.items() :
	#	print(i)
	#	print(j)
	#print(nbdocs)
	return wordpresence,nbdocs,baseapprentissage,wordtest

	'''
	#verification qu'on est pas dans le dernier élément
	if (element != ligne[-1]) :
		#recuperation de la clef
		print(couple[0])
		#recup nb occur
		print(couple[1])'''	
	'''
	#Suppression du premier element que l'on devra avoir stocke avant. 
	del (ligne[0])
	#division de clef & nombre occurence		
	for element in ligne :
		couple = element.split(":")
		#verification qu'on est pas dans le dernier élément
print(la)
print(pasla)
		if (element != ligne[-1]) :
			#recuperation de la clef
			print(couple[0])
			#recup nb occur
			print(couple[1])
	'''

	#return data
	#affichage de data
	'''for k, v in data.items() :
		print(k,"\n")
		for elem in v :		
			print(elem,"\n")
	'''

def probappari(dicomot,nbdocs,baza) :
    apari={}
    absence={}
    for i in dicomot :
        print(i)
        apari[i]={}
        absence[i]=(log(1/nbdocs[i]),log(1-(1/nbdocs[i])))
        print(absence[i])
        for j,k in dicomot[i].items() :
            #print(j, k)
            nbmaux=int(nbdocs[i])
            apari[i][j]=(k+1)/nbmaux
            #if j in prezdansdoc :
                #prezdansdoc.remove(j)
        #print(prezdansdoc)
        #for h in prezdansdoc :
    
    #for i,j in apari.items() : 
        #print(i,j)
	#for i,j in baseapprentissage.items() :
	#	print(i,j)
    #for i,j in absence.items() :
        #print (i,j)
    return apari,absence

def computeProbasK(data) :
	nbtotaldocs = sum(len(v) for v in data.values())				# total number of documents in the learning base
	dictprobasK = {}
	for k, v in data.items() :										# compute and store p(k) for each class k in the learning base
		dictprobasK[k] = len(v)/nbtotaldocs
	return dictprobasK



#wordintestfile,nbdocsintestfile,baseapprentissage=readfile("BaseReuters-29")
wordininputfile,nbdocsininputfile,baseapprentissage,motdanstest=readfile("test")

la,pasla=probappari(wordininputfile,nbdocsininputfile,baseapprentissage)
probasK = computeProbasK(data)
print("P : ", probasK)

'''
allwords = []
for k, v in wordininputfile.items() :		# for each class detected in the input file
	for k2, v2 in v.items() :				# for each word found existing in this class
		if k2 not in allwords :				# if this word hasn't been seen yet amongst previous classes
			allwords.append(k2)				# add the word to the words already seen in the input file

bigsums = []
index = 0									# dictionary (class : log(p(k|current doc in testbase))
for doctest in motdanstest :				# for each document of the test base
	bigsums.append({})
	for k, v in data.items():				# for each class k detected in the input file 
		s = 0								# initialise log(p|k) to zero
		for word in allwords :				# for each word amongst all the different words in the learning base
			if word in doctest[1] :			# if the word of the learning base exists in the current document of the test base
				s += pasla[word][0]		# add log(p(word|k)) to log(p|k)
			else :							# else
				s += pasla[word][1]		# add the log of the opposite probability 1-p(word|k) to log(p|k)
		bigsums[-1] = s + log(probasK[k])	# store dictionary(k : log(p(k|doc))

print(bigsums)
'''

