import time	#debug

def readfile(file) :
	f = open(file, "r")
	data = {}

	for line in f :
		#Parsing lines with whitespaces
		ligne = line.split(" ")
		#Stocking the first element of the line
		classe=ligne[0]
		del(ligne[0])
		#first time that we find this class
		if classe not in data.keys() :
			data[classe] = []	#dictionary (key : value) = (class : list of docs)
		data[classe].append({})	#doc = dictionary(word : nb of occurrences)
		for element in ligne :
			couple = element.split(":")
			if (element != ligne[-1]) :

				data[classe][-1][couple[0]] = couple[1]		#add in last
			else :
				if element != '\n' : 
					data[classe][-1][couple[0]] = couple[1]

	#TO BE DEBUGGED-----------------------------------------------------------------------
	'''for k, v in data.items() :
		print(k,"\n")
		for elem in v :		
			print(elem,"\n")
	time.sleep(2)'''

	#for each word detected through all the docs, listing the number of docs containing it.
	wordpresence = {}	#dictionary(class : dictionary(word : nb of docs containing it))
	for k, v in data.items() :
		#print(k,"###########\n")
		#if k not in wordpresence.keys() : 			optional
		wordpresence[k] = {}
		for elem in v :
			for k2 in elem.keys() :
				#print(k2, "\n")
				if k2 not in (wordpresence[k]).keys() :
					(wordpresence[k])[k2] = 1
				else :
					#print((wordpresence[k])[k2]+"\n")
					(wordpresence[k])[k2] += 1
				
	#for i in wordpresence.keys() :
		#print(i)
	for i,j in wordpresence.items() :
		print(i)
		print(j)
	#--------------------------------------------------------------------------------------


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

#readfile("BaseReuters-29")
readfile("test")
