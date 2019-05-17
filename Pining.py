#-*-coding:utf-8-*-
import os, sys, logging,platform
menuac="opciones"
R= '\033[31m'
G= '\033[32m'
C= '\033[36m'
P= '\033[35m'
O= '\033[33m'
W= '\033[0m'
def ayuda():
	os.system("clear")
	global menuac
	logoayuda="""

	  /$$$$$$                            /$$
	 /$$__  $$                          | $$
	| $$  \ $$ /$$   /$$ /$$   /$$  /$$$$$$$  /$$$$$$ 
	| $$$$$$$$| $$  | $$| $$  | $$ /$$__  $$ |____  $$
	| $$__  $$| $$  | $$| $$  | $$| $$  | $$  /$$$$$$$
	| $$  | $$| $$  | $$| $$  | $$| $$  | $$ /$$__  $$
	| $$  | $$|  $$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$
	|__/  |__/ \____  $$ \______/  \_______/ \_______/
	           /$$  | $$ 
	          |  $$$$$$/
	           \______/"""

	explicaci="""
__________________________________________________________________________________________

-> El modo automatico funciona de la siguiente manera:
	-> Tiene asignado un rangode IP(s) de 192.168.1.0 asta 192.168.1.255.
	   Eso significa que solo cubrira ese rango de IP(s)."""
	
	expliPer="""
__________________________________________________________________________________________

-> El modo Personalizado funciona de esta manera:
	-> Usted decide los rangos que quere asignar.
		Colocado la IP donde iniciara y despues la IP en la que quiere finalizar.
	-> Las IP(s) se filtraran solo mostrando las que hace PING correctamene. 
		De todas formas todos lo movimientos se guardan en el log."""

	expliUR="""
__________________________________________________________________________________________

-> El modo URL funciona de la siguiente manera:
	-> Tiene que colcar la URL de la siguiente forma:
		-> https://duckduckgo.com puede ser que alguna pagina no llegue a dar ping
			esto puede ser por cuestiones de seguridad del propio servidor."""

	Desp="""
__________________________________________________________________________________________

		                 Atentamente ©Fury.OS Software.
__________________________________________________________________________________________
	"""
	print(C+logoayuda+W)
	print(P+explicaci+W)
	print(G+expliPer+W)
	print(O+expliUR+W)
	print(R+Desp+W)
	print(R+'[1]'+O+' para volver atras.'+W)
	print("")
	op = input(G+'Pininig'+P+'@'+G+'pining'+P+'$~> '+W)
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
	print(R+'[1]'+O+' para salir '+G+'o'+C+' Coloque la pimera IP.'+W)
	P1=input(G+'Pininig'+P+'@'+G+'pining'+P+'$~> '+W)
	p1 = P1.split(".")
	if P1 == "1":
		menuac="opciones"
	elif int(p1[0]) >= int(256):
		menuac="ERROR"
	elif int(p1[1]) >= int(256):
		menuac="ERROR"
	elif int(p1[2]) >= int(256):
		menuac="ERROR"
	elif int(p1[3]) >= int(256):
		menuac="ERROR"
	else:
		print(R+'[1]'+O+' para salir '+G+'o'+C+' Coloque la IP a la que quiere llegar.'+W)
		ip=input(G+'Pininig'+P+'@'+G+'pining'+P+'$~> '+W)
		Ip = ip.split(".")
		if ip == "1":
			menuac="opciones"
		elif int(Ip[0]) >= int(256):
			menuac="ERROR"
		elif int(Ip[1]) >= int(256):
			menuac="ERROR"
		elif int(Ip[2]) >= int(256):
			menuac="ERROR"
		elif int(Ip[3]) >= int(256):
			menuac="ERROR"
		else:
			print(P+'----------------------------------------------'+W)
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
	print(C+'--> Coloque la URL a la que quiere hacer ping.'+W)
	url = input(G+'Pininig'+P+'@'+G+'pining'+P+'$~> '+W)
	logging.basicConfig(filename='Pining.log',format='%(message)s %(asctime)s',level=logging.INFO )
	logging.info("URL --> "+url)
	os.system("curl -Is   "+url+" | head -1")
	print(R+'[1]'+O+' para volver atras.'+W)
	print("")
	op = input(G+'Pininig'+P+'@'+G+'pining'+P+'$~> '+W)
	if op == "1":
		menuac="opciones"
def ERROR():
	global menuac
	error="""
	Parece que acaba de colocar un numero que no es compatible o supera
	el rango maximo, no puede colocar mas de 255.255.255.255, 
	ese es el limite establecido.

	"""
	print(R+' ERROR!'+P+' numero no compatible con el sistema.'+W)
	print(P+error+W)
	print(R+'[1]'+O+' para volver atras.'+W)
	volveratras = input(G+'Pininig'+P+'@'+G+'pining'+P+'$~> '+W)
	if volveratras == "1":
		menuac="a_la_carta"

logomenu="""                         
 
	 /$$$$$$$  /$$           /$$
	| $$__  $$|__/          |__/
	| $$  \ $$ /$$ /$$$$$$$  /$$ /$$$$$$$   /$$$$$$
	| $$$$$$$/| $$| $$__  $$| $$| $$__  $$ /$$__  $$
	| $$____/ | $$| $$  \ $$| $$| $$  \ $$| $$  \ $$
	| $$      | $$| $$  | $$| $$| $$  | $$| $$  | $$
	| $$      | $$| $$  | $$| $$| $$  | $$|  $$$$$$$
	|__/      |__/|__/  |__/|__/|__/  |__/ \____  $$
	                                       /$$  \ $$
	                                      |  $$$$$$/
	                                       \______/"""

def opciones():
	os.system("clear")
	global menuac
	print(C + logomenu + W)
	print("")
	print(P + '___________[<!>]'+ C +'V5.4.9 -> Debeloped by'+ R +' @Lucoberto'+ P +'[<!>]_______________'+W)
	print("")
	print(R +'			[+]'+O+' Elija una opcion'+W)
	print(R +'			[1]'+O+' Pining Automatico'+W)
	print(R +'			[2]'+O+' Pining Personalizado'+W)
	print(R +'			[3]'+O+' Pining URL'+W)
	print(R +'			[4]'+O+' Ayuda'+W)
	print(R +'			[5]'+O+' Salir'+W)
	print("")
	op = input(G+'Pininig'+P+'@'+G+'pining'+P+'$~> '+W)
	if op == "1":
		menuac = "automatico"
	elif op == "2":
		menuac="a_la_carta"
	elif op == "3":
		menuac="URL"
	elif op == "4":
		menuac="ayuda"
	elif op == "5":
		sys.exit()
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
