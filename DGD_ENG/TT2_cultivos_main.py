"""
******************************************************************
Autores:
López Juárez Anayantzin Paola
Vargas Monroy Israel Agustin
Trabajo: ESCOM-IPN TT A009
TT-II Tratamiento de imágenes con CNN para la estimación de la sa-
lud de los cultivos.
Versión:
1.0
Descripción de clase:
De acuerdo con el MV, el programa pricipal debe de realizar la i-
nstanciación de todas las clases necesarias para poder crear los e
nlaces entre las clases.
******************************************************************
"""

"""
Imports: modulos de las librerias de python
Imports de paquetes: clases que importamos de cada carpeta del pro
yecto.
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Model.TT_cultivos_modelo import TT_modelo #Hay que pasarlo a orientado a obejtos
from View.VistaInicio import Ui_VistaInicial


class TT2_main(object):
	"""
	Documentación para TT2_main:
	DENTRO DEL IF
	La razón de poner __name__, es que es un métododefine el espaci
	o de nombres en el que se está ejecutando. Es usado para identi
	ficar de forma única un módulo en el sistema de importaciones.
	Por su parte __main__ es el nombre del ámbito en el que se ejec
	uta el código de nivel superior (tu programa principal).
	El intérprete pasa el valor del atributo a '__main__' si el mód
	ulo se está ejecutando como programa principal (cuando lo ejecu
	tas llamando al intérptrete en la terminal con python my_modulo
	.py, haciendo doble click en él, ejecutandolo en el intérprete 
	interactivo, etc ).
	Si el módulo no es llamado como programa principal, sino que es 
	importado desde otro módulo, el atributo __name__ pasa a conten
	er el nombre del archivo en si.

	DENTRO DEL CONSTRUCTOR:
	Esto llama al constructor de la clase C ++ QApplication. Utiliz
	a sys.argv (argc y argv en C ++) para inicializar la aplicación
	QT. Hay muchos argumentos que puede pasar a QT, como estilos, d
	epuración, etc. 
	"""
	def __init__(self):
		super().__init__()
		modelo1 = TT_modelo("")
		app = QtWidgets.QApplication(sys.argv) #pasarle modelo 2 ui
		ui = Ui_VistaInicial(modelo1) #Cuando se intancia la clase,
		# este ejecuta por defecto al contructor.
		ui.showing() #Se realiza esto para que la ventana solo se m
		#uestre una ves y no varias cuando la segunda ventana se ci
		#erre y vuelva a llamar a la primer venta.
		sys.exit(app.exec_()) #Mantiene en ejecución a la aplicación.

if __name__ == '__main__':
	app = TT2_main() #Se instancia la aplicación.