
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaMapa.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QAction,qApp
from PyQt5.QtGui import QIcon, QPixmap
import secrets
import pickle
import numpy as np
import glob
from View.VistaDatos import Ui_Grafica
from View.VistaBlended import Ui_Blended
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import collections
from PyQt5.QtCore import *
from sys import platform
from PyQt5 import QtWebEngineWidgets
from PIL import Image

class Ui_VistaMapa(QWidget):
    def __init__(self,etiqueta_path,boton_nuevo,boton_cargar,ancho,alto,imgs_sin_cortar,etiquetas,altura,all_metadata,signo_capital,directorio,dicc_pos,ref,dicc_aux,guardado=False):
        #Se reciben los botones de los cuales se desea cambiar su valor.
        self.guardado = guardado
        self.imgs_sin_cortar = imgs_sin_cortar #Este nos dice el numero total de imagenes dentro de la carpeta para los fors del grid
        self.etiquetas = etiquetas #lista del argmax de las propagaciones que hace la red
        self.etiqueta_path = etiqueta_path #Es la label donde se escribe la ruta de la carpeta del dron
        self.button_3 = boton_nuevo #botones para activar la ventana padre 
        self.button_4 = boton_cargar #botones ***
        self.ancho = ancho #de cuantas imagenes a lo ancho
        self.alto = alto #de cuantas imagenes a lo alto
        self.altura = altura #altura para generar grid de botones
        self.all_metadata = all_metadata #metadatos de cada imagen padre
        self.signo_capital = signo_capital #este dira como pegar las imagenes
        self.directorio = directorio #Aqui es la ruta donde hasta donde estan las imaganes del dron
        self.dicc_pos = dicc_pos
        self.ref = ref
        self.dicc_aux = dicc_aux
        super().__init__()
        self.setupUi(self)
        self.valores_analisis(self.etiquetas)
        self.img_big = Ui_Blended(self.directorio)

    def setupUi(self, VistaMapa):
        VistaMapa.setObjectName("VistaMapa")
        VistaMapa.resize(1241, 741)
        VistaMapa.setStyleSheet("background-color: rgb(216, 223, 234);")
        self.centralwidget = QtWidgets.QWidget(VistaMapa)
        self.centralwidget.setObjectName("centralwidget")
        self.V1SB1_Mapa = QtWidgets.QScrollArea(self.centralwidget)
        self.V1SB1_Mapa.setGeometry(QtCore.QRect(10, 100, 851, 521))
        self.V1SB1_Mapa.setStyleSheet("background-color: rgb(242, 239, 241);")
        self.V1SB1_Mapa.setWidgetResizable(True)
        self.V1SB1_Mapa.setObjectName("V1SB1_Mapa")
        self.V1S1_Mapa = QtWidgets.QWidget()
        self.V1S1_Mapa.setGeometry(QtCore.QRect(0, 0, 849, 519))
        self.V1S1_Mapa.setObjectName("V1S1_Mapa")
        self.gridLayoutWidget = QtWidgets.QWidget(self.V1S1_Mapa)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 851, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.imgs = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.imgs.setContentsMargins(0, 0, 0, 0)
        self.imgs.setObjectName("imgs")
        self.pedazos_imgs = QtWidgets.QGridLayout()
        self.pedazos_imgs.setObjectName("pedazos_imgs")
        self.imgs.addLayout(self.pedazos_imgs, 0, 0, 1, 1)
        self.V1SB1_Mapa.setWidget(self.V1S1_Mapa)
        self.V2F2 = QtWidgets.QFrame(self.centralwidget)
        self.V2F2.setGeometry(QtCore.QRect(870, 100, 361, 221))
        self.V2F2.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V2F2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V2F2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V2F2.setObjectName("V2F2")
        self.V2F2E2_ImgZoom = QtWidgets.QLabel(self.V2F2)
        self.V2F2E2_ImgZoom.setGeometry(QtCore.QRect(90, 10, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F2E2_ImgZoom.setFont(font)
        self.V2F2E2_ImgZoom.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V2F2E2_ImgZoom.setObjectName("V2F2E2_ImgZoom")
        self.V2F3 = QtWidgets.QFrame(self.centralwidget)
        self.V2F3.setGeometry(QtCore.QRect(870, 330, 361, 291))
        self.V2F3.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V2F3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V2F3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V2F3.setObjectName("V2F3")
        self.VistaGoogleMaps = QtWebEngineWidgets.QWebEngineView(self.V2F3)
        self.VistaGoogleMaps.setGeometry(QtCore.QRect(10, 10, 341, 271))
        self.VistaGoogleMaps.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.VistaGoogleMaps.setUrl(QtCore.QUrl("about:blank"))
        self.VistaGoogleMaps.setObjectName("VistaGoogleMaps")
        self.V2F4 = QtWidgets.QFrame(self.centralwidget)
        self.V2F4.setGeometry(QtCore.QRect(870, 630, 181, 101))
        self.V2F4.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V2F4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V2F4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V2F4.setObjectName("V2F4")
        self.V2F4E1_DCoordenadas = QtWidgets.QLabel(self.V2F4)
        self.V2F4E1_DCoordenadas.setGeometry(QtCore.QRect(20, 10, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F4E1_DCoordenadas.setFont(font)
        self.V2F4E1_DCoordenadas.setObjectName("V2F4E1_DCoordenadas")
        self.V2F4E2_DLat = QtWidgets.QLabel(self.V2F4)
        self.V2F4E2_DLat.setGeometry(QtCore.QRect(10, 40, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F4E2_DLat.setFont(font)
        self.V2F4E2_DLat.setObjectName("V2F4E2_DLat")
        self.V2F4E3_DLon = QtWidgets.QLabel(self.V2F4)
        self.V2F4E3_DLon.setGeometry(QtCore.QRect(10, 60, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F4E3_DLon.setFont(font)
        self.V2F4E3_DLon.setObjectName("V2F4E3_DLon")
        self.V2F4E4_Lat = QtWidgets.QLabel(self.V2F4)
        self.V2F4E4_Lat.setGeometry(QtCore.QRect(80, 40, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F4E4_Lat.setFont(font)
        self.V2F4E4_Lat.setObjectName("V2F4E4_Lat")
        self.V2F4E5_Lon = QtWidgets.QLabel(self.V2F4)
        self.V2F4E5_Lon.setGeometry(QtCore.QRect(80, 60, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F4E5_Lon.setFont(font)
        self.V2F4E5_Lon.setObjectName("V2F4E5_Lon")
        self.V2F4E3_DAlt = QtWidgets.QLabel(self.V2F4)
        self.V2F4E3_DAlt.setGeometry(QtCore.QRect(10, 80, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F4E3_DAlt.setFont(font)
        self.V2F4E3_DAlt.setObjectName("V2F4E3_DAlt")
        self.V2F4E5_Alt = QtWidgets.QLabel(self.V2F4)
        self.V2F4E5_Alt.setGeometry(QtCore.QRect(80, 80, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F4E5_Alt.setFont(font)
        self.V2F4E5_Alt.setObjectName("V2F4E5_Alt")
        self.V2F1 = QtWidgets.QFrame(self.centralwidget)
        self.V2F1.setGeometry(QtCore.QRect(10, 20, 1221, 71))
        self.V2F1.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V2F1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V2F1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V2F1.setObjectName("V2F1")
        self.V2F1E1_Titulo = QtWidgets.QLabel(self.V2F1)
        self.V2F1E1_Titulo.setGeometry(QtCore.QRect(140, 10, 911, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F1E1_Titulo.setFont(font)
        self.V2F1E1_Titulo.setObjectName("V2F1E1_Titulo")
        
        self.pushButton = QtWidgets.QPushButton(self.V2F1)
        self.pushButton.setGeometry(QtCore.QRect(1100, 10, 60, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon(QPixmap('./View/Logo.png')))
        self.pushButton.setIconSize(QtCore.QSize(60,60))

        self.Big_img = QtWidgets.QPushButton(self.V2F1)
        self.Big_img.setGeometry(QtCore.QRect(20, 20, 101, 32))
        self.Big_img.setMouseTracking(True)
        self.Big_img.setTabletTracking(True)
        self.Big_img.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Big_img.setAcceptDrops(True)
        self.Big_img.setStyleSheet("background-color: rgb(242, 239, 241);")
        self.Big_img.setAutoDefault(True)
        self.Big_img.setDefault(True)
        self.Big_img.setFlat(True)
        self.Big_img.setObjectName("Big_img")
        
        self.V2F6 = QtWidgets.QFrame(self.centralwidget)
        self.V2F6.setGeometry(QtCore.QRect(10, 630, 851, 101))
        self.V2F6.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V2F6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V2F6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V2F6.setObjectName("V2F6")
        self.V2F6E8_TNS = QtWidgets.QLabel(self.V2F6)
        self.V2F6E8_TNS.setGeometry(QtCore.QRect(70, 50, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E8_TNS.setFont(font)
        self.V2F6E8_TNS.setObjectName("V2F6E8_TNS")
        self.V2F6E6_TSA = QtWidgets.QLabel(self.V2F6)
        self.V2F6E6_TSA.setGeometry(QtCore.QRect(70, 10, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E6_TSA.setFont(font)
        self.V2F6E6_TSA.setObjectName("V2F6E6_TSA")
        self.V2F6E3_TSEV = QtWidgets.QLabel(self.V2F6)
        self.V2F6E3_TSEV.setGeometry(QtCore.QRect(210, 30, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E3_TSEV.setFont(font)
        self.V2F6E3_TSEV.setObjectName("V2F6E3_TSEV")
        self.V2F6E9_TNSV = QtWidgets.QLabel(self.V2F6)
        self.V2F6E9_TNSV.setGeometry(QtCore.QRect(210, 50, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E9_TNSV.setFont(font)
        self.V2F6E9_TNSV.setObjectName("V2F6E9_TNSV")
        self.V2F6E7_TSAV = QtWidgets.QLabel(self.V2F6)
        self.V2F6E7_TSAV.setGeometry(QtCore.QRect(210, 10, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E7_TSAV.setFont(font)
        self.V2F6E7_TSAV.setObjectName("V2F6E7_TSAV")
        self.V2F6E8_TNP = QtWidgets.QLabel(self.V2F6)
        self.V2F6E8_TNP.setGeometry(QtCore.QRect(70, 70, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E8_TNP.setFont(font)
        self.V2F6E8_TNP.setObjectName("V2F6E8_TNP")
        self.V2F6E9_TNPV = QtWidgets.QLabel(self.V2F6)
        self.V2F6E9_TNPV.setGeometry(QtCore.QRect(210, 70, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E9_TNPV.setFont(font)
        self.V2F6E9_TNPV.setObjectName("V2F6E9_TNPV")
        self.V2F6E6_TSE = QtWidgets.QLabel(self.V2F6)
        self.V2F6E6_TSE.setGeometry(QtCore.QRect(70, 30, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E6_TSE.setFont(font)
        self.V2F6E6_TSE.setObjectName("V2F6E6_TSE")
        self.label = QtWidgets.QLabel(self.V2F6)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 17))
        self.label.setStyleSheet("background-color: rgb(109, 199, 42);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.V2F6)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 51, 17))
        self.label_2.setStyleSheet("background-color: rgb(255, 236, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.V2F6)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 51, 17))
        self.label_3.setStyleSheet("background-color: rgb(251, 153, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.V2F6)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 51, 17))
        self.label_4.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.label_4.setObjectName("label_4")
        self.V2F6E3_TSECV = QtWidgets.QLabel(self.V2F6)
        self.V2F6E3_TSECV.setGeometry(QtCore.QRect(630, 30, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E3_TSECV.setFont(font)
        self.V2F6E3_TSECV.setObjectName("V2F6E3_TSECV")
        self.V2F6E9_TNPCV = QtWidgets.QLabel(self.V2F6)
        self.V2F6E9_TNPCV.setGeometry(QtCore.QRect(630, 70, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E9_TNPCV.setFont(font)
        self.V2F6E9_TNPCV.setObjectName("V2F6E9_TNPCV")
        self.V2F6E9_TNSCV = QtWidgets.QLabel(self.V2F6)
        self.V2F6E9_TNSCV.setGeometry(QtCore.QRect(630, 50, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E9_TNSCV.setFont(font)
        self.V2F6E9_TNSCV.setObjectName("V2F6E9_TNSCV")
        self.V2F6E8_TNSC = QtWidgets.QLabel(self.V2F6)
        self.V2F6E8_TNSC.setGeometry(QtCore.QRect(390, 50, 221, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E8_TNSC.setFont(font)
        self.V2F6E8_TNSC.setObjectName("V2F6E8_TNSC")
        self.label_5 = QtWidgets.QLabel(self.V2F6)
        self.label_5.setGeometry(QtCore.QRect(330, 10, 51, 17))
        self.label_5.setStyleSheet("background-color: rgb(112, 139, 39);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.V2F6)
        self.label_6.setGeometry(QtCore.QRect(330, 50, 51, 17))
        self.label_6.setStyleSheet("background-color: rgb(165, 111, 9);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.V2F6)
        self.label_7.setGeometry(QtCore.QRect(330, 30, 51, 17))
        self.label_7.setStyleSheet("background-color: rgb(250, 89, 1);")
        self.label_7.setObjectName("label_7")
        self.V2F6E6_TSEC = QtWidgets.QLabel(self.V2F6)
        self.V2F6E6_TSEC.setGeometry(QtCore.QRect(390, 30, 221, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E6_TSEC.setFont(font)
        self.V2F6E6_TSEC.setObjectName("V2F6E6_TSEC")
        self.V2F6E8_TNPC = QtWidgets.QLabel(self.V2F6)
        self.V2F6E8_TNPC.setGeometry(QtCore.QRect(390, 70, 231, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E8_TNPC.setFont(font)
        self.V2F6E8_TNPC.setObjectName("V2F6E8_TNPC")
        self.V2F6E6_TSAC = QtWidgets.QLabel(self.V2F6)
        self.V2F6E6_TSAC.setGeometry(QtCore.QRect(390, 10, 221, 17))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.V2F6E6_TSAC.setFont(font)
        self.V2F6E6_TSAC.setObjectName("V2F6E6_TSAC")
        self.label_8 = QtWidgets.QLabel(self.V2F6)
        self.label_8.setGeometry(QtCore.QRect(330, 70, 51, 17))
        self.label_8.setStyleSheet("background-color: rgb(40, 126, 140);")
        self.label_8.setObjectName("label_8")
        self.V2F6E7_TSACV = QtWidgets.QLabel(self.V2F6)
        self.V2F6E7_TSACV.setGeometry(QtCore.QRect(630, 10, 61, 17))
        self.B_MasInfo = QtWidgets.QPushButton(self.V2F6)
        self.B_MasInfo.setGeometry(QtCore.QRect(710, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(12)
        self.B_MasInfo.setFont(font)
        self.B_MasInfo.setStyleSheet("background-color: rgb(242, 239, 241);")
        self.B_MasInfo.setObjectName("B_MasInfo")
        self.V2F6E7_TSACV.setFont(font)
        self.V2F6E7_TSACV.setObjectName("V2F6E7_TSACV")
        self.V2F6E8_TNS.raise_()
        self.V2F6E6_TSA.raise_()
        self.V2F6E3_TSEV.raise_()
        self.V2F6E9_TNSV.raise_()
        self.V2F6E7_TSAV.raise_()
        self.V2F6E8_TNP.raise_()
        self.V2F6E9_TNPV.raise_()
        self.V2F6E6_TSE.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.V2F6E3_TSECV.raise_()
        self.V2F6E9_TNPCV.raise_()
        self.V2F6E9_TNSCV.raise_()
        self.V2F6E8_TNSC.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.V2F6E6_TSEC.raise_()
        self.V2F6E8_TNPC.raise_()
        self.V2F6E6_TSAC.raise_()
        self.label_8.raise_()
        self.V2F6E7_TSACV.raise_()
        self.V2F5 = QtWidgets.QFrame(self.centralwidget)
        self.V2F5.setGeometry(QtCore.QRect(1060, 630, 171, 101))
        self.V2F5.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V2F5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V2F5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V2F5.setObjectName("V2F5")
        self.V2F2B1_NAnalisis = QtWidgets.QPushButton(self.V2F5)
        self.V2F2B1_NAnalisis.setGeometry(QtCore.QRect(30, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(12)
        self.V2F2B1_NAnalisis.setFont(font)
        self.V2F2B1_NAnalisis.setStyleSheet("background-color: rgb(242, 239, 241);")
        self.V2F2B1_NAnalisis.setObjectName("V2F2B1_NAnalisis")
        self.V2F2B1_NAnalisis.raise_()
        self.V2F2B1_NAnalisis.raise_()
        #VistaMapa.setCentralWidget(self.centralwidget)

        #######
        #menu Bar
        #######

        self.menuBar = QtWidgets.QMenuBar(VistaMapa)
        self.menuBar.setNativeMenuBar(False) #only for MacOS
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1240, 22))
        self.menuBar.setObjectName("menuBar")

        self.file_menu = self.menuBar.addMenu('&File')
        self.save_action = QAction('Save', VistaMapa)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.triggered.connect(self.guardar_como)
        self.file_menu.addAction(self.save_action)

        self.exit_action = QAction('Exit', VistaMapa)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.triggered.connect(qApp.quit)
        self.file_menu.addAction(self.exit_action)

        self.retranslateUi(VistaMapa)
        QtCore.QMetaObject.connectSlotsByName(VistaMapa)

        self.botones(self.ancho,self.alto,self.altura)

        self.show()

        self.V2F2B1_NAnalisis.clicked.connect(self.parent_window)

        self.B_MasInfo.clicked.connect(self.ventanaMasInfo)

        self.pushButton.clicked.connect(self.pagDeepDaemon)

        self.Big_img.clicked.connect(self.big_img_window)


    def retranslateUi(self, VistaMapa):
        _translate = QtCore.QCoreApplication.translate
        VistaMapa.setWindowTitle(_translate("VistaMapa", "Analyzer"))
        self.V2F2E2_ImgZoom.setText(_translate("VistaMapa", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">ZOOM image</span></p></body></html>"))
        self.V2F4E1_DCoordenadas.setText(_translate("VistaMapa", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">GPS Coordinates</span></p></body></html>"))
        self.V2F4E2_DLat.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Latitude: </span></p></body></html>"))
        self.V2F4E3_DLon.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Longitude:</span></p></body></html>"))
        self.V2F4E4_Lat.setText(_translate("VistaMapa", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">0.000000</span></p></body></html>"))
        self.V2F4E5_Lon.setText(_translate("VistaMapa", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">0.000000</span></p></body></html>"))
        self.V2F4E3_DAlt.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Altitude:</span></p></body></html>"))
        self.V2F4E5_Alt.setText(_translate("VistaMapa", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">0.000000</span></p></body></html>"))
        self.V2F1E1_Titulo.setText(_translate("VistaMapa", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">DeepGreenDiagnostics</span></p></body></html>"))
        self.V2F6E8_TNS.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Total Unhealthy (UNH):</span></p></body></html>"))
        self.V2F6E6_TSA.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Total Healthy (H):</span></p></body></html>"))
        self.V2F6E3_TSEV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.V2F6E9_TNSV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.V2F6E7_TSAV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.V2F6E8_TNP.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Total NO Veg (NV):</span></p></body></html>"))
        self.V2F6E9_TNPV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.V2F6E6_TSE.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Total Dry (D):</span></p></body></html>"))
        self.label.setText(_translate("VistaMapa", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("VistaMapa", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("VistaMapa", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("VistaMapa", "<html><head/><body><p><br/></p></body></html>"))
        self.V2F6E3_TSECV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.V2F6E9_TNPCV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.V2F6E9_TNSCV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.V2F6E8_TNSC.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Total Unhealthy Cont (UNHC):</span></p></body></html>"))
        self.label_5.setText(_translate("VistaMapa", "<html><head/><body><p><br/></p></body></html>"))
        self.label_6.setText(_translate("VistaMapa", "<html><head/><body><p><br/></p></body></html>"))
        self.label_7.setText(_translate("VistaMapa", "<html><head/><body><p><br/></p></body></html>"))
        self.V2F6E6_TSEC.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Total Dry Cont (DC):</span></p></body></html>"))
        self.V2F6E8_TNPC.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Total No Veg Cont (NVC):</span></p></body></html>"))
        self.V2F6E6_TSAC.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">Total Healthy Cont (HC):</span></p></body></html>"))
        self.label_8.setText(_translate("VistaMapa", "<html><head/><body><p><br/></p></body></html>"))
        self.V2F6E7_TSACV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.V2F2B1_NAnalisis.setText(_translate("VistaMapa", "New"))
        self.Big_img.setText(_translate("VistaMapa", "Details"))
        #self.pushButton.setText(_translate("VistaMapa", "DeepDaemon"))
        self.B_MasInfo.setText(_translate("VistaMapa", "More information"))

    def parent_window(self,VistaMapa):
        #Se utiliza cuando el usuario presiona "Nuevo_Analisis"
        #Los botones de la ventana 1 vuelven a estan habilitados
        _translate = QtCore.QCoreApplication.translate
        self.button_3.setEnabled(True)
        self.button_4.setEnabled(True)
        self.etiqueta_path.setText(_translate("VistaInicial", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\"></span></p></body></html>"))
        self.close()

    def pagDeepDaemon(self):
        driverLocation = './chromedriver'
        browser = webdriver.Chrome(driverLocation)
        browser.get('http://www.deepdaemon.org/')

    def valores_analisis(self,etiquetas):
        #Contadores sin contaminacion
        cont_SA = 0
        cont_SE = 0
        cont_NS = 0
        cont_NP = 0
        #Contadores con contaminacion
        cont_SAC = 0
        cont_SEC = 0
        cont_NSC = 0
        cont_NPC = 0
        _translate = QtCore.QCoreApplication.translate
        for lista in etiquetas:
            dicc = collections.Counter(lista)
            for k,v in dicc.items():
                if k == 0:
                    cont_SA = cont_SA + v
                    continue
                elif k == 1:
                    cont_SE = cont_SE + v
                    continue
                elif k == 2:
                    cont_NS = cont_NS + v
                    continue
                elif k == 3:
                    cont_NP = cont_NP + v
                    continue
                elif k == 4:
                    cont_SAC = cont_SAC + v
                    continue
                elif k == 5:
                    cont_SEC = cont_SEC + v
                    continue
                elif k == 6:
                    cont_NSC = cont_NSC + v
                    continue
                elif k == 7:
                    cont_NPC = cont_NPC + v
                    continue
            del dicc
        self.V2F6E7_TSAV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">"+str(cont_SA)+"</span></p></body></html>"))
        self.V2F6E3_TSEV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">"+str(cont_SE)+"</span></p></body></html>"))
        self.V2F6E9_TNSV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">"+str(cont_NS)+"</span></p></body></html>"))
        self.V2F6E9_TNPV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">"+str(cont_NP)+"</span></p></body></html>"))

        self.V2F6E7_TSACV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">"+str(cont_SAC)+"</span></p></body></html>"))
        self.V2F6E3_TSECV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">"+str(cont_SEC)+"</span></p></body></html>"))
        self.V2F6E9_TNSCV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">"+str(cont_NSC)+"</span></p></body></html>"))
        self.V2F6E9_TNPCV.setText(_translate("VistaMapa", "<html><head/><body><p><span style=\" color:#ffffff;\">"+str(cont_NPC)+"</span></p></body></html>"))

        totalEtiquetas = cont_SA + cont_SE + cont_NS + cont_NP + cont_SAC + cont_SEC + cont_NSC + cont_NPC 
        self.paramGraf = [ (cont_SA * 100)/totalEtiquetas , (cont_SE * 100)/totalEtiquetas , (cont_NS * 100)/totalEtiquetas , (cont_NP * 100)/totalEtiquetas ,
        (cont_SAC * 100)/totalEtiquetas , (cont_SEC * 100)/totalEtiquetas , (cont_NSC * 100)/totalEtiquetas , (cont_NPC * 100)/totalEtiquetas ]
        totalbio = cont_SA + cont_SAC + cont_SE + cont_SEC + cont_NS + cont_NSC
        self.perCon = (cont_SAC + cont_SEC + cont_NSC) * 100 / totalbio
        self.paramBio = [(cont_SA*100)/totalbio , (cont_SE*100)/totalbio , (cont_NS*100)/totalbio , (cont_SAC*100)/totalbio  , 
        (cont_SEC*100)/totalbio  , (cont_NSC*100)/totalbio]
        self.totalbiomas = (totalbio * 100) / totalEtiquetas
        #print(self.paramGraf)

    def ventanaMasInfo(self):
        self.masInfo = Ui_Grafica(self.paramGraf,self.all_metadata,self.alto,self.ancho,self.totalbiomas,self.perCon,self.paramBio)
        self.masInfo.show()

    def big_img_window(self,directorio):
        self.img_big.show()
        
    def calcular(self,lat,lon):
        latitud=lat
        longitud=lon
        html=self.localizacion(latitud,longitud)
        self.VistaGoogleMaps.setHtml(html)

    def guardar(self,guardado,name):

        if guardado == False:
            self.guardar_como
        else:
            #ancho,alto,imgs_sin_cortar,etiquetas,altura,all_metadata,signo_capital,directorio,dicc_pos,ref
            salvados = []
            salvados.append(self.ancho) # pos 0 - arg 3
            salvados.append(self.alto) # pos 1 - arg 4
            salvados.append(self.imgs_sin_cortar) #pos 2 - arg 5
            salvados.append(self.etiquetas) # pos 3 - arg 6
            salvados.append(self.altura) # pos 4 - arg 7
            salvados.append(self.all_metadata) # pos 5 - arg 8
            salvados.append(self.signo_capital) # pos 6 - arg 9
            salvados.append(self.directorio) # pos 7 - arg 10
            salvados.append(self.dicc_pos)  # pos 8 - arg 11
            salvados.append(self.ref) # pos 9 - arg 12
            salvados.append(self.dicc_aux)

            pickle.dump(salvados,open(name + '.p' ,"wb"))

    def guardar_como(self,guardado):
        if self.guardado == False:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            name, _ = QFileDialog.getSaveFileName(self,"Save as...", "","Serialized Files (*.pickle);;Serialized File (*.pickle)", options=options)
            salvados = []
            salvados.append(self.ancho) # pos 0 - arg 3
            salvados.append(self.alto) # pos 1 - arg 4
            salvados.append(self.imgs_sin_cortar) #pos 2 - arg 5
            salvados.append(self.etiquetas) # pos 3 - arg 6
            salvados.append(self.altura) # pos 4 - arg 7
            salvados.append(self.all_metadata) # pos 5 - arg 8
            salvados.append(self.signo_capital) # pos 6 - arg 9
            path_imgs=self.directorio.split('/')
            salvados.append('./'+'Images/'+path_imgs[-2]+'/') # pos 7 - arg 10
            salvados.append(self.dicc_pos)  # pos 8 - arg 11
            salvados.append(self.ref) # pos 9 - arg 12
            salvados.append(self.dicc_aux)
            pickle.dump(salvados,open(name + '.p',"wb"))#Guardar la lista de atributos en un archivo serializado
            self.guardado == True
            self.directorio='./'+'Images/'+path_imgs[-2]+'/'
        else:
            guardar(self.guardado,self.name)

    def localizacion(self,lat,lon):
        latitud=str(lat)
        longitud=str(lon)
        html= \
        """<!DOCTYPE html>
        <html>
          <head>
            <style>
               #map {
                height: 400px;
                width: 100%;
               }
            </style>
          </head>
          <body>
            <div id="map"></div>
            <script>
              function initMap() {
                var uluru = {lat: """+latitud+""", lng: """+longitud+"""};
                var map = new google.maps.Map(document.getElementById('map'), {
                  zoom: 16,
                  center: uluru
                });
                var marker = new google.maps.Marker({
                  position: uluru,
                  map: map
                });
              }
            </script>
            <script async defer
            src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY_HERE&callback=initMap">
            </script>
          </body>
        </html>
        """
        return html

    def botones(self,ancho,alto,altura):
        self.gridLayoutP = QtWidgets.QGridLayout(self.V1S1_Mapa)
        cont = 0
        if altura == 2:
            print('Must not enter here')
            for k in range(alto): #alto
                for l in range(ancho): #ancho
                    self.gridLayoutP.addLayout(self.grid_de_botones_2m(cont),k,l)
                    cont = cont +1
        if altura == 30:
            #print("Para los botones, checando orden:")
            #print(self.dicc_pos)
            for k,val in self.dicc_pos.items():
                #print(k)
                x,y=self.dicc_pos[k]
                #print(x,y)
                self.gridLayoutP.addLayout(self.grid_de_botones_30m(k),y,x)
                #print("Grid: ",k," creado en: ",x,y)
            #for k in range(alto): #alto
                #for l in range(ancho): #ancho
                    #x,y=self.dicc_pos[cont]
                    #self.gridLayoutP.addLayout(self.grid_de_botones_30m(cont),y,x)
                    #print(x,y,"_",k,l)
                    #cont = cont +1 #49 imgs 

    def grid_de_botones_2m(self,imgcont):
        self.buttons = {}
        l_eti=self.dicc_aux[imgcont]
        gridLayout = QtWidgets.QGridLayout()
                        #SA             SE                  NS             NP
        dic_colores = {0:"rgb(109,199,42)",1:"rgb(255,236,0)",2:"rgb(251,153,0)",3:"rgb(158,158,158)", #sin contaminación
                       4:"rgb(112,139,39)",5:"rgb(250,89,1)",6:"rgb(165,111,9)",7:"rgb(40,126,140)"} #con contaminación
        self.mapper = QSignalMapper(self)
        cont = 0
        for i in range(3):
            for j in range(4):
                self.buttons[(i,j)] = QtWidgets.QPushButton("")
                self.buttons[(i,j)].setStyleSheet("background-color: "+dic_colores[self.etiquetas[imgcont][cont]]+";")
                self.buttons[(i,j)].setObjectName(str(i)+"_"+str(j))
                self.mapper.setMapping(self.buttons[(i,j)],str(imgcont)+"_"+str(cont)+"-"+dic_colores[self.etiquetas[imgcont][cont]]+";")
                self.buttons[(i,j)].clicked.connect(self.mapper.map)
                gridLayout.addWidget(self.buttons[(i,j)],i,j)
                cont = cont+1
        self.mapper.mapped[str].connect(self.metodo_boton)
        return gridLayout

    def grid_de_botones_30m(self,imgcont):
        self.buttons = {}
        #l_eti=self.dicc_aux[imgcont]
        gridLayout = QtWidgets.QGridLayout()
                        #SA             SE                  NS             NP
        dic_colores = {0:"rgb(109,199,42)",1:"rgb(255,236,0)",2:"rgb(251,153,0)",3:"rgb(158,158,158)", #sin contaminación
                       4:"rgb(112,139,39)",5:"rgb(250,89,1)",6:"rgb(165,111,9)",7:"rgb(40,126,140)"} #con contaminación
        self.mapper = QSignalMapper(self)
        cont = 0
        
        if self.ref =='NO' or self.ref =='SE':
            for i in range(20):
                for j in range(15):
                    #print("valor dicc: "+dic_colores[self.etiquetas[imgcont][cont]])
                    self.buttons[(i,j)] = QtWidgets.QPushButton("")
                    self.buttons[(i,j)].setStyleSheet("background-color: "+dic_colores[self.etiquetas[imgcont][cont]]+";") #dic_colores[self.etiquetas[imgcont][cont]]
                    self.buttons[(i,j)].setObjectName(str(i)+"_"+str(j))
                    self.mapper.setMapping(self.buttons[(i,j)],str(imgcont)+"_"+str(cont)+"-"+dic_colores[self.etiquetas[imgcont][cont]]+";")
                    self.buttons[(i,j)].clicked.connect(self.mapper.map)
                    gridLayout.addWidget(self.buttons[(i,j)],i,j)
                    cont = cont+1
        if self.ref =='NE' or self.ref =='SO':
            for i in range(15):
                for j in range(20):
                    #print("valor dicc: "+dic_colores[self.etiquetas[imgcont][cont]])
                    self.buttons[(i,j)] = QtWidgets.QPushButton("")
                    self.buttons[(i,j)].setStyleSheet("background-color: "+dic_colores[self.etiquetas[imgcont][cont]]+";") #dic_colores[self.etiquetas[imgcont][cont]]
                    self.buttons[(i,j)].setObjectName(str(i)+"_"+str(j))
                    self.mapper.setMapping(self.buttons[(i,j)],str(imgcont)+"_"+str(cont)+"-"+dic_colores[self.etiquetas[imgcont][cont]]+";")
                    self.buttons[(i,j)].clicked.connect(self.mapper.map)
                    gridLayout.addWidget(self.buttons[(i,j)],i,j)
                    cont = cont+1
        self.mapper.mapped[str].connect(self.metodo_boton)
        return gridLayout

    '''Una señal puede estar sobrecargada, es decir, una señal con un nombre particular puede admitir más de una firma. 
    Una señal puede indexarse ​​con una firma para seleccionar la requerida. Una firma es una secuencia de tipos. 
    Un tipo es un objeto de tipo Python'''
    #para eso se requiere de este metodo, ya que se requiere mandar a llamar a la misma señal "metodo_boton" cada vez que 
    #se presione un boton en el "gridLayout"
    @pyqtSlot(str)    
    def metodo_boton(self,name):
        print(name)
        aux = name.split('-') #Nombre del pedazo de la imagen
        self.V2F2.setStyleSheet("background-color: "+aux[1]+";\n"
"border:rgb(1, 118, 180);")
        pixmap = QPixmap(self.directorio+'ImgsCut/'+aux[0]+'.JPG')
        print(self.directorio+'ImgsCut/'+aux[0]+'.JPG')
        self.V2F2E2_ImgZoom.setPixmap(pixmap)
        vals = aux[0].split('_') #Nombre de la imagen grande
        print(aux[0])
        print(vals[0])
        gps = self.all_metadata[vals[0]+".JPG"]
        self.calcular(gps[0],gps[1])

        self.img_big.actualiza(vals[0],self.etiquetas[int(vals[0])],self.ref) 

        _translate = QtCore.QCoreApplication.translate
        self.V2F4E4_Lat.setText(_translate("VistaMapa", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">"+str(gps[0])+"</span></p></body></html>"))
        self.V2F4E5_Lon.setText(_translate("VistaMapa", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">"+str(gps[1])+"</span></p></body></html>"))
        self.V2F4E5_Alt.setText(_translate("VistaMapa", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">"+str(gps[2])+"</span></p></body></html>"))
