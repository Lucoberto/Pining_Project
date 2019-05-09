#-*-coding:utf-8-*-
import os, sys, logging
menuac="opciones"
def ayuda():
	os.system("clear")
	global menuac
	var="""

	         db    8b        d8  88        88  88888888ba,         db         
	        d88b    Y8,    ,8P   88        88  88      `"8b       d88b        
	       d8'`8b    Y8,  ,8P    88        88  88        `8b     d8'`8b       
	      d8'  `8b    "8aa8"     88        88  88         88    d8'  `8b      
	     d8YaaaaY8b    `88'      88        88  88         88   d8YaaaaY8b     
	    d8"      "8b    88       88        88  88         8P  d8"      "8b    
	   d8'        `8b   88       Y8a.    .a8P  88      .a8P  d8'        `8b   
	  d8'          `8b  88        `"Y8888Y"'   88888888Y"'  d8'          `8b 
__________________________________________________________________________________________

-> El modo automatico funciona de la siguiente manera:
	-> Tiene asignado un rangode IP(s) de 192.168.1.0 asta 192.168.1.255.
	   Eso significa que solo cubrira ese rango de IP(s).
__________________________________________________________________________________________

-> El modo Personalizado funciona de esta manera:
	-> Tu decides los rangos que queres asignar.
		Colocado la IP donde iniciara y despues la IP en la que quieres acabar.
	-> Las IP(s) se filtraran solo mostrando las que hace PING correctamene. 
		De todas formas todos lo movimientos se guardan el el log.

__________________________________________________________________________________________

		Gracias por usar nuestros productos ©Fury.OS Software.
__________________________________________________________________________________________
	"""
	print(var)
	print("-> 1 para volver atras.")
	op = input("Pininig@pining$~> ")
	if op == "1":
		menuac="opciones"

def automatico():
	global menuac
	ip="192.168.1.255"
	for pri in range(192,256):
		for seg in range(168,256):
			for ter in range(1,256):
				for cua in range(0,256):
					ip2="{}.{}.{}.{}".format(pri,seg,ter,cua)
					if ip == ip2:
						sys.exit()
					else:
						logging.basicConfig(filename='Pining.log',format='%(message)s %(asctime)s',level=logging.WARNING )
						logging.warning("IP --> "+ip2)
						os.system("ping -w 1 "+ip2+"| grep from ")
def a_la_carta():
	global menuac
	parar=0
	print("--> Coloque la primera IP.")
	P1=input("Pininig@pining$~> ")
	p1 = P1.split(".")
	print("--> Coloque la IP a la que quiere llegar.")
	ip=input("Pininig@pining$~> ")
	print("----------------------------------------------")
	for N1 in range(int(p1[0]),256):
		if parar == 1:
			break
		for N2 in range(int(p1[1]),256):
			if parar == 1:
				break
			for N3 in range(int(p1[2]),256):
				if parar == 1:
					break
				for N4 in range(int(p1[3]),256):
					rango="{}.{}.{}.{}".format(N1,N2,N3,N4)
					if ip == rango:
						parar = 1
						break
					else:
						logging.basicConfig(filename='Pining.log',format='%(message)s %(asctime)s',level=logging.WARNING )
						logging.warning("IP --> "+rango)
						os.system("ping -w 1 "+rango+"| grep from ")
menu2="""                                                              
   88888888ba   88  888b      88  88  888b      88    ,ad8888ba,   
   88      "8b  88  8888b     88  88  8888b     88   d8"'    `"8b 
   88      ,8P  88  88 `8b    88  88  88 `8b    88  d8'            
   88aaaaaa8P'  88  88  `8b   88  88  88  `8b   88  88             
   88'          88  88   `8b  88  88  88   `8b  88  88      88888  
   88           88  88    `8b 88  88  88    `8b 88  Y8,        88  
   88           88  88     `8888  88  88     `8888   Y8a.    .a88  
   88           88  88      `888  88  88      `888    `"Y88888P"

___________[<!>]V2.0.4 -> Debeloped by @Lucoberto[<!>]_______________
			[1] Pining Automatico
			[2] Pining Personalizado
			[3] Ayuda
			[4] Salir
"""
def opciones():
	os.system("clear")
	global menuac
	print(menu2)
	print("-> Elija una opcion.")
	op = input("Pininig@pining$~> ")
	if op == "1":
		menuac = "automatico"
	elif op == "2":
		menuac="a_la_carta"
	elif op == "3":
		menuac="ayuda"
	elif op == "4":
		exit()
def motor():
	try:
		while True:
			if menuac == "opciones":
				opciones()
			elif menuac == "automatico":
				automatico()
			elif menuac == "a_la_carta":
				a_la_carta()
			elif menuac == "ayuda":
				ayuda()

	except KeyboardInterrupt:
		sys.exit()
if __name__=="__main__":
	motor()