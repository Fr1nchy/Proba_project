import time	#debug
from math import log
import random
data = {}
def readfile(file) :
	f = open(file, "r")
	for line in f :
		#Parsing lines with whitespaces
		ligne = line.split(" ")
		#Stocking the first element of the line
		classe=int(ligne[0])
		del(ligne[0])
		#first time that we find this class
		if classe not in data.keys() :
			data[classe] = []	#dictionary (key : value) = (class : list of docs)
		data[classe].append({})	#doc = dictionary(word : nb of occurrences)
		for element in ligne :
			couple = element.split(":")
			if (element != '\n' ) :
				data[classe][-1][int(couple[0])] = int(couple[1])		#add in last

	#TO BE DEBUGGED-----------------------------------------------------------------------
	'''for k, v in data.items() :
		print(k,"\n")
		for elem in v :		
			print(elem,"\n")
	time.sleep(2)'''

	#for each word detected through all the docs, listing the number of docs containing it.
	wordpresence = {}	#dictionary(class : dictionary(word : nb of docs containing it))
	nbdocs = {}			#number of documents in each class
	baseapprentissage = [] #Liste des mots dans le texte
	onfaitbazap=True
	for k, v in data.items() :
		rng=random.randint(1,100)
		if rng < 31 : 
			wordpresence[k] = {}
			onfaitbazap=False
		else : 
			onfaitbazap=True
		for elem in v :
			for k2 in elem.keys() :
				#print(k2, "\n")
				if onfaitbazap :							
					if k2 not in baseapprentissage :		# if the current word is not known yet
						baseapprentissage.append(k2)
				else :
					if k2 not in (wordpresence[k]).keys() :	
						(wordpresence[k])[k2] = 1
						if k not in nbdocs :
							nbdocs[k] = 3
						else :
							nbdocs[k] += 1
					else :
						(wordpresence[k])[k2] += 1
				
	#for i in baseapprentissage :
	#	print(i)
	#for i,j in wordpresence.items() :
	#	print(i)
	#	print(j)
	#print(nbdocs)
	#--------------------------------------------------------------------------------------
	return wordpresence,nbdocs,baseapprentissage

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
	nbtotaldocs = 0
	for k, v in data.items() :
		nbtotaldocs = nbtotaldocs + len(v)

	probasK = {}
	i = 0
	for k, v in data.items() :
		probasK[i] = len(v)/nbtotaldocs
		i += 1
	return probasK





#wordintestfile,nbdocsintestfile,baseapprentissage=readfile("BaseReuters-29")
wordininputfile,nbdocsininputfile,baseapprentissage=readfile("test")

la,pasla=probappari(wordininputfile,nbdocsininputfile,baseapprentissage)
print("P : ", computeProbasK(data))


