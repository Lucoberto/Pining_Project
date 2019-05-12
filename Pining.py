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
	-> Usted decide los rangos que quere asignar.
		Colocado la IP donde iniciara y despues la IP en la que quiere finalizar.
	-> Las IP(s) se filtraran solo mostrando las que hace PING correctamene. 
		De todas formas todos lo movimientos se guardan en el log.
__________________________________________________________________________________________

-> El modo URL funciona de la siguiente manera:
	-> Tiene que colcar la URL de la siguiente forma:
		-> www.duckduckgo.com puede ser que alguna pagina no llegue a dar ping
			esto puede llegar a ser por cuestiones de seguridad.
__________________________________________________________________________________________

		Gracias por usar nuestros productos ©Fury.OS Software.
__________________________________________________________________________________________
	"""
	print(var)
	print("-> 1 para volver atras.")
	print("")
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
						logging.basicConfig(filename='Pining.log',format='%(message)s %(asctime)s',level=logging.INFO )
						logging.info("IP --> "+ip2)
						os.system("ping -w 1 "+ip2+"| grep from ")
def a_la_carta():
	global menuac
	parar=0
	print("--> Coloque la primera IP.")
	P1=input("Pininig@pining$~> ")
	p1 = P1.split(".")
	if int(p1[0]) >= int(256):
		menuac="ERROR"
	elif int(p1[1]) >= int(256):
		menuac="ERROR"
	elif int(p1[2]) >= int(256):
		menuac="ERROR"
	elif int(p1[3]) >= int(256):
		menuac="ERROR"
	else:
		print("--> Coloque la IP a la que quiere llegar.")
		ip=input("Pininig@pining$~> ")
		Ip = ip.split(".")
		if int(Ip[0]) >= int(256):
			menuac="ERROR"
		elif int(Ip[1]) >= int(256):
			menuac="ERROR"
		elif int(Ip[2]) >= int(256):
			menuac="ERROR"
		elif int(Ip[3]) >= int(256):
			menuac="ERROR"
		else:
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
								logging.basicConfig(filename='Pining.log',format='%(message)s %(asctime)s',level=logging.INFO )
								logging.info("IP --> "+rango)
								os.system("ping -w 1 "+rango+"| grep from ")
def URL():
	global menuac
	print("--> Coloque la URL a la que quiere hacer ping.")
	url = input("Pininig@pining$~> ")
	os.system("ping -w 1 "+url)
	print("-> 1 para volver atras.")
	print("")
	op = input("Pininig@pining$~> ")
	if op == "1":
		menuac="opciones"
def ERROR():
	global menuac
	error="""
--> ERROR! numero no compatible con el sistema.

	Parece que acaba de colocar un numero que no es compatible o supera
	el rango maximo, no puede colocar mas de 255.255.255.255, 
	ese es el limite establecido.

	"""
	print(error)
	print("-> 1 para volver atras.")
	volveratras = input("Pininig@pining$~> ")
	if volveratras == "1":
		menuac="opciones"

menu2="""                                                              
   88888888ba   88  888b      88  88  888b      88    ,ad8888ba,   
   88      "8b  88  8888b     88  88  8888b     88   d8"'    `"8b 
   88      ,8P  88  88 `8b    88  88  88 `8b    88  d8'            
   88aaaaaa8P'  88  88  `8b   88  88  88  `8b   88  88             
   88'          88  88   `8b  88  88  88   `8b  88  88      88888  
   88           88  88    `8b 88  88  88    `8b 88  Y8,        88  
   88           88  88     `8888  88  88     `8888   Y8a.    .a88  
   88           88  88      `888  88  88      `888    `"Y88888P"

___________[<!>]V5.3.6 -> Debeloped by @Lucoberto[<!>]_______________
			[1] Pining Automatico
			[2] Pining Personalizado
			[3] Pining URL
			[4] Ayuda
			[5] Salir
"""
def opciones():
	os.system("clear")
	global menuac
	print(menu2)
	print("-> Elija una opcion.")
	print("")
	op = input("Pininig@pining$~> ")
	if op == "1":
		menuac = "automatico"
	elif op == "2":
		menuac="a_la_carta"
	elif op == "3":
		menuac="URL"
	elif op == "4":
		menuac="ayuda"
	elif op == "5":
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
			elif menuac == "URL":
				URL()
			elif menuac == "ERROR":
				ERROR()
			elif menuac == "ayuda":
				ayuda()
	except KeyboardInterrupt:
		sys.exit()
if __name__=="__main__":
	motor()
