#-*-coding:utf-8-*-
import os,sys
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
	   tendras que rellenar todas haste completar el rango de inicio y final.
		-> Por ejemplo:
		   	-> El rango de Inicio |195|168|0|1| y al final colocas la IP hasta la que
			   quieres llegar --> 195.168.0.50. 
		   	-> Muy importante:
		   	   No tienes que colocar puntos en la primera IP pero si en la IP final.
		   	   solo tienes que colocar las cifras de la primera IP.
		   		-> Por ejemplo:
		   			Numero1: 195 Numero2: 168 Numero3: 0 Numero4: 1
		   			asi con la primera y con la segunad segunda IP tienes que colocar
					toda la IP 195.168.0.50.
__________________________________________________________________________________________

		Gracias por usar nuestros productos ©Fury.OS Software.
__________________________________________________________________________________________
	"""
	print(var)
	op = input("-> 1 para volver atras: ")
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
						os.system("ping -w 1 {}.{}.{}.{}".format(pri,seg,ter,cua))
def a_la_carta():
	global menuac
	print("--> IP de partida coloque de celda en celda")
	P1=input("Primera celda de la IP: ")
	a = int(P1)
	P2=input("Seguda celda de la IP: ")
	b = int(P2)
	P3=input("Tercera celda de la IP: ")
	c = int(P3)
	P4=input("Cuarta celda de la IP: ")
	d = int(P4)
	print("--> Coloque la IP a la que quiere llegar.")
	ip=input("Coloque la IP: ")
	for N1 in range(a,256):
		for N2 in range(b,256):
			for N3 in range(c,256):
				for N4 in range(d,256):
					rango="{}.{}.{}.{}".format(N1,N2,N3,N4)
					if ip == rango:
						sys.exit()
					else:
						os.system("ping -w 1 {}.{}.{}.{}".format(N1,N2,N3,N4))
menu2="""                                                              
   88888888ba   88  888b      88  88  888b      88    ,ad8888ba,   
   88      "8b  88  8888b     88  88  8888b     88   d8"'    `"8b  
   88      ,8P  88  88 `8b    88  88  88 `8b    88  d8'            
   88aaaaaa8P'  88  88  `8b   88  88  88  `8b   88  88             
   88'          88  88   `8b  88  88  88   `8b  88  88      88888  
   88           88  88    `8b 88  88  88    `8b 88  Y8,        88  
   88           88  88     `8888  88  88     `8888   Y8a.    .a88  
   88           88  88      `888  88  88      `888    `"Y88888P"

___________[<!>]V3.2.4 -> Debeloped by @Lucoberto[<!>]_______________
			[1] Pining Automatico
			[2] Pining Personalizado
			[3] Ayuda
			[4] Salir
"""
def opciones(): 
	os.system("clear")
	global menuac
	print(menu2)
	op = input("Elija la opcion mas adecuada: ")
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
