# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaInicio.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QBasicTimer
from View.VistaMapa import Ui_VistaMapa
from View.V_Chooser import Ui_TrainFiles
from Model.TT_modelo_RNC import TT_modelo_RNC
from Model.TT_modelo_RNC30 import TT_modelo_RNC30
#from Modelo.RedAreasVerdes import TT_modelo_RNC30
from sys import platform
from bs4 import BeautifulSoup
import numpy as np
#from libxmp import XMPFiles #We replace this library for BeatifulSoup
from PIL import Image,ImageOps,ImageDraw
import os
import glob
import pickle
from PyQt5.QtWidgets import QMessageBox

class Ui_VistaInicial(QWidget):
    def __init__(self,modelo): #Se envia como parametro el modelo, para que sea una variable de clase y se puedan utilizar sus metodos.
        self.modelo = modelo
        """El contructor manda hereda los metodos de clase cuando esta se instancie,
           además manda a llamar el setupUi, que es donde se albergan los metodos (cicket) 
           o señales y todos los estilos de que se presentarán en la ventana."""
        super().__init__()
        self.setupUi(self)

    def setupUi(self, VistaInicial):
        """Todo el estilo necesario y señales en los botones, boton self.V1F3B1_Enviar.setEnabled(False)
           inicia en False para que no se ejecute nada."""
        VistaInicial.setObjectName("VistaInicial")
        VistaInicial.resize(640, 310)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        VistaInicial.setFont(font)
        VistaInicial.setAccessibleDescription("")
        VistaInicial.setAutoFillBackground(False)
        VistaInicial.setStyleSheet("background-color: rgb(216, 223, 234);")
        VistaInicial.setWindowFilePath("")
        #VistaInicial.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(VistaInicial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.V1F1 = QtWidgets.QFrame(self.centralwidget)
        self.V1F1.setGeometry(QtCore.QRect(0, 0, 641, 71))
        self.V1F1.setAutoFillBackground(False)
        self.V1F1.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V1F1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V1F1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.V1F1.setObjectName("V1F1")
        self.V1F1E1_Titulo = QtWidgets.QLabel(self.V1F1)
        self.V1F1E1_Titulo.setEnabled(True)
        self.V1F1E1_Titulo.setGeometry(QtCore.QRect(136, 20, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V1F1E1_Titulo.setFont(font)
        self.V1F1E1_Titulo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.V1F1E1_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.V1F1E1_Titulo.setObjectName("V1F1E1_Titulo")

        self.V1F1B1_Cargar = QtWidgets.QPushButton(self.V1F1)
        self.V1F1B1_Cargar.setEnabled(True)
        self.V1F1B1_Cargar.setGeometry(QtCore.QRect(180, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V1F1B1_Cargar.setFont(font)
        self.V1F1B1_Cargar.setMouseTracking(True)
        self.V1F1B1_Cargar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.V1F1B1_Cargar.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V1F1B1_Cargar.setObjectName("V1F1B1_Cargar")

        self.V1F1B2_Nuevo = QtWidgets.QPushButton(self.V1F1)
        self.V1F1B2_Nuevo.setEnabled(True)
        self.V1F1B2_Nuevo.setGeometry(QtCore.QRect(310, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V1F1B2_Nuevo.setFont(font)
        self.V1F1B2_Nuevo.setMouseTracking(True)
        self.V1F1B2_Nuevo.setFocusPolicy(QtCore.Qt.TabFocus)
        self.V1F1B2_Nuevo.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V1F1B2_Nuevo.setObjectName("V1F1B2_Nuevo")

        self.V1F2 = QtWidgets.QFrame(self.centralwidget)
        self.V1F2.setGeometry(QtCore.QRect(0, 70, 641, 80))
        self.V1F2.setAutoFillBackground(False)
        self.V1F2.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V1F2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V1F2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V1F2.setObjectName("V1F2")
        self.V1F2E1_Ingresa = QtWidgets.QLabel(self.V1F2)
        self.V1F2E1_Ingresa.setEnabled(True)
        self.V1F2E1_Ingresa.setGeometry(QtCore.QRect(40, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E1_Ingresa.setFont(font)
        self.V1F2E1_Ingresa.setObjectName("V1F2E1_Ingresa")
        self.V1F2B1_Directorio = QtWidgets.QPushButton(self.V1F2)
        self.V1F2B1_Directorio.setGeometry(QtCore.QRect(530, 20, 51, 27))
        self.V1F2B1_Directorio.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V1F2B1_Directorio.setFont(font)
        self.V1F2B1_Directorio.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V1F2B1_Directorio.setObjectName("V1F2B1_Directorio")
        self.V1F2E2_Path = QtWidgets.QLabel(self.V1F2)
        self.V1F2E2_Path.setGeometry(QtCore.QRect(150, 20, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E2_Path.setFont(font)
        self.V1F2E2_Path.setAlignment(QtCore.Qt.AlignCenter)
        self.V1F2E2_Path.setObjectName("V1F2E2_Path")
        self.V1F3 = QtWidgets.QFrame(self.centralwidget)
        self.V1F3.setGeometry(QtCore.QRect(190, 160, 261, 141))
        self.V1F3.setAutoFillBackground(False)
        self.V1F3.setStyleSheet("background-color: rgb(216, 223, 234);\n"
"border: rgb(216, 223, 234);")
        self.V1F3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V1F3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V1F3.setObjectName("V1F3")
        self.V1F3B1_Enviar = QtWidgets.QPushButton(self.V1F3)
        self.V1F3B1_Enviar.setEnabled(False)
        self.V1F3B1_Enviar.setGeometry(QtCore.QRect(60, 40, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V1F3B1_Enviar.setFont(font)
        self.V1F3B1_Enviar.setMouseTracking(True)
        self.V1F3B1_Enviar.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V1F3B1_Enviar.setObjectName("V1F3B1_Enviar")

        self.V1Chooser = QtWidgets.QComboBox(self.V1F3)
        self.V1Chooser.setGeometry(QtCore.QRect(0, 0, 261, 26))
        self.V1Chooser.setObjectName("V1Chooser")
        self.V1Chooser.setEnabled(False)

        self.V1F3B1_ReTrain = QtWidgets.QPushButton(self.centralwidget)
        self.V1F3B1_ReTrain.setEnabled(True)
        self.V1F3B1_ReTrain.setGeometry(QtCore.QRect(510, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V1F3B1_ReTrain.setFont(font)
        self.V1F3B1_ReTrain.setMouseTracking(True)
        self.V1F3B1_ReTrain.setStyleSheet("font: 16pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V1F3B1_ReTrain.setObjectName("V1F3B1_ReTrain")
        #self.progressBar = QtWidgets.QProgressBar(self.V1F3)
        #self.progressBar.setGeometry(QtCore.QRect(10, 110, 241, 23))
        #self.progressBar.setStyleSheet("background-color: rgb(216, 223, 234);\n"
#"border:rgb(1, 118, 180);")
        #self.progressBar.setProperty("value", 0)
        #self.progressBar.setObjectName("progressBar")
        #self.timer = QBasicTimer()
        #self.step = 0
        #VistaInicial.setCentralWidget(self.centralwidget)

        self.retranslateUi(VistaInicial)
        QtCore.QMetaObject.connectSlotsByName(VistaInicial)
        VistaInicial.setTabOrder(self.V1F2B1_Directorio, self.V1F3B1_Enviar)

        self.V1F2B1_Directorio.clicked.connect(self.up_filechooser)
        self.V1F3B1_Enviar.clicked.connect(self.child_window)
        self.V1F1B1_Cargar.clicked.connect(self.child_window_cargar)
        self.V1F1B2_Nuevo.clicked.connect(self.change_button_status_nuevo)
        self.V1F3B1_ReTrain.clicked.connect(self.child_retrain)
        self.V1Chooser.currentIndexChanged.connect(self.getItem)

    def retranslateUi(self, VistaInicial):
        """Se ejecuta código HTML para agregarle estilo a las ventanas de PyQT"""
        _translate = QtCore.QCoreApplication.translate
        VistaInicial.setWindowTitle(_translate("VistaInicial", "Main window"))
        self.V1F1E1_Titulo.setText(_translate("VistaInicial", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\"></span></p></body></html>"))
        self.V1F1B1_Cargar.setText(_translate("VistaInicial", "Load"))
        self.V1F1B2_Nuevo.setText(_translate("VistaInicial", "New"))
        self.V1F2E1_Ingresa.setText(_translate("VistaInicial", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Directory:</span></p></body></html>"))
        self.V1F2B1_Directorio.setText(_translate("VistaInicial", "..."))
        self.V1F2E2_Path.setText(_translate("VistaInicial", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"></span></p></body></html>"))
        self.V1F3B1_Enviar.setText(_translate("VistaInicial", "Submit"))
        self.V1F3B1_ReTrain.setText(_translate("VistaInicial", "Re-Train"))

    def child_retrain(self):
        self.V1F2B1_Directorio.setEnabled(True)
        self.V1F1B1_Cargar.setEnabled(False)
        self.V1F1B2_Nuevo.setEnabled(False)

        self.retrain = Ui_TrainFiles(self.V1F1B1_Cargar,self.V1F1B2_Nuevo,self.V1Chooser)
        self.change_button_status()
        self.retrain.show()
        #self.destroy()

    def child_window(self):#Tambien agregar que este boton ejecutará TOOOOOOOOOOOOODOOOOOOOOOOOOOOOO
        """Aquí intancialos la clase de la segunda ventana y le mandamos los dos botones como paráme
           tros debido a que es una ventana hija de esta, y la lógica es que cuando se levante la se
           gunda ventana, se bloquearán los botones de la primer ventana, posiblemente, se tenga agr
           eguen las labels para que se limpie. La intencion es que el contructor reciba los botones
           y le permita a la ventana hija manipular las cosas de la ventana padre."""

        with open(self.imagen,"rb") as fin:
            img = fin.read()
        imgAsString=str(img)
        soup = BeautifulSoup(imgAsString, 'html.parser')
        string = str(soup.find_all("rdf:description"))
        l=string.split()
        FlyYawDegree = l[12].split("=")
        #print(FlyYawDegree)
        if (FlyYawDegree[0] == 'drone-dji:flightyawdegree'):
            #print('Imagen de la familia DJI')                
            self.all_back(self.directorio)
            alto = self.img_sin_cortar/self.cont_signo
            #print(self.img_sin_cortar)

            self.ui = Ui_VistaMapa(self.V1F2E2_Path,self.V1F1B2_Nuevo,self.V1F1B1_Cargar,self.cont_signo,int(alto),self.img_sin_cortar,self.etiquetas,self.RelativeAltitude,self.all_metadata,self.signo_capital,self.directorio,self.dicc_pos,self.ref,self.dic_aux) #Se le pasarán los botones, los labels para actualizar, y el path 
            self.change_button_status() #Bloqueo de botones
            self.ui.show()
        else:
            #print('Error: Imagen no reconocida')
            QMessageBox.critical(self, "Error", "The input images do not belong to the DJI family, select valid images.")

    def child_window_cargar(self):
        
        self.V1F1B2_Nuevo.setEnabled(False)#Se desabilita el boton de "Nuevo"
        archivo = self.up_filechooser_cargar()#Se levanta un nuevo fileChooser que busca los archivos con extensión ".pickle" 
        if archivo != None:
            datos = pickle.load(open(archivo,'rb'))# Se cargan los archivos que contienen la extensión ".pickle" para obtener 
                                                    #los datos para instanciar de nuevo la ventana de "VistaMapa"
                                                                                        #ancho,    alto, imgs_sin_cortar,etiquetas,altura,all_metadata,signo_capital,directorio,dicc_pos,ref
            self.ui = Ui_VistaMapa(self.V1F2E2_Path,self.V1F1B2_Nuevo,self.V1F1B1_Cargar,datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10])
            self.change_button_status()#Se desactivan todos los botones
            self.ui.show()
        else: pass

    def change_button_status(self):
        """Cambio de estado en los botones"""
        self.V1F3B1_Enviar.setEnabled(False)
        self.V1F2B1_Directorio.setEnabled(False)
        self.V1F1B1_Cargar.setEnabled(False)
        self.V1F1B2_Nuevo.setEnabled(False)
        self.V1Chooser.setEnabled(False)


    def change_button_status_nuevo(self):
        self.V1F2B1_Directorio.setEnabled(True)
        self.V1F1B1_Cargar.setEnabled(False)
        self.V1F1B2_Nuevo.setEnabled(False)

    def showing(self):
        """Muestra la ventana, es un metodo para que se ejecute una sola vez."""
        self.show()

    def up_filechooser(self):
        """Levantamos el file chooser, cuando se de aceptar en la ventana del
           FileChooser, este mostrará en la etiqueta path, el path del direct
           orio de imágenes, y aquí solo guararemos el path de la carpte."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose file .JPG", "","JPG files (*.JPG);;Images files (*.JPG)", options=options)
        _translate = QtCore.QCoreApplication.translate #Permite ejecutar código html a pyqt
        self.imagen =fileName
        if fileName:
            self.V1F3B1_Enviar.setEnabled(True) #SE CAMBIA EL ESTADO INICIAL.
            #Se requiere obtener el directorio que contiene a la imagen que se esta seleccionando para así tener un "path"
            #del que se obtendrán todas las imagenes y pasarlo al modelo
            #para este fin se analiza la plataforma en la que se esta corriendo el programa ya que en sistemas UNIX
            #se construyen los paths de manera distinta a los sistemas basados en windows 
            if platform == "linux" or platform == "linux2":
                self.directorio = os.path.dirname(fileName)
                self.V1F2E2_Path.setText(_translate("VistaInicial", "<html><head/><body><p><span style=\" color:#ffffff;\">"+self.directorio+"</span></p></body></html>"))
                self.directorio = self.directorio + '/'
            elif platform == "darwin":
                self.directorio = os.path.dirname(fileName)
                self.V1F2E2_Path.setText(_translate("VistaInicial", "<html><head/><body><p><span style=\" color:#ffffff;\">"+self.directorio+"</span></p></body></html>"))
                self.directorio = self.directorio + '/'
            elif platform == "win32":
                self.directorio = os.path.dirname(fileName)
                self.V1F2E2_Path.setText(_translate("VistaInicial", "<html><head/><body><p><span style=\" color:#ffffff;\">"+self.directorio+"</span></p></body></html>"))
                self.directorio = self.directorio + '/'
            items = os.listdir("./Model/Nets/")
            if platform == "darwin":
                index_del = items.index('.DS_Store')
                del(items[index_del])
            self.V1Chooser.addItems(items)
            self.V1Chooser.setEnabled(True)
            self.V1F3B1_Enviar.setEnabled(True)
        else:
            pass

    def getItem(self):
        self.opcNet = "./Model/Nets/" + self.V1Chooser.currentText()
        print(self.opcNet)
    def up_filechooser_cargar(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose file .pickle", "","Pickle files (*.p);;Serialized files (*.p)", options=options)
        if fileName:
            _translate = QtCore.QCoreApplication.translate #Permite ejecutar código html a pyqt
            self.V1F2E2_Path.setText(_translate("VistaInicial", "<html><head/><body><p><span style=\" color:#ffffff;\">"+fileName+"</span></p></body></html>"))
           #Se coloca todo en el label en donde va el path 
            return fileName
        else:
            pass

    def all_back(self,directorio):
        """Esta función ejecutará todo lo del módelo1 que se ha instanciado desde el main, su deber es
           cambiar el path que es una variable de clase con el primer metodo, y a continuacion se ejec
           utan, los metodos en el orden que ya se habia definido."""
        self.currentDir = self.V1Chooser.currentText()
        if self.currentDir == 'OriginalNet':
            self.path_pesos = './Model/Nets/OriginalNet/Pesos/AreaVerde30m.ckpt'
        else:
            files = glob.glob('./Model/Nets/'+self.currentDir+'/Pesos/*')
            self.path_pesos = './Model/Nets/'+self.V1Chooser.currentText()+'/Pesos/Pesos.ckpt'
            print(self.path_pesos)

        self.modelo.dir_name(directorio)
        print('VistaInicial: antes de preprocesamiento')
        self.all_metadata,self.RelativeAltitude,self.cont_signo, self.signo_capital,self.L_signo,self.date = self.modelo.all_renamerGPS_data()
        self.dicc_pos,self.ref = self.modelo.Armar(self.all_metadata,self.cont_signo,self.L_signo,self.RelativeAltitude)
        print('VistaInicial: despues de preprocesamiento')
        dim = self.modelo.MakePickle(self.RelativeAltitude,self.dicc_pos)
        if self.RelativeAltitude == 30 and self.currentDir == 'OriginalNet':
            self.etiquetas = []
            self.img_sin_cortar = len(glob.glob(directorio +'*.JPG'))
            #print(self.img_sin_cortar)
            #print('Start propagation')
            self.dic_aux = {}
            for k,v in self.dicc_pos.items():
                print(k)
                print(self.directorio+'pickle/pickle_'+str(k))
                clase_arquitectura = TT_modelo_RNC30(300,self.directorio+'pickle/pickle_'+str(k),
                self.path_pesos)
                l = clase_arquitectura.propagacion(self.currentDir)
                self.dic_aux[k] = list(l[0])
                self.etiquetas.append(list(l[0]))
                del clase_arquitectura
        else:
            self.etiquetas = []
            self.img_sin_cortar = len(glob.glob(directorio +'*.JPG'))
            #print(self.img_sin_cortar)
            #print('Start propagation')
            self.dic_aux = {}
            print(self.dicc_pos)
            for k,v in self.dicc_pos.items():
                print(k)
                print(self.directorio+'pickle/pickle_'+str(k))
                clase_arquitectura = TT_modelo_RNC30(300,self.directorio+'pickle/pickle_'+str(k),
                self.path_pesos)
                l = clase_arquitectura.propagacion(self.currentDir)
                self.dic_aux[k] = list(l[0])
                self.etiquetas.append(list(l[0]))
                del clase_arquitectura #Aqui estuvo la arquitectura de la red de 2m

        #N_dir = directorio.split('/')
        dir_new = directorio
        os.rename(dir_new[:-1],dir_new[:-1] + '_' + str(self.date)+ '/')
        self.directorio = dir_new[:-1] + '_' + str(self.date)+ '/'
        self.coloreaImagen()


    def coloreaImagen(self):
        list_tags = []
        dic_colores = {0:[109,199,42],1:[255,236,0],2:[251,153,0],3:[158,158,158], #colors 
               4:[112,139,39],5:[250,89,1],6:[165,111,9],7:[98,126,140]}  #con contaminación

        for cont in range(len(self.dicc_pos)):
            img_org = Image.open(self.directorio+'rotacion/'+str(cont)+'.JPG')

            list_tags = self.etiquetas[cont]

            self_cont = 0

            if self.ref == 'NO' or self.ref == 'SE':
                img_colors = np.zeros((4000,3000,3),dtype=np.uint8) #white
                for w_b in range(0,4000,200):
                    for h_b in range(0,3000,200):
                        for w in range (w_b,w_b+200):
                            for h in range(h_b,h_b+200):
                                img_colors[w,h] = dic_colores[list_tags[self_cont]]
                        self_cont = self_cont + 1
            else:
                img_colors = np.zeros((3000,4000,3),dtype=np.uint8) #white
                for w_b in range(0,3000,200):
                    for h_b in range(0,4000,200):
                        for w in range (w_b,w_b+200):
                            for h in range(h_b,h_b+200):
                                img_colors[w,h] = dic_colores[list_tags[self_cont]]
                        self_cont = self_cont + 1
            img = Image.fromarray(img_colors, 'RGB')
            #img.save(self.directorio+'ImgsBlended/'+str(cont)+'_mask.JPG')
            print('Contador de colorea imagen'+str(cont))
            out = Image.blend(Image.open(self.directorio+'rotacion/'+str(cont)+'.JPG'),img,0.5)
            out.save(self.directorio+'ImgsBlended/'+str(cont)+'_blended.JPG')  


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_VistaInicial()
    sys.exit(app.exec_())