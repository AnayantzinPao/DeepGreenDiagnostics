import sys
from PyQt5.QtWidgets import QApplication, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Grafica(QWidget):

    def __init__(self,porcentajes,GPS_data,alto,ancho,totalbio,perCon,paramBio):
        self.porcentajes = porcentajes
        self.GPS_data = GPS_data
        self.alto = alto
        self.ancho = ancho
        self.totalbio = totalbio
        self.perCon = perCon
        self.paramBio = paramBio
        super().__init__()
        self.setupUi(self)

        self.rutaDrone()
        self.graficaSalud()
        self.datos()
        self.graficaBio()
        self.datosBio()

    def setupUi(self, Grafica):
        Grafica.setObjectName("Grafica")
        Grafica.resize(972, 434)
        self.centralwidget = QtWidgets.QWidget(Grafica)
        self.centralwidget.setObjectName("centralwidget")
        self.V3Frame_Grafica = QtWidgets.QFrame(self.centralwidget)
        self.V3Frame_Grafica.setGeometry(QtCore.QRect(0, 30, 331, 281))
        self.V3Frame_Grafica.setStyleSheet("background-color: rgb(216, 223, 234);")
        self.V3Frame_Grafica.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V3Frame_Grafica.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V3Frame_Grafica.setObjectName("V3Frame_Grafica")
        self.gridLayoutWidget = QtWidgets.QWidget(self.V3Frame_Grafica)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 331, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.V3Grid1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.V3Grid1.setContentsMargins(0, 0, 0, 0)
        self.V3Grid1.setObjectName("V3Grid1")
        self.V3Frame_Vuelo = QtWidgets.QFrame(self.centralwidget)
        self.V3Frame_Vuelo.setGeometry(QtCore.QRect(330, 30, 311, 281))
        self.V3Frame_Vuelo.setStyleSheet("background-color: rgb(216, 223, 234);")
        self.V3Frame_Vuelo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V3Frame_Vuelo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V3Frame_Vuelo.setObjectName("V3Frame_Vuelo")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.V3Frame_Vuelo)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, -1, 311, 281))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.V3Grid2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.V3Grid2.setContentsMargins(0, 0, 0, 0)
        self.V3Grid2.setObjectName("V3Grid2")
        self.V3FrameEt1 = QtWidgets.QFrame(self.centralwidget)
        self.V3FrameEt1.setGeometry(QtCore.QRect(0, 0, 331, 31))
        self.V3FrameEt1.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V3FrameEt1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V3FrameEt1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V3FrameEt1.setObjectName("V3FrameEt1")
        self.V3LabeGrafica = QtWidgets.QLabel(self.V3FrameEt1)
        self.V3LabeGrafica.setGeometry(QtCore.QRect(80, 10, 181, 20))
        self.V3LabeGrafica.setObjectName("V3LabeGrafica")
        self.V3FrameEt2 = QtWidgets.QFrame(self.centralwidget)
        self.V3FrameEt2.setGeometry(QtCore.QRect(329, 0, 311, 31))
        self.V3FrameEt2.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V3FrameEt2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V3FrameEt2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V3FrameEt2.setObjectName("V3FrameEt2")
        self.V3LabeVuelo = QtWidgets.QLabel(self.V3FrameEt2)
        self.V3LabeVuelo.setGeometry(QtCore.QRect(100, 10, 121, 20))
        self.V3LabeVuelo.setObjectName("V3LabeVuelo")
        self.V3F3 = QtWidgets.QFrame(self.centralwidget)
        self.V3F3.setGeometry(QtCore.QRect(0, 310, 331, 121))
        self.V3F3.setStyleSheet("background-color: rgb(216, 223, 234);")
        self.V3F3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V3F3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V3F3.setObjectName("V3F3")
        self.V3F3L2_color = QtWidgets.QLabel(self.V3F3)
        self.V3F3L2_color.setGeometry(QtCore.QRect(140, 40, 51, 31))
        self.V3F3L2_color.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.V3F3L2_color.setText("")
        self.V3F3L2_color.setObjectName("V3F3L2_color")
        self.V3F3L3_analisis = QtWidgets.QLabel(self.V3F3)
        self.V3F3L3_analisis.setGeometry(QtCore.QRect(10, 80, 311, 31))
        self.V3F3L3_analisis.setObjectName("V3F3L3_analisis")
        self.V3F3L1_titulo = QtWidgets.QLabel(self.V3F3)
        self.V3F3L1_titulo.setGeometry(QtCore.QRect(90, 10, 161, 17))
        self.V3F3L1_titulo.setObjectName("V3F3L1_titulo")
        self.V4F4 = QtWidgets.QFrame(self.centralwidget)
        self.V4F4.setGeometry(QtCore.QRect(330, 310, 311, 121))
        self.V4F4.setStyleSheet("background-color: rgb(216, 223, 234);\n"
"")
        self.V4F4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V4F4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V4F4.setObjectName("V4F4")
        self.label_3 = QtWidgets.QLabel(self.V4F4)
        self.label_3.setGeometry(QtCore.QRect(70, 10, 191, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.V4F4)
        self.label_4.setGeometry(QtCore.QRect(50, 60, 221, 20))
        self.label_4.setObjectName("label_4")
        self.V3FrameEt3_Porcentaje = QtWidgets.QFrame(self.centralwidget)
        self.V3FrameEt3_Porcentaje.setGeometry(QtCore.QRect(640, 0, 331, 31))
        self.V3FrameEt3_Porcentaje.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V3FrameEt3_Porcentaje.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V3FrameEt3_Porcentaje.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V3FrameEt3_Porcentaje.setObjectName("V3FrameEt3_Porcentaje")
        self.label = QtWidgets.QLabel(self.V3FrameEt3_Porcentaje)
        self.label.setGeometry(QtCore.QRect(90, 10, 161, 20))
        self.label.setObjectName("label")
        self.V3Frame_Porcentajes = QtWidgets.QFrame(self.centralwidget)
        self.V3Frame_Porcentajes.setGeometry(QtCore.QRect(640, 310, 331, 121))
        self.V3Frame_Porcentajes.setStyleSheet("background-color: rgb(216, 223, 234);\n"
"")
        self.V3Frame_Porcentajes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V3Frame_Porcentajes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V3Frame_Porcentajes.setObjectName("V3Frame_Porcentajes")
        self.label_2 = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 21, 17))
        self.label_2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 21, 17))
        self.label_5.setStyleSheet("background-color: rgb(112,139,39);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.label_6.setGeometry(QtCore.QRect(120, 40, 21, 17))
        self.label_6.setStyleSheet("background-color: rgb(250,89,1);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.label_7.setGeometry(QtCore.QRect(120, 10, 21, 17))
        self.label_7.setStyleSheet("background-color: rgb(255,236,0);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.label_8.setGeometry(QtCore.QRect(230, 10, 21, 17))
        self.label_8.setStyleSheet("background-color: rgb(251,153,0);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.label_9.setGeometry(QtCore.QRect(230, 40, 21, 17))
        self.label_9.setStyleSheet("background-color: rgb(165,111,9);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.label_10.setGeometry(QtCore.QRect(10, 100, 211, 17))
        self.label_10.setObjectName("label_10")
        self.V3PoC = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.V3PoC.setGeometry(QtCore.QRect(260, 100, 67, 17))
        self.V3PoC.setObjectName("V3PoC")
        self.V3PBS = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.V3PBS.setGeometry(QtCore.QRect(40, 10, 67, 17))
        self.V3PBS.setObjectName("V3PBS")
        self.V3PBSe = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.V3PBSe.setGeometry(QtCore.QRect(150, 10, 67, 17))
        self.V3PBSe.setObjectName("V3PBSe")
        self.V3PBNS = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.V3PBNS.setGeometry(QtCore.QRect(260, 10, 67, 17))
        self.V3PBNS.setObjectName("V3PBNS")
        self.V3PBSC = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.V3PBSC.setGeometry(QtCore.QRect(40, 40, 67, 17))
        self.V3PBSC.setObjectName("V3PBSC")
        self.V3PBSeC = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.V3PBSeC.setGeometry(QtCore.QRect(150, 40, 67, 17))
        self.V3PBSeC.setObjectName("V3PBSeC")
        self.V3PBNSC = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.V3PBNSC.setGeometry(QtCore.QRect(260, 40, 67, 17))
        self.V3PBNSC.setObjectName("V3PBNSC")
        self.label_18 = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.label_18.setGeometry(QtCore.QRect(80, 70, 67, 17))
        self.label_18.setObjectName("label_18")
        self.V3SumBio = QtWidgets.QLabel(self.V3Frame_Porcentajes)
        self.V3SumBio.setGeometry(QtCore.QRect(190, 70, 67, 17))
        self.V3SumBio.setObjectName("V3SumBio")
        self.V3Frame_GraficaBio = QtWidgets.QFrame(self.centralwidget)
        self.V3Frame_GraficaBio.setGeometry(QtCore.QRect(640, 30, 331, 281))
        self.V3Frame_GraficaBio.setStyleSheet("background-color: rgb(216, 223, 234);\n"
"")
        self.V3Frame_GraficaBio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V3Frame_GraficaBio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V3Frame_GraficaBio.setObjectName("V3Frame_GraficaBio")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.V3Frame_GraficaBio)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(-1, -1, 331, 281))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.V3GridBio = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.V3GridBio.setContentsMargins(0, 0, 0, 0)
        self.V3GridBio.setObjectName("V3GridBio")
        #Grafica.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grafica)
        QtCore.QMetaObject.connectSlotsByName(Grafica)

    def retranslateUi(self, Grafica):
        _translate = QtCore.QCoreApplication.translate
        Grafica.setWindowTitle(_translate("Grafica", "Data"))
        self.V3LabeGrafica.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Health percentage.</span></p></body></html>"))
        self.V3LabeVuelo.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Flightmade.</span></p></body></html>"))
        self.V3F3L3_analisis.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">98 % of contaminated no-vegetation area .</span></p></body></html>"))
        self.V3F3L1_titulo.setText(_translate("Grafica", "<html><head/><body><p><span style=\" font-weight:600;\">Analysis results:</span></p></body></html>"))
        self.label_3.setText(_translate("Grafica", "<html><head/><body><p><span style=\" font-weight:600;\">Total square meters covered:</span></p></body></html>"))
        self.label_4.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">W * H meters.</span></p></body></html>"))
        self.label.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Biomass percent.</span></p></body></html>"))
        self.label_10.setText(_translate("Grafica", "<html><head/><body><p><span style=\" font-weight:600;\">Contamination percent:</span></p></body></html>"))
        self.V3PoC.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">24.34%</span></p></body></html>"))
        self.V3PBS.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">24.34%</span></p></body></html>"))
        self.V3PBSe.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">24.34%</span></p></body></html>"))
        self.V3PBNS.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">24.34%</span></p></body></html>"))
        self.V3PBSC.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">24.34%</span></p></body></html>"))
        self.V3PBSeC.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">24.34%</span></p></body></html>"))
        self.V3PBNSC.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">24.34%</span></p></body></html>"))
        self.label_18.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Total:</span></p></body></html>"))
        self.V3SumBio.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">24.34%</span></p></body></html>"))

    def rutaDrone(self):
        self.fig = Figure((5.0, 5.0), dpi=50, facecolor="#F6F4F2")

        self.canvas = FigureCanvas(self.fig)
        self.V3Grid2.addWidget(self.canvas,0,0)
        self.graph_a = self.fig.add_subplot(111)
        
        #self.graph_c = self.fig.add_subplot(313)

        #self.graph_a.grid(True)
        x = []
        y = []
        for k,v in self.GPS_data.items():
            x.append(v[0])
            y.append(v[1])
        self.graph_a.plot(x[0:2],y[0:2],marker='*',color='g',label='inicio')
        self.graph_a.plot(x[1:-2],y[1:-2],marker='o',color='b')
        self.graph_a.plot(x[-3:-1],y[-3:-1],marker='x',color='r',label='termino')
        self.graph_a.set_xlabel("Longitud")
        self.graph_a.set_ylabel("Latitud")

        """self.graph_c.grid(True)
        self.graph_c.axes.set_xlim([1, 3])
        self.graph_c.axes.set_ylim([0, 120])
        self.graph_c.plot(data2, '--')"""

        self.graph_plot_a = self.graph_a.plot(
            [],
            linewidth=1,
            color=("darkorange"),
        )[0]
        """self.graph_plot_c = self.graph_c.plot(
            [],
            linewidth=1,
            color=("darkorange"),
        )[0]"""

        ajust = {"top": 0.95,
                 "bottom": 0.1,
                 "right": 0.97,
                 "left": 0.05,
                 "wspace": 0.2,
                 "hspace": 1, }
        #self.fig.subplots_adjust(**ajust)

        # graficar (lo que se ve cuando se ejecuta el programa por)
        self.canvas.draw()

    def graficaSalud(self):
        self.fig2 = Figure((5.0, 5.0), dpi=50, facecolor="#F6F4F2")

        self.canvas2 = FigureCanvas(self.fig2)
        self.V3Grid1.addWidget(self.canvas2,0,0)
        self.graph_b = self.fig2.add_subplot(111)

        labels = 'SA', 'SE', 'NS', 'NP','SAC','SEC','NSC','NPC'
        self.graph_b.bar(labels,self.porcentajes,3/4)
        self.graph_b.get_children()[0].set_color('#6DC72A') 
        self.graph_b.get_children()[1].set_color('#FFEC00') 
        self.graph_b.get_children()[2].set_color('#FB9900') 
        self.graph_b.get_children()[3].set_color('#9E9E9E') 
        self.graph_b.get_children()[4].set_color('#708B27') 
        self.graph_b.get_children()[5].set_color('#FA5901') 
        self.graph_b.get_children()[6].set_color('#A56F09') 
        self.graph_b.get_children()[7].set_color('#287E8C') 
        self.canvas2.draw()

    def graficaBio(self):
        self.fig3 = Figure((5.0, 5.0), dpi=50, facecolor="#F6F4F2")

        self.canvas3 = FigureCanvas(self.fig3)
        self.V3GridBio.addWidget(self.canvas3,0,0)
        self.graph_c = self.fig3.add_subplot(111)

        labels = 'Bio Sa', 'Bio Se', 'Bio NS', 'Bio SaC','Bio SeC','Bio NSC'
        self.graph_c.bar(labels,self.paramBio,3/4)
        self.graph_c.get_children()[0].set_color('#6DC72A') 
        self.graph_c.get_children()[1].set_color('#FFEC00') 
        self.graph_c.get_children()[2].set_color('#FB9900') 
        self.graph_c.get_children()[4].set_color('#708B27') 
        self.graph_c.get_children()[5].set_color('#FA5901') 
        self.graph_b.get_children()[6].set_color('#A56F09') 
        self.canvas3.draw()

    def datos(self):
        #Agregar la alerta con el color
        dic_colores = {0:"rgb(109,199,42)",1:"rgb(255,236,0)",2:"rgb(251,153,0)",3:"rgb(158,158,158)", #sin contaminación
                       4:"rgb(112,139,39)",5:"rgb(250,89,1)",6:"rgb(165,111,9)",7:"rgb(40,126,140)"} 
        self.V3F3L2_color.setStyleSheet("background-color: "+dic_colores[self.porcentajes.index(max(self.porcentajes))]+";")
        _translate = QtCore.QCoreApplication.translate
        if self.porcentajes.index(max(self.porcentajes)) == 0:
            porcentaje = round (max(self.porcentajes),2)
            self.V3F3L3_analisis.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"+str(porcentaje)+"% of healthy area.</span></p></body></html>"))
        elif self.porcentajes.index(max(self.porcentajes)) == 1:
            porcentaje = round (max(self.porcentajes),2)
            self.V3F3L3_analisis.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"+str(porcentaje)+"% of dry area.</span></p></body></html>"))
        elif self.porcentajes.index(max(self.porcentajes)) == 2:
            porcentaje = round (max(self.porcentajes),2)
            self.V3F3L3_analisis.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"+str(porcentaje)+"% of unhealthy area.</span></p></body></html>"))
        elif self.porcentajes.index(max(self.porcentajes)) == 3:
            porcentaje = round (max(self.porcentajes),2)
            self.V3F3L3_analisis.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"+str(porcentaje)+"% of no-vegetation area.</span></p></body></html>"))
        elif self.porcentajes.index(max(self.porcentajes)) == 4:
            porcentaje = round (max(self.porcentajes),2)
            self.V3F3L3_analisis.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"+str(porcentaje)+"% of contaminated healthy area.</span></p></body></html>"))
        elif self.porcentajes.index(max(self.porcentajes)) == 5:
            porcentaje = round (max(self.porcentajes),2)
            self.V3F3L3_analisis.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"+str(porcentaje)+"% of contaminated dry area.</span></p></body></html>"))
        elif self.porcentajes.index(max(self.porcentajes)) == 6:
            porcentaje = round (max(self.porcentajes),2)
            self.V3F3L3_analisis.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"+str(porcentaje)+"% of contaminated unhealthy area.</span></p></body></html>"))
        elif self.porcentajes.index(max(self.porcentajes)) == 7:
            porcentaje = round (max(self.porcentajes),2)
            self.V3F3L3_analisis.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"+str(porcentaje)+"% of contaminated no-vegetation area.</span></p></body></html>"))

        #Datos para calcular el área mapeada 1.31 es nuesto GSD
        ancho = (((self.ancho*(4000*1.31))/100)-(((self.ancho*(4000*1.31))*0.26)/100))
        alto  = (((self.alto*(3000*1.31))/100)-(((self.alto*(3000*1.31))*0.26)/100))

        self.label_4.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">"+str(round(ancho*alto,2))+" square meters.</span></p></body></html>"))

    def datosBio(self):
        _translate = QtCore.QCoreApplication.translate
        self.V3PBS.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">"+str("{0:.2f}".format(self.paramBio[0]))+"%</span></p></body></html>"))
        self.V3PBSe.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">"+str("{0:.2f}".format(self.paramBio[1]))+"%</span></p></body></html>"))
        self.V3PBNS.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">"+str("{0:.2f}".format(self.paramBio[2]))+"%</span></p></body></html>"))
        self.V3PBSC.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">"+str("{0:.2f}".format(self.paramBio[3]))+"%</span></p></body></html>"))
        self.V3PBSeC.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">"+str("{0:.2f}".format(self.paramBio[4]))+"%</span></p></body></html>"))
        self.V3PBNSC.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">"+str("{0:.2f}".format(self.paramBio[5]))+"%</span></p></body></html>"))
        self.V3SumBio.setText(_translate("Grafica", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">"+str("{0:.2f}".format(self.totalbio))+"%</span></p></body></html>"))
        self.V3PoC.setText(_translate("Grafica", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">"+str("{0:.2f}".format(self.perCon))+"%</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Grafica = QtWidgets.QMainWindow()
    ui = Ui_Grafica()
    ui.setupUi(Grafica)
    Grafica.show()
    sys.exit(app.exec_())

