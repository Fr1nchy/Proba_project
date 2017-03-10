import time	#debug
from math import log
import random
data = {}
def readfile(file) :
	f = open(file, "r")
	#for each word detected through all the docs, listing the number of docs containing it.
	wordpresence = {}	#dictionary(class : dictionary(word : nb of docs containing it))
	nbdocs = {}			#number of documents in each class
	baseapprentissage = [] #Liste des mots dans le texte
	onfaitbazap=True
	wordtest=[]

	for line in f :
		rng=random.randint(1,100)
		# parsing lines with whitespaces
		ligne = line.split(" ")
		# stocking the first element of the line
		classe=int(ligne[0])
		del(ligne[0])
		# first time that we find this class
		if rng < 31 : 
			wordtest.append((classe,[]))
			onfaitbazap=False
		else : 
			if classe not in wordpresence : 
				wordpresence[classe] = {}
			onfaitbazap=True
		#if classe not in data.keys() :
			#data[classe] = []	# dictionary (key : value) = (class : list of docs)
		#data[classe].append({})	# doc = dictionary(word : nb of occurrences)
		for element in ligne :
			couple = element.split(":")
			if (element != '\n' ) :
				k2 = int(couple[0])
				#data[classe][-1][int(couple[0])] = int(couple[1])		# add in last
				if onfaitbazap :			
					if k2 not in baseapprentissage :		# if the current word is not known yet
						baseapprentissage.append(k2)
					if k2 not in (wordpresence[classe]).keys() :	
						(wordpresence[classe])[k2] = 1
						if classe not in nbdocs :
							nbdocs[classe] = 3
						else :
							nbdocs[classe] += 1
					else :
						(wordpresence[classe])[k2] += 1
				else :
					if k2 not in wordtest[-1][1] :
						wordtest[-1][1].append(k2)
	return wordpresence,nbdocs,baseapprentissage,wordtest

def probappari(dicomot,nbdocs,baza) :
    apari={}
    absence={}
    for i in dicomot :
        apari[i]={}
        absence[i]=(log(1/nbdocs[i]),log(1-(1/nbdocs[i])))
        for j,k in dicomot[i].items() :
            nbmaux=int(nbdocs[i])
            apari[i][j]=(k+1)/nbmaux
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
#print("P : ", probasK)
i=0
bigsums=[]
juste = 0
faux = 0
for j in motdanstest : 
	#print(j)
	bigsums.append({})
	for z in baseapprentissage :
	#Mot dans doctest ?
		if z in j[1] : 
			Motdansdoctest = True
		else : 
			Motdansdoctest = False
		for ka in wordininputfile.keys() :
		#mot dans K ?
			if ka not in bigsums[-1].keys() :
				bigsums[-1][ka] = 0
			if Motdansdoctest :
				if z in wordininputfile[ka].keys() :
					bigsums[-1][ka]+=log(la[ka][z])
				else :
					if z in la[ka] :
						bigsums[-1][ka]+=log(1-la[ka][z])
					#else : 
						#bigsums[-1][ka]+=pasla[ka][1]
			else : 
				if z in wordininputfile[ka].keys() :
					#bigsums[-1][ka]+=pasla[ka][0]
					a=1
				else :
					#bigsums[-1][ka]+=pasla[ka][1]
					a=2
	maxi = 0
	classem = 0
	for a,b in bigsums[-1].items() :
		if b < maxi :
			maxi = b
			classem = a
	if classem == j[0] :
		juste += 1
	else :
		faux += 1
print("Score Juste : ", juste)
print("Score Faux : ", faux)


