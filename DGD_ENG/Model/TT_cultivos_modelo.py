"""
******************************************************************
Autores:
López Juárez Anayantzin Paola
Vargas Monroy Israel Agustin
Trabajo: ESCOM-IPN TT A009
TT-II Tratamiento de imágenes con CNN para la estimación de la sa-
lud de los cultivos.
Versión:
0.0
Descripción de clase:
En este script se colocan TODAS las funciones de back-end, se toman 
las imagenes, se renombran, se extraen metadatos y se colocan en un 
archivo de texto, se ordenan, se cortan, se redimensionan, se seri-
alizan y se propagan hacia adelante en la RNC
******************************************************************
"""

"""
Imports: modulos de las librerias de python
Imports de paquetes: clases que importamos de cada carpeta del pro
yecto.
"""
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image,ImageOps,ImageDraw
#import piexif
import numpy as np
import pickle
import csv
from sklearn.utils import shuffle
import os
import sys
import glob
import errno
import string
from sys import platform
from bs4 import BeautifulSoup
#from libxmp import XMPFiles #We replace this library for BeatifulSoup
import math

class TT_modelo:
	"""El constructor de la clase debe de generar la instanciación
	de la arquitectura y el entrenamiento de la red (NO SE VUELVE 
	A ENTRENAR, SOLO SE HACE REFERENCIA A ELLOS PARA PROPAGAR HACI
	A ADELANTE)"""
	def GPS_Metadata(self,imagen):
	    #Función que regresa un bonito diccionario con los datos solo del GPS de la imagen
	    #y la fecha con horas, minutos y segundos en que la foto fue digitalizada.
	    GPS_metadata = {}#Declara dic
	    date_metadata = {}
	    info = imagen._getexif()#Pide los datos exif
	    if info:
	        for tag, value in info.items(): #Este ciclo revisa todas las etiquetas que existen en el archivo exif
	            decoded = TAGS.get(tag, tag)
	            if decoded == "GPSInfo":#Si la etiqueta corresponde a informacion de GPS
	                gps_data = {} #Crea diccionario
	                for t in value: 
	                    sub_decoded = GPSTAGS.get(t, t)#Se pide en el primer parametro, el nombre de la referencia 
	                                                    #y en el segundo parametro su valor
	                    gps_data[sub_decoded] = value[t]
	                GPS_metadata[decoded] = gps_data
	            if decoded == "DateTimeDigitized":#Si la etiqueta corresponde a la fecha y hora en que se tomo la foto
	                date_data = {} #Crea diccionario
	                date_metadata[decoded] = value
	            #else:
	             #   GPS_metadata[decoded] = value
	    return GPS_metadata,date_metadata

	def key_dic(self,data,key):
	    #Devuelve la el dato del diccionario que se requiere si este existe
	    if key in data:
	        return data[key]
	    else:
	        print("No se encuentra en diccionario")
	    return None

	def convert_to_degress(self,value):
	    #Convierte las coordenadas a grados decimales, mismos que puede utilizar cualquier sistema GPS
	    d0 = value[0][0]
	    d1 = value[0][1]
	    d = float(d0) / float(d1)

	    m0 = value[1][0]
	    m1 = value[1][1]
	    m = float(m0) / float(m1)

	    s0 = value[2][0]
	    s1 = value[2][1]
	    s = float(s0) / float(s1)

	    return d + (m / 60.0) + (s / 3600.0)

	def lat_lon_date(self,GPS_metadata,date_metadata):
	    #Se va a comprobar que los datos GPS existan y se extrae la informacion de ellos
	    #para despues obtener latitud y longitud con el signo real
	    lat = None
	    lon = None
	    alt = None
	    date = None

	    if "GPSInfo" in GPS_metadata:
	        gps_info = GPS_metadata["GPSInfo"]

	        gps_latitude = self.key_dic(gps_info, "GPSLatitude")
	        gps_latitude_ref = self.key_dic(gps_info, 'GPSLatitudeRef')
	        gps_longitude = self.key_dic(gps_info, 'GPSLongitude')
	        gps_longitude_ref = self.key_dic(gps_info, 'GPSLongitudeRef')
	        gps_altitude = self.key_dic(gps_info, 'GPSAltitude')
	    
	        date = date_metadata["DateTimeDigitized"]

	        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
	            lat = self.convert_to_degress(gps_latitude)
	            if gps_latitude_ref != "N": #Si es norte es latitud positiva                    
	                lat = 0 - lat

	            lon = self.convert_to_degress(gps_longitude)
	            if gps_longitude_ref != "E": #Si es este es longitud positiva
	                lon = 0 - lon
	        
	        if gps_altitude:
	        	alt = gps_altitude[0]/gps_altitude[1]
	    return lat, lon, alt, date

	def get_date(self,date):
	    year = date[0:4]
	    month = date[5:7]
	    day = date[8:10]
	    hour = date[11:13]
	    minu = date[14:16]
	    sec = date[17:19]

	    return int(year+month+day+hour+minu+sec)

	def renamer(self):#Recibe path
	    cont = 0
	    for fname in sorted(glob.glob(self.path+'*.JPG'),key=os.path.getmtime):
	        os.rename(fname,self.path+str(cont)+'.JPG')#Aqui va la extensión con la cual se va a renombrar
	        cont = cont+1
	    return None 
	def cut_img(self,img,num_img,directorio,high):
	    """
	    GET: La imagen, el numero de imagen a la que corresponde, el directorio que se creo para poner las imagenes
	        y la altura a la que se volo el dron
	    Return: Se devolverán las 12 imagenes
	    """
	    l_img = []
	    cont=0
	    h=img.size[0]
	    v=img.size[1]
	    print(num_img)
	    if int(high) == 2:
	        if (h == 4000 and v == 3000) or (h == 4032 and v == 3024):
	            for y in range(0,3000,1000):
	                for x in range(0,4000,1000):
	                    img_n = img.crop((x,y,1000+x,1000+y))
	                    img_n.save(self.path+directorio+"/"+str(num_img)+"_"+str(cont)+".JPG")
	                    l_img.append(img_n)
	                    cont=cont+1
	        elif (h == 3000 and v == 4000) or (h == 3024 and v == 4032):
	            for y in range(0,4000,1000):
	                for x in range(0,3000,1000):
	                    img_n = img.crop((x,y,1000+x,1000+y))
	                    img_n.save(self.path+directorio+"/"+str(num_img)+"_"+str(cont)+".JPG")
	                    l_img.append(img_n)
	                    cont=cont+1

	    elif int(high) == 30:
	        if (h == 4000 and v == 3000) or (h == 4032 and v == 3024):
	            for y in range(0,3000,200):
	                for x in range(0,4000,200):
	                    img_n = img.crop((x,y,200+x,200+y))
	                    img_n.save(self.path+directorio+"/"+str(num_img)+"_"+str(cont)+".JPG")
	                    l_img.append(img_n)
	                    cont=cont+1
	        elif (h == 3000 and v == 4000) or (h == 3024 and v == 4032):
	            for y in range(0,4000,200):
	                for x in range(0,3000,200):
	                    img_n = img.crop((x,y,200+x,200+y))
	                    img_n.save(self.path+directorio+"/"+str(num_img)+"_"+str(cont)+".JPG")
	                    l_img.append(img_n)
	                    cont=cont+1
	        else:
	            print('Tamaño NO identificado')
	            print(self.path+"/"+num_img)
	    else:
	        print('NO SE QUE ALTURA ES!')
	    return l_img
	
	def resizeador(self,high): #path
		'''Paso siguiente se deben redimensionar las imagenes cortadas'''
		if high == 2:
			for item in glob.glob(self.path+"ImgsCut/*.JPG"):
				img = Image.open(item)
				im = ImageOps.fit(img,(200,200),Image.ANTIALIAS)
				if platform == "linux" or platform == "linux2":
					l_aux = item.split('/')
				elif platform == "darwin":
					l_aux = item.split('/')
				elif platform == "win32":
					l_aux = item.split('\\')
				im.save(self.path+"ImgsResize/"+l_aux[-1])
		if high == 30:
			pass
		return None

	def MakePickle(self,high,dicc_pos): #path
		if high == 2:
			lNS = []
			for k,v in dicc_pos.items():
				for pedazo in range(0,12):
					name = self.path + 'ImgsCut/'+ str(k) + "_" + str(pedazo) +'.JPG'
					nparr = np.array(Image.open(name))
					lNS.append([nparr])
		if high == 30:
			lNS = []
			for k,v in dicc_pos.items():
				for pedazo in range(0,300):
					name = self.path + 'ImgsCut/'+ str(k) + "_" + str(pedazo) +'.JPG'
					nparr = np.array(Image.open(name))
					lNS.append([nparr])

		pathy = self.path+"pickle/pickle"
		dim = len(lNS)

		if dim >= 300:
			dim1 = dim/300
			h = 0
			for d in range(0,int(dim1)):
				pickle.dump(lNS[h:300+h],open(pathy+"_"+str(d)+".pickle","wb"))
				h = h + 300
		print(dim)
		print('Finish preprocessing')
		#pickle.dump(lNS[0:dim],open(pathy,"wb"))#Se debe hacer un cich
		return dim

	def VerificaSigno(self,L_signo):
		cont_signo = 0
		signo_capital = L_signo[0]
		for l in L_signo:
			if l == signo_capital:
				cont_signo = cont_signo + 1
			else:
				break
		return cont_signo,signo_capital

	def all_renamerGPS_data(self): #path
	    #Se extraen los datos de TODAS las imagenes
	    alt = 0
	    all_metadata = {}
	    cont_alt = 0
	    L_signo = []

	    altura_absoluta = 2235.81 #Altura sobre el nivel del mar de ESCOM 
	    self.renamer()#Renombra archivos ordenados
	    if os.path.exists(self.path+'ImgsCut') == False:
	    	os.makedirs(self.path+'ImgsCut')
	    if os.path.exists(self.path+'pickle') == False:
	    	os.makedirs(self.path+'pickle')
	    if os.path.exists(self.path+'rotacion') == False:
	    	os.makedirs(self.path+'rotacion')
	    if os.path.exists(self.path+'ImgsBlended') == False:
	    	os.makedirs(self.path+'ImgsBlended')

	    for cont,img in enumerate(sorted(glob.glob(self.path +'*.JPG'),key=os.path.getmtime)):
	    	imagen = Image.open(img)#Abre imagen
	    	GPS_superData,date_superData = self.GPS_Metadata(imagen)#2 diccionarios con GPS y fecha
	    	lat,lon,alt,date = self.lat_lon_date(GPS_superData,date_superData)#Transforma los GPS
	    	sumdate=self.get_date(date)#Transforma fecha en ID
	    	if platform == "linux" or platform == "linux2":
	    		name = str.split(str(img),"/")
	    	elif platform == "darwin":
	    		name = str.split(str(img),"/")
	    	elif platform == "win32":
	    		name = str.split(str(img),"\\")
	    	name = name[-1]
	    	all_metadata[name]=[lat,lon,alt,sumdate]#Se mete todo en un diccionario
	    	#Se requieren extraer los datos que vienen del archivo XMP
	    	RelativeAltitude , signo = self.ExtraerXMP(img)
	    	L_signo.append(signo)
	    	imagen.close()
	    
	    cont_signo,signo_capital = self.VerificaSigno(L_signo)
	    return all_metadata, RelativeAltitude, cont_signo, signo_capital,L_signo,sumdate

	def banderas_mapa(self,all_metadata,cont_signo,L_signo):
		strx = '' #Aqui indicamos hacia donde se va a pegar la imagen
		esquina='' #Aquí indicamos desde donde comienza el vuelo, es decir si la imagen 0 esta ubicada ya sea en (0,0), (0,n), (n,0), (n,n)
		rotacion_t1='' #Hacia donde rotar cada imagen en la primer tira
		rotacion_t2='' #Hacia donde rotar cada imagene de la segunda tira , estos se repiten una si otra no empezando por tira 1
		l1 = []
		l2 = []
		l1 = all_metadata["0.JPG"]
		l2 = all_metadata[str(cont_signo-1) + ".JPG"]
		name_L = len(L_signo)-1
		name_PL = len(L_signo) - (cont_signo-1)
		l4 = all_metadata[str(name_L) + '.JPG']
		l3 = all_metadata[str(name_PL) + '.JPG']
		lat1 = l1[0]
		lat2 = l2[0]
		lon1 = l1[1]
		lon2 = l2[1]
		lado1 = cont_signo
		lado2 = len(L_signo)/lado1

		'''print(all_metadata["0.JPG"])
		print(all_metadata[str(cont_signo-1) + ".JPG"])
		print(L_signo[cont_signo-1])
		print('lat: ')
		print(lat1-lat2)
		print('lon: ')
		print(abs(lon1-lon2))'''
		if (abs(lat1-lat2)) > (abs(lon1-lon2)):
			strx = 'lat'
			#print('lat')
		else:
			strx = 'lon'
			#print('lon')
		ref,diag = self.dir_tiras(strx,l1,l3,l4)
		print(ref,diag)

		if (L_signo[cont_signo-1] == '+') and (strx == 'lon'):
			if ref == 'abajo': #Caso pix4d
				esquina = 'NO'
				rotacion_t1 = '90D'
				rotacion_t2 = '90I'
			elif ref == 'arriba': #Caso posibles
				esquina = 'SO'
				rotacion_t1 = '90D'
				rotacion_t2 = '90I'
		elif (L_signo[cont_signo-1] == '+') and (strx == 'lat'):
			if ref == 'izquierda': #Caso posibles
				esquina = 'SE'
				rotacion_t1 = '0'
				rotacion_t2 = '180I'
			elif ref == 'derecha': #Caso pix4d
				esquina = 'SO'
				rotacion_t1 = '0'
				rotacion_t2 = '180D'
		elif (L_signo[cont_signo-1] == '-') and (strx == 'lon'):
			if ref == 'abajo': #Caso posibles
				esquina = 'NE'
				rotacion_t1 = '90I'
				rotacion_t2 = '90D'
			elif ref == 'arriba': #Caso pix4d
				esquina = 'SE'
				rotacion_t1 = '90I'
				rotacion_t2 = '90D'
		elif (L_signo[cont_signo-1] == '-') and (strx == 'lat'):
			if ref == 'izquierda': #Caso pix4d
				esquina = 'NE'
				rotacion_t1 = '180D'
				rotacion_t2 = '0'
			elif ref == 'derecha': #Caso posibles
				esquina = 'NO'
				rotacion_t1 = '180I'
				rotacion_t2 = '0'
		'''print(esquina)
		print(rotacion_t1)
		print(rotacion_t2)'''
		return esquina,rotacion_t1,rotacion_t2,ref,L_signo[cont_signo-1]

	def Armar(self,all_metadata,cont_signo,L_signo,RelativeAltitude):
		esquina,rotacion_t1,rotacion_t2,ref,signo = self.banderas_mapa(all_metadata,cont_signo,L_signo)
		#cont_signo=0
		l_imgs=[]
		l_rotar=[]
		for cont,item in enumerate(sorted(glob.glob(self.path+'*.JPG'),key=os.path.getmtime)):
			img = Image.open(item)
			name = str(item)
			if platform == 'win32':
				name1 = name.split('\\')
			else:
				name1 = name.split('/')
			#Este es un modo de vuelo
			l_rotar.append(name1)
			if L_signo[cont] == '+' and rotacion_t1 == '90D' and esquina == 'NO':
				img = img.rotate(-90,expand=True)
				img.save(self.path+'rotacion/'+name1[-1])
			elif L_signo[cont] == '-' and rotacion_t2 == '90I' and esquina == 'NO':
				img = img.rotate(90,expand=True)
				img.save(self.path+'rotacion/'+name1[-1])
			#Termina
			#Este es un modo de vuelo
			elif L_signo[cont] == '+' and rotacion_t1 == '0' and esquina == 'SO':
				img.save(self.path+'rotacion/'+name1[-1])
			elif L_signo[cont] == '-' and rotacion_t2 == '180D' and esquina == 'SO':
				img = img.rotate(180,expand=True)
				img.save(self.path+'rotacion/'+name1[-1])
			#Termina
			#Este es un modo de vuelo
			elif L_signo[cont] == '-' and rotacion_t1 == '90I' and esquina == 'SE':
				img = img.rotate(90,expand=True)
				img.save(self.path+'rotacion/'+name1[-1])
			elif L_signo[cont] == '+' and rotacion_t2 == '90D' and esquina == 'SE':
				img = img.rotate(-90,expand=True)
				img.save(self.path+'rotacion/'+name1[-1])
			#Termina
			#Este es un modo de vuelo
			elif L_signo[cont] == '-' and rotacion_t1 == '180D' and esquina == 'NE':
				img = img.rotate(-180,expand=True)
				img.save(self.path+'rotacion/'+name1[-1])
			elif L_signo[cont] == '+' and rotacion_t2 == '0' and esquina == 'NE':
				img.save(self.path+'rotacion/'+name1[-1])
			#Termina
			img.close()
		for cont,item in enumerate(sorted(glob.glob(self.path+'rotacion/'+'*.JPG'),key=os.path.getmtime)):
			print(item)
			img = Image.open(item)
			l_imgs.append(self.cut_img(img,cont,'ImgsCut',high=RelativeAltitude))#Corta imagenes y las coloca en una lista
			img.close()
			
		self.resizeador(RelativeAltitude)
		coordenadas = self.coordenadas(esquina,cont_signo,len(L_signo))
		return coordenadas,esquina

	def rotar(self,l1):
		print('Rota imagenes')
		l2 = []
		for i in range(0,len(l1)):
			l2.append(l1[(len(l1)-1)-i])
		return l2

	def coordenadas(self,esquina,cont_signo,area):
		lista_giros = []
		dicc_pos = {} #Imagen,poscicion
		ancho = cont_signo
		alto = int(area/ancho)
							#comienzo, final,     saltos 
		for giros in range(0,int(alto*ancho),cont_signo):
			lista_giros.append(giros)
		print(lista_giros)
		lista_orden = []
		############
		# VUELO1
		############
		if esquina == 'NO':
			for index,giro in enumerate(lista_giros):
				if ((giro%2) == 0):
					for cont_tiras in range(giro,cont_signo+giro):
						lista_orden.append(cont_tiras)
				elif ((giro%2) == 1):
					for cont_tiras in range(giro,(cont_signo+giro)):
						lista_orden.append((cont_signo+giro)-(cont_tiras-(giro-1)))
			cont = 0
			for y in range(alto):
				for x in range(ancho):
					dicc_pos[lista_orden[cont]] = [x,y]
					cont = cont + 1
		#############
		# VUELO 2
		############
		elif esquina == 'SO':
			for index,giro in enumerate(lista_giros):
				if ((giro%2) == 0):
					lista_orden.append([cont_tiras for cont_tiras in range(giro,cont_signo+giro)])
				elif ((giro%2) == 1):
					lista_orden.append([((cont_signo+giro)-(cont_tiras-(giro-1))) for cont_tiras in range(giro,cont_signo+giro)])
			matriz = np.array(lista_orden,int)
			matriz = np.rot90(matriz)
			for y in range(alto):
				for x in range(ancho):
					dicc_pos[matriz[x][y]] = [y,x]
		#############
		# VUELO 3
		############
		elif esquina == 'SE':
			lista_giros = self.rotar(lista_giros)
			for index,giro in enumerate(lista_giros):
				if ((giro%2) == 1):
					for cont_tiras in range(giro,cont_signo+giro):
						lista_orden.append(cont_tiras)
				elif ((giro%2) == 0):
					for cont_tiras in range(giro,(cont_signo+giro)):
						lista_orden.append((cont_signo+giro)-(cont_tiras-(giro-1)))
			cont = 0
			#print("Lista orden aqui es la clave: ",lista_orden)
			#print("Dimension de la Lista orden: ",len(lista_orden))
			for y in range(alto):
				for x in range(ancho):
					dicc_pos[lista_orden[cont]] = [x,y]
					cont = cont + 1
		#############
		# VUELO 4
		############
		if esquina == 'NE':
			for index,giro in enumerate(lista_giros):
				if ((giro%2) == 0):
					lista_orden.append([cont_tiras for cont_tiras in range(giro,cont_signo+giro)])
				elif ((giro%2) == 1):
					lista_orden.append([((cont_signo+giro)-(cont_tiras-(giro-1))) for cont_tiras in range(giro,cont_signo+giro)])
			matriz = np.array(lista_orden,int)
			matriz = np.rot90(matriz,k=3)
			for y in range(alto):
				for x in range(ancho):
					dicc_pos[matriz[x][y]] = [y,x]
		return dicc_pos

	def ExtraerXMP(self, img):
		#print(img)
		with open(img,"rb") as fin:
			img = fin.read()
		imgAsString=str(img)
		soup = BeautifulSoup(imgAsString, 'html.parser')
		string = str(soup.find_all("rdf:description"))
		l=string.split()
		FYD = 'drone-dji:flightyawdegree='
		RA ='drone-dji:relativealtitude='
		#any(palabra in string for string in l)
		FYD_index = [(indice)for indice, string in enumerate(l) if FYD in string]
		FlyYawDegree = l[FYD_index[0]].split("\"")

		RA_index = [(indice)for indice, string in enumerate(l) if RA in string]
		ra = l[RA_index[0]].split("\"")
		#Se requieren establecer parametros debido a que los metadatos del dron no son exactos
		if float(ra[1]) < 15.0:
			RelativeAltitude = 2.0
			print('Must not enter here')
		else:
			RelativeAltitude = 30.0

		return RelativeAltitude,FlyYawDegree[1][0]
		########Old code
		"""xmpfile = XMPFiles( file_path = img, open_forupdate = True )
		xmp = xmpfile.get_xmp()
		lista_xmp = list(xmp) 

		for cont,xmp1 in enumerate(lista_xmp):
			if cont == 16:
				FlightYawDegree = lista_xmp[16][2]	
				continue

			if cont == 11:
				RelativeAltitude = lista_xmp[11][2]
				continue

		#Se requieren establecer parametros debido a que los metadatos del dron no son exactos
		if float(RelativeAltitude) < 15.0:
			RelativeAltitude = 2.0
		else:
			RelativeAltitude = 30.0

		return RelativeAltitude,lista_xmp[16][2][0]"""

	def haversine(self,lat1, lon1, lat2, lon2):
		rad=math.pi/180
		dlat=lat2-lat1
		dlon=lon2-lon1
		R=6372.795477598
		a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
		distancia=2*R*math.asin(math.sqrt(a))
		return distancia

	def dir_tiras(self,ref,l1,l3,l4):
		limg1 = l1
		limg2 = l3
		limg3 = l4
		latimg1 = limg1[0]
		latimg2 = limg2[0]
		latimg3 = limg3[0]
		lonimg1 = limg1[1]
		lonimg2 = limg2[1]
		lonimg3 = limg3[1]
		dist1 = self.haversine(latimg1,lonimg1,latimg2,lonimg2)
		dist2 = self.haversine(latimg1,lonimg1,latimg3,lonimg3)
		strc = ""
		if dist2 > dist1:
			strc = 'CE'
		else:
			#print("NO Es contraesquina")
			strc = 'NCE'
		if ref == 'lon':
			y1 = 90 - abs(latimg1)
			y2 = 90 - abs(latimg2)
			if strc == 'NCE':
				if y1 > y2:
					return "arriba",strc #Ubicado arriba, y Pegar hacia abajo 
				else:
					return "abajo",strc
			else:
				if y1 > y2:
					return "arriba",strc #Ubicado arriba, y Pegar hacia abajo 
				else:
					return "abajo",strc
		elif ref == 'lat':
			x1 = 180 - abs(lonimg1)
			x2 = 180 - abs(lonimg2)
			if strc == 'NCE':
				if x1 > x2:
					return "izquierda",strc #Ubicado a la izquierda Y Pegar hacia la DERECHA
				else:
					return "derecha",strc
			else:
				if x1 > x2:
					return "izquierda",strc #Ubicado a la izquierda Y Pegar hacia la DERECHA
				else:
					return "derecha",strc

	def dir_name(self,path):
		self.path = path
	def dir_name_imgsCrudas(self,ruta_crudas):
		self.path_crudas = ruta_crudas
	def __init__(self,path):
		print('Start')
		self.path = path
