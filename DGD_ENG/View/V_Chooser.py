# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V_Chooser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QMessageBox
from bs4 import BeautifulSoup
from Model.TT_modelo_retrain import TT_modelo_retrain
from PIL import Image,ImageOps,ImageDraw
from PyQt5.QtWidgets import QMessageBox
import os
import numpy as np
from sklearn.utils import shuffle
import csv
import numpy as np
import pickle
import datetime
from sys import platform
import sys
import glob

class Ui_TrainFiles(QWidget):
    def __init__(self,b3,b4,b5): #Se envia como parametro el modelo, para que sea una variable de clase y se puedan utilizar sus metodos.
        super().__init__()
        self.setupUi(self)
        self.V1F1B1_Cargar = b3
        self.V1F1B2_Nuevo = b4
        self.V1Chooser = b5

    def setupUi(self, TrainFiles):
        TrainFiles.setObjectName("TrainFiles")
        TrainFiles.resize(611, 339)
        self.V1F2 = QtWidgets.QFrame(TrainFiles)
        self.V1F2.setGeometry(QtCore.QRect(0, 90, 611, 80))
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
        self.V5_DIR_IMGS = QtWidgets.QPushButton(self.V1F2)
        self.V5_DIR_IMGS.setGeometry(QtCore.QRect(530, 20, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V5_DIR_IMGS.setFont(font)
        self.V5_DIR_IMGS.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V5_DIR_IMGS.setObjectName("V5_DIR_IMGS")
        self.V1F2_2 = QtWidgets.QFrame(self.V1F2)
        self.V1F2_2.setGeometry(QtCore.QRect(620, 70, 641, 80))
        self.V1F2_2.setAutoFillBackground(False)
        self.V1F2_2.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V1F2_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V1F2_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V1F2_2.setObjectName("V1F2_2")
        self.V1F2E1_Ingresa_2 = QtWidgets.QLabel(self.V1F2_2)
        self.V1F2E1_Ingresa_2.setEnabled(True)
        self.V1F2E1_Ingresa_2.setGeometry(QtCore.QRect(40, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E1_Ingresa_2.setFont(font)
        self.V1F2E1_Ingresa_2.setObjectName("V1F2E1_Ingresa_2")
        self.V1F2B1_Directorio_2 = QtWidgets.QPushButton(self.V1F2_2)
        self.V1F2B1_Directorio_2.setGeometry(QtCore.QRect(530, 20, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V1F2B1_Directorio_2.setFont(font)
        self.V1F2B1_Directorio_2.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V1F2B1_Directorio_2.setObjectName("V1F2B1_Directorio_2")
        self.V1F2E2_Path_2 = QtWidgets.QLabel(self.V1F2_2)
        self.V1F2E2_Path_2.setGeometry(QtCore.QRect(150, 20, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E2_Path_2.setFont(font)
        self.V1F2E2_Path_2.setAlignment(QtCore.Qt.AlignCenter)
        self.V1F2E2_Path_2.setObjectName("V1F2E2_Path_2")
        self.V1F2E2_Path = QtWidgets.QLabel(self.V1F2)
        self.V1F2E2_Path.setGeometry(QtCore.QRect(130, 20, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E2_Path.setFont(font)
        self.V1F2E2_Path.setAlignment(QtCore.Qt.AlignCenter)
        self.V1F2E2_Path.setObjectName("V1F2E2_Path")
        self.Chooser_F1 = QtWidgets.QFrame(TrainFiles)
        self.Chooser_F1.setGeometry(QtCore.QRect(0, 0, 721, 91))
        self.Chooser_F1.setAutoFillBackground(False)
        self.Chooser_F1.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.Chooser_F1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Chooser_F1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Chooser_F1.setObjectName("Chooser_F1")
        self.chooser_preparar = QtWidgets.QPushButton(self.Chooser_F1)
        self.chooser_preparar.setEnabled(True)
        self.chooser_preparar.setGeometry(QtCore.QRect(220, 20, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chooser_preparar.setFont(font)
        self.chooser_preparar.setMouseTracking(True)
        self.chooser_preparar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.chooser_preparar.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.chooser_preparar.setObjectName("chooser_preparar")
        self.Chooser_NN = QtWidgets.QFrame(TrainFiles)
        self.Chooser_NN.setGeometry(QtCore.QRect(0, 170, 611, 71))
        self.Chooser_NN.setAutoFillBackground(False)
        self.Chooser_NN.setStyleSheet("background-color: rgb(216, 223, 234);\n"
"border: rgb(216, 223, 234);")
        self.Chooser_NN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Chooser_NN.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Chooser_NN.setObjectName("Chooser_NN")
        self.V1F2E1_Ingresa_3 = QtWidgets.QLabel(self.Chooser_NN)
        self.V1F2E1_Ingresa_3.setEnabled(True)
        self.V1F2E1_Ingresa_3.setGeometry(QtCore.QRect(30, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E1_Ingresa_3.setFont(font)
        self.V1F2E1_Ingresa_3.setObjectName("V1F2E1_Ingresa_3")
        self.V5_DIR_CSV = QtWidgets.QPushButton(self.Chooser_NN)
        self.V5_DIR_CSV.setGeometry(QtCore.QRect(530, 20, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V5_DIR_CSV.setFont(font)
        self.V5_DIR_CSV.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V5_DIR_CSV.setObjectName("V5_DIR_CSV")
        self.V5_DIR_CSV.setEnabled(False)

        self.V1F2E2_Path_3 = QtWidgets.QLabel(self.Chooser_NN)
        self.V1F2E2_Path_3.setGeometry(QtCore.QRect(150, 30, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E2_Path_3.setFont(font)
        self.V1F2E2_Path_3.setAlignment(QtCore.Qt.AlignCenter)
        self.V1F2E2_Path_3.setObjectName("V1F2E2_Path_3")

        self.Param_input = QtWidgets.QFrame(TrainFiles)
        self.Param_input.setGeometry(QtCore.QRect(0, 240, 611, 101))
        self.Param_input.setAutoFillBackground(False)
        self.Param_input.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.Param_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Param_input.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Param_input.setObjectName("Param_input")
        self.Ingresa_it = QtWidgets.QLabel(self.Param_input)
        self.Ingresa_it.setEnabled(True)
        self.Ingresa_it.setGeometry(QtCore.QRect(10, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.Ingresa_it.setFont(font)
        self.Ingresa_it.setObjectName("Ingresa_it")
        self.lineEdit = QtWidgets.QLineEdit(self.Param_input)
        self.lineEdit.setGeometry(QtCore.QRect(250, 40, 91, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"font: 18pt \"Comfortaa\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.chooser_enviar = QtWidgets.QPushButton(self.Param_input)
        self.chooser_enviar.setEnabled(False)
        self.chooser_enviar.setGeometry(QtCore.QRect(450, 20, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chooser_enviar.setFont(font)
        self.chooser_enviar.setMouseTracking(True)
        self.chooser_enviar.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.chooser_enviar.setObjectName("chooser_enviar")

        self.V5_DIR_IMGS.clicked.connect(self.choose_imgs)
        self.V5_DIR_CSV.clicked.connect(self.choose_csv)
        self.chooser_enviar.clicked.connect(self.re_train)
        self.chooser_preparar.clicked.connect(self.Prep_imgs)
        
        self.retranslateUi(TrainFiles)
        QtCore.QMetaObject.connectSlotsByName(TrainFiles)

    def retranslateUi(self, TrainFiles):
        _translate = QtCore.QCoreApplication.translate
        TrainFiles.setWindowTitle(_translate("TrainFiles", "Training Files"))
        self.V1F2E1_Ingresa.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Images:</span></p></body></html>"))
        self.V5_DIR_IMGS.setText(_translate("TrainFiles", "..."))
        self.V1F2E1_Ingresa_2.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Directory:</span></p></body></html>"))
        self.V1F2B1_Directorio_2.setText(_translate("TrainFiles", "..."))
        self.V1F2E2_Path_2.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p></body></html>"))
        self.V1F2E2_Path.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p></body></html>"))
        self.chooser_preparar.setText(_translate("TrainFiles", "Cut Images"))
        self.V1F2E1_Ingresa_3.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">CSV File:</span></p></body></html>"))
        self.V5_DIR_CSV.setText(_translate("TrainFiles", "..."))
        self.Ingresa_it.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" font-family:\'.SF NS Text\'; font-size:18pt; font-weight:400; color:#ffffff;\">Write the number of epochs:</span></p></body></html>"))
        self.lineEdit.setText(_translate("TrainFiles", "1"))
        self.chooser_enviar.setText(_translate("TrainFiles", "Submit"))

    def choose_imgs(self):
        options_imgs = QFileDialog.Options()
        options_imgs |= QFileDialog.DontUseNativeDialog
        self.fileName_imgs, _ = QFileDialog.getOpenFileName(self,"Choose the imagenes", "","JPG Files (*.JPG)", options=options_imgs)
        if self.fileName_imgs:
            _translate = QtCore.QCoreApplication.translate #Permite ejecutar código html a pyqt
            self.V1F2E2_Path.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" color:#ffffff;\">"+self.fileName_imgs+"</span></p></body></html>"))
            #Se coloca todo en el label en donde va el path 
            self.V5_DIR_CSV.setEnabled(True)
            self.lineEdit.setEnabled(True)
            return self.fileName_imgs
        else:
            pass


    def choose_csv(self):
        options_csv = QFileDialog.Options()
        options_csv |= QFileDialog.DontUseNativeDialog
        self.fileName_csv, _ = QFileDialog.getOpenFileName(self,"Choose the tags file", "","CSV  Files(*.csv)", options=options_csv)
        if self.fileName_csv:
            _translate = QtCore.QCoreApplication.translate #Permite ejecutar código html a pyqt
            self.V1F2E2_Path_3.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" color:#ffffff;\">"+self.fileName_csv+"</span></p></body></html>"))
            #Se coloca todo en el label en donde va el path
            self.chooser_enviar.setEnabled(True) 
            return self.fileName_csv
        else:
            pass

    def make_train_pickle():
    	pass

    def re_train(self):
        # Creando el pickle con el csv y las imagenes
        self.dir_imgs_retrain = os.path.dirname(self.fileName_imgs)
        self.dir_imgs_retrain = self.dir_imgs_retrain + '/'
        path_img = self.dir_imgs_retrain
        #path_img = '/Users/anayantzinp/Desktop/RE_PARQUE_B/'
        #path_img, _= os.path.split(self.fileName_imgs)
        path_csv = self.fileName_csv
        with open(path_csv,newline='') as csvfile:
            spamreader = csv.reader(csvfile,quotechar='|')
            lp = []
            for row in spamreader:
                np_arr = np.array(Image.open(path_img+row[0]))
                if row[1] == 'SA' and row[2] =='0':
                    lp.append([np_arr,[1,0,0,0,0,0,0,0]])
                if row[1] == 'SA' and row[2] =='1':
                    lp.append([np_arr,[0,0,0,0,1,0,0,0]])
                if row[1] == 'SE' and row[2] == '0':
                    lp.append([np_arr,[0,1,0,0,0,0,0,0]])
                if row[1] == 'SE' and row[2] == '1':
                    lp.append([np_arr,[0,0,0,0,0,1,0,0]])
                if row[1] == 'NS' and row[2] == '0':
                    lp.append([np_arr,[0,0,1,0,0,0,0,0]])
                if row[1] == 'NS' and row[2] == '1':
                    lp.append([np_arr,[0,0,0,0,0,0,1,0]])
                if row[1] == 'NP' and row[2] == '0':
                    lp.append([np_arr,[0,0,0,1,0,0,0,0]])
                if row[1] == 'NP' and row[2] == '1':
                    lp.append([np_arr,[0,0,0,0,0,0,0,1]])
                del np_arr
        lp=shuffle(lp)
        len_data=len(lp)
        ########### Hacer pickle para retrain

        name_pickle = self.dir_imgs_retrain.split('/')
        #print(name_pickle)
        len_pickle_train = int(len_data*.8)
        len_pickle_test  = len_data-len_pickle_train
        h = 0
        cont_train = 0
        if len_pickle_train >= 9000:
            if len_pickle_train%9000 == 0:
                dim1 = len_pickle_train/9000
                for d in range(0,int(dim1)):
                    pickle.dump(lp[h:len_pickle_train+h],open("./Model/Pickles/"+name_pickle[-2]+"Train_"+str(d)+".pickle","wb"))
                    cont_train = d
                h = h + 9000
            elif len_pickle_train%9000 != 0:
                module = len_pickle_train%9000
                dim1 = module/9000
                for d in range(0,int(dim1)):
                    pickle.dump(lp[h:len_pickle_train+h],open("./Model/Pickles/"+name_pickle[-2]+"Train_"+str(d)+".pickle","wb"))
                    cont_train = d
                h = h + 9000
        else:
            pickle.dump(lp[0:len_pickle_train],open("./Model/Pickles/"+name_pickle[-2]+"Train_0.pickle","wb"))
            cont_train = 1
        h = 0
        cont_test = 0
        if len_pickle_test >= 9000:
            QMessageBox.critical(self, "Error", "Maximum size of test set = 9000 images")
            '''if len_pickle_test%9000 == 0:
                dim1 = len_pickle_test/9000
                for d in range(0,int(dim1)):
                    pickle.dump(lp[h:len_pickle_test+h],open("./Model/Pickles/"+name_pickle[-2]+"Test_"+str(d)+".pickle","wb"))
                    cont_test = d
                h = h + 9000
            elif len_pickle_test%9000 != 0:
                module = len_pickle_test%9000
                dim1 = module/9000
                for d in range(0,int(dim1)):
                    pickle.dump(lp[h:len_pickle_test+h],open("./Model/Pickles/"+name_pickle[-2]+"Test_"+str(d)+".pickle","wb"))
                    cont_test = d
                h = h + 9000'''
        else:
            pickle.dump(lp[0:len_pickle_test],open("./Model/Pickles/"+name_pickle[-2]+"Test_0.pickle","wb"))
            cont_test = 1
        del lp

        # Creando los directorios para la nueva red (Carpeta Nuevo, Pesos y CNNClass)
        now = datetime.datetime.now()
        date = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)
        if os.path.exists("./Model/Nets/New_"+date) == False:
            os.makedirs("./Model/Nets/New_"+date)
        if os.path.exists("./Model/Nets/New_"+date+"/Pesos") == False:
            os.makedirs("./Model/Nets/New_"+date+"/Pesos")
        if os.path.exists("./Model/Nets/New_"+date+"/CNNClass") == False:
            os.makedirs("./Model/Nets/New_"+date+"/CNNClass")
        

        path_pickle = "./Model/Pickles/"+name_pickle[-2]
        ## tamaño del batch, pickle y path del nuevo archivo para pesos y bias
        #Obtenemos el tamaño del batch, recordemos que en mac no podemos guardar pickles mayores a 2 GB
        #Instanciamos la clase 
        clase_arquitectura_retrain = TT_modelo_retrain(100,path_pickle,"./Model/Nets/OriginalNet/Pesos/AreaVerde30m.ckpt")
        #Instanciamos la arquitectura
        intance_dicc  = clase_arquitectura_retrain.deep_neural_convolutional_class() 
        #print("INSTANCIA CREADA CORRECTAMENTE")
        #Preparamos el entrenamiento (Metemos lo necesario)
        trainig_encoder = clase_arquitectura_retrain.training(intance_dicc,path_pickle,cont_train,self.lineEdit.text(),
                                                              batch_size=20,save="./Model/Nets/New_"+date+"/Pesos/Pesos.ckpt",path_restore="./Model/Nets/New_"+date+"/CNNClass/",
                                                              checkpoint="./Model/Nets/OriginalNet/Pesos/AreaVerde30m.ckpt",
                                                              verbose=False)
        #print(trainig_encoder)
        #print("Termina entrenamiento")
        del(intance_dicc)

        ############Cargar Pickle para realizar la evaluacion de la red
        path= "./Model/Pickles/"+name_pickle[-2]+"Test_0.pickle"
        data1=np.array(pickle.load(open(path,"rb"))) #np.load()
        ####### RE TRAIN
        g = clase_arquitectura_retrain.deep_neural_convolutional_class(batch_size=len_pickle_test)
        ######CHECK NET 
        pred,accuracy = clase_arquitectura_retrain.check_net(g,data1,"./Model/Nets/New_"+date+"/Pesos/Pesos.ckpt","./Model/Nets/New_"+date+"/CNNClass/")
        percentage_acc = accuracy*100
        buttonReply = QMessageBox.question(self, 'Training finished', "Accuracy: "+str(format(percentage_acc, '.2f'))+"%"+"\n¿Do you want to analize a map?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        del(g)
        if buttonReply == QMessageBox.Yes:
            self.V1F1B1_Cargar.setEnabled(True)
            self.V1F1B2_Nuevo.setEnabled(True)
            self.V1Chooser.setEnabled(True)
            del(self)
        else:
            sys.exit()
        #En esta parte colocar un ventana emergente con el accuracy y el exito en el entrenamiento
        #También habilitar o refrescar la vista inicio, para seleccionar la nueva red y destruir esta ventana

    def Prep_imgs(self):
        options_prep = QFileDialog.Options()
        options_prep |= QFileDialog.DontUseNativeDialog
        fileName_prep, _ = QFileDialog.getOpenFileName(self,"Choose images", "","JPG Files (*.JPG)", options=options_prep)
        val_img = os.path.dirname(fileName_prep)

        self.imagenCruda = os.path.dirname(fileName_prep)
        self.imagenCruda = self.imagenCruda + '/'
        path_img_cruda = self.imagenCruda

        with open(fileName_prep,"rb") as fin:
            img = fin.read()
        imgAsString=str(img)
        soup = BeautifulSoup(imgAsString, 'html.parser')
        string = str(soup.find_all("rdf:description"))
        l = string.split()
        FlyYawDegree = l[12].split("=")
        if fileName_prep and FlyYawDegree[0] == 'drone-dji:flightyawdegree':
            self.chooser_enviar.setEnabled(True) 
            #return fileName_prep
        else:
            #print('Error: Unrecognized images')
            QMessageBox.critical(self, "Error", "The input images do not belong to the DJI family")
        #Renombrar las imagenes
        self.renamer()
        #print("Todo bien hasta aqui")
        #Crear una carpeta que contendra las imagenes recortadas del conjunto total
        if os.path.exists(self.imagenCruda+'Imgs_Prep') == False:
            os.makedirs(self.imagenCruda+'Imgs_Prep')
        for cont,item in enumerate(sorted(glob.glob(self.imagenCruda+'*.JPG'),key=os.path.getmtime)):
            img = Image.open(item)
            self.cut_img(img,cont,'Imgs_Prep')#Corta imagenes y las coloca en una lista
            img.close()
        #Hacer pickle

        buttonOK = QMessageBox.information(self, "Attention", "The images have been cut, take your time to prepare your Tags File (CSV)",buttons = QMessageBox.Ok)

        if buttonOK == QMessageBox.Ok:
            sys.exit()

    def renamer(self):#Recibe path
        cont = 0
        for fname in sorted(glob.glob(self.imagenCruda+'*.JPG'),key=os.path.getmtime):
            os.rename(fname,self.imagenCruda+str(cont)+'.JPG')#Aqui va la extensión con la cual se va a renombrar
            cont = cont+1
        return None 

    def cut_img(self,img,num_img,directorio):
        """
        GET: La imagen, el numero de imagen a la que corresponde, el directorio que se creo para poner las imagenes
            y la altura a la que se volo el dron
        Return: Se devolverán las 12 imagenes
        """
        l_img = []
        cont=0
        h=img.size[0]
        v=img.size[1]
        for x in range(0,4000,200):
            for y in range(0,3000,200):
                img_n = img.crop((x,y,200+x,200+y))
                img_n.save(self.imagenCruda+directorio+"/"+str(num_img)+"_"+str(cont)+".JPG")
                cont=cont+1

