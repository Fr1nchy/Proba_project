
def readfile(file) :
	f = open(file, "r")
	data = {}

	for line in f :
		#Division de tous les éléments autour du stockage
		ligne = line.split(" ")
		#Stockage du premier élément
		classe=ligne[0]
		del(ligne[0])
		#1ere fois qu'on trouve la classe
		if classe not in data.keys() :
			data[classe] = []	#dictionary (key : value) = (class : list of docs)
		data[classe].append({})	#doc = dictionary(word : nb of occurrences)
		for element in ligne :
			couple = element.split(":")
			if (element != ligne[-1]) :

				data[classe][-1][couple[0]] = couple[1]
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
	for k, v in data.items() :
		print(k,"\n")
		for elem in v :		
			print(elem,"\n")
	

#readfile("BaseReuters-29")
readfile("test")
