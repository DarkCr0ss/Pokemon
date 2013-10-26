import csv,os
evs = 510
en = 0
nombre = ""

stats = {"ps" : 0, \
		 "atq" : 0, \
		 "def" : 0, \
		 "atq sp" : 0, \
		 "def sp" : 0, \
	 	 "vel" : 0}

def entrenamiento():
	res = ""
	while res == "":
		print "elige un tipo de entrenamiento:"
		x = raw_input("(1) = 4 evs\t(2) = 8 evs\t(3) = 12 evs\n:: ").lower()
		if x == "1" or x == "4":
			res = 4
		elif x == "2" or x == "8":
			res = 8
		elif x == "3" or x == "12":
			res = 12
	return res

def comparar(x):
	if x + 4 == 252:
		return "cambie al entrenamiento de 4 puntos"
	elif x + 8 == 252:
		return "cambie al entrenamiento de 8 puntos"
	elif x + 12 == 252:
		return "cambie al entrenamiento de 12 puntos"

def elegir(param = stats):
	x = ""
	while x not in param.keys():
		print "que desea entrenar?"
		print " / ".join(param.keys())
		x = raw_input(":: ").lower()
		if x in param:
			return x
		else:
			print "\"%s\" no es una opcion" % (x)

def mostrar(x,y,z):
	if z <= 0:
		return "%s : %d \t\t\t 0 ev's restantes" % (x,y)
	else:
		return "%s : %d \t\t\t %d ev's restantes" % (x,y,z)

def guardar(n,s = stats):
	x = open("save/%s.csv" % (n),"w")
	for n in s:
		x.write("%s,%d\n" % (n,s[n]))
	x.close()
try:			
	try:
		os.mkdir("save")
	except OSError:
		pass

	if os.listdir("save") != []:
		while True:
			res = raw_input("desea reanudar un entrenamiento?[S/n] ").lower()
			if res == "s" or res == "si":
				while True:
					try:
						x = raw_input("introdusca el nombre del archivo: ")
						f = open("save/%s.csv" % (x))
					except Exception:
						print "\"%s\" esta mal escrito o no exite" % (x)
						print "esto es lo que a guardado:"
						print "\n".join(os.listdir("save"))
						x = raw_input("quiere reintentarlo[S/n] ").lower()
						if x == "s" or x == "si":
							pass
						elif x == "n" or x == "no":
							break
						else:
							print "\"%s\" no es una opcion" % (x)
					else:
						f_csv = csv.reader(f)
						for n,v in f_csv:
							stats[n] = int(v)
						f.close()
						break
				break
			elif res == "n" or res == "no":
				break
			else:
				print "%s no es una opcion" % (res)

	ev = elegir()
	en = entrenamiento()

	print "\t\tInstrucciones:"
	print "(x)multiplicar\t\t\t(s)salir\n(c)cambiar entrenamiento\t(v)ver stats\n(e)elegir otro parametro\t(g)guardar"

	while True:
		
		if stats[ev] == 252:
			print "\"%s\" ya esta al maximo" % (ev)
			ev = elegir()
		
		elif en + stats[ev] > 252:
			print comparar(stats[ev])
			en = entrenamiento()
		
		elif evs <= 0:
			resp = raw_input("desea entrenar otro pokemon?[S/n] ").lower()
			if resp == "si" or resp == "s":
				evs = 510
				for x in stats.keys():
					stats[x] = 0
				en = entrenamiento()
				ev = elegir()

			elif resp == "no" or resp == "n":
				break

		else:
			x = raw_input(":: ").lower()
			
			if x == "x":
				stats[ev] += en * 2
				evs -= en * 2
				print mostrar(ev,stats[ev],evs)
			
			elif x == "s":
				res = raw_input("desea guardar antes de salir?[S/n] ").lower()
				if res == "s":
					if nombre == "":
						nombre = raw_input("ingrese el nombre: ")
					guardar(nombre)
				break
			
			elif x == "e":
				ev = elegir()
			
			elif x == "c":
				en = entrenamiento()
			
			elif x == "v":
				for x in stats:
					print "%s : %s" % (x,stats[x])
			elif x == "g":
				if nombre == "":
					nombre = raw_input("ingrese el nombre: ")
				guardar(nombre)
			
			else:
				stats[ev] += en
				evs -= en
				print mostrar(ev,stats[ev],evs)

	print "\ngracias por usar este programa"
except KeyboardInterrupt:
	print "\ngracias por usar este programa"
except EOFError:
	print "\ngracias por usar este programa"
