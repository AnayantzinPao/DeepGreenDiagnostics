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
import tensorflow as tf
	 ###############
	 ##Red neuronal
	 ###############
class TT_modelo_RNC:

	def __init__(self, batch_size, path_pickle, path_checkpoint):
		self.checkpoint = path_checkpoint
		self.imagenes = np.array(pickle.load(open(path_pickle+".pickle","rb"))) #Es todo el archivo pickle que contenga las imágenes
		self.batch_size = batch_size #tamaño del pickle
		self.arquitectura = self.deep_neural_convolutional_class_build(self.batch_size,
			image_size=[200,200],
			Drop_prob=1.0,
			learning_rate = 1e-2,
			n_nodes_hl1 = 100,
			n_nodes_hl2 = 100,
			n_nodes_hl3 = 100,
			n_nodes_hl4 = 100,
			n_classes=8)

	def conv2d(self,x, W,strid=[1,1,1,1]):
		return tf.nn.conv2d(x, W, strides=strid, padding='SAME')

	def maxpool2d(self,x,ks=[1,2,2,1],st=[1,2,2,1]):
		"""
		size of window  movement of window
		"""
		return tf.nn.max_pool(x, ksize=ks, strides=st, padding='SAME')

	def reset_graph(self):
		"""
		Limpia la grafica de tensorboard.
		"""
		if 'sess' in globals() and sess:
			sess.close()
		tf.reset_default_graph()

	def deep_neural_convolutional_class_build(self,
	    batch_size=20,
	    image_size=[200,200],
	    Drop_prob=1.0,
	    learning_rate = 1e-2,
	    n_nodes_hl1 = 100,
	    n_nodes_hl2 = 100,
	    n_nodes_hl3 = 100,
	    n_nodes_hl4 = 100,
	    n_classes=8
	    ):
	    
	    self.reset_graph()
	    #input place holder 
	    x= tf.placeholder(tf.float32,[batch_size,image_size[0],image_size[1],3], name='input_image_placeholder')
	  
	    # Convolutional weigths and Bias 
	    
	    weigths={"w_conv1":tf.Variable(tf.random_normal([5,5,3,32])),
	                 "w_conv2":tf.Variable(tf.random_normal([5,5,32,64])),
	                 "w_conv3":tf.Variable(tf.random_normal([5,5,64,128])),   
	                 "w_conv4":tf.Variable(tf.random_normal([5,5,128,256])),
	                 "w_conv5":tf.Variable(tf.random_normal([5,5,256,512])),
	                }
	    
	    biases={"b_conv1":tf.Variable(tf.random_normal([32])),
	                "b_conv2":tf.Variable(tf.random_normal([64])),
	                "b_conv3":tf.Variable(tf.random_normal([128])),
	                "b_conv4":tf.Variable(tf.random_normal([256])),
	                "b_conv5":tf.Variable(tf.random_normal([512])),
	               }

	    conv1=tf.nn.relu(self.conv2d(x,weigths["w_conv1"],strid=[1,2,2,1])+biases["b_conv1"])
	    conv1=tf.nn.dropout(conv1,Drop_prob)
	        #imagen resultante de 100x100x32
	    
	    conv2=tf.nn.relu(self.conv2d(conv1,weigths["w_conv2"],strid=[1,2,2,1])+biases["b_conv2"])
	    conv2=tf.nn.dropout(conv2,Drop_prob)
	        #imagen resultante de 50x50x64
	        
	    conv3=tf.nn.relu(self.conv2d(conv2,weigths["w_conv3"],strid=[1,2,2,1])+biases["b_conv3"])
	    conv3=tf.nn.dropout(conv3,Drop_prob)
	        #imagen resultante de 25x25x128
	    
	    conv4=tf.nn.relu(self.conv2d(conv3,weigths["w_conv4"],strid=[1,5,5,1])+biases["b_conv4"])
	    conv4=tf.nn.dropout(conv4,Drop_prob)
	    	#imagen resultante de 5x5x256
	    
	    conv5=tf.nn.relu(self.conv2d(conv4,weigths["w_conv5"],strid=[1,5,5,1])+biases["b_conv5"])
	    conv5=tf.nn.dropout(conv5,Drop_prob)
	    	#imagen resultante de 1x1x512
	    
	    #Este es el resultado de las caracteristicas extraidas por la red convolucional que 
	    #posteriormente serán los parametros de entrada a la red completamente conectada p-
	    #ara su clasifiación.
	    embdeding=tf.reshape(conv5,[batch_size,512]) 

	    ########Capa completamente conectada########
	    
	    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([512, n_nodes_hl1])),
	                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

	    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
	                      'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

	    hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
	                      'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

	    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
	                    'biases':tf.Variable(tf.random_normal([n_classes])),}
	    
	    l1 = tf.add(tf.matmul(embdeding,hidden_1_layer['weights']), hidden_1_layer['biases'])
	    l1 = tf.nn.relu(l1)
	    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
	    l2 = tf.nn.relu(l2)
	    l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']), hidden_3_layer['biases'])
	    l3 = tf.nn.relu(l3)

	    output = tf.matmul(l3,output_layer['weights']) + output_layer['biases']

	    ########Capa completamente conectada########FIN
	    
	    #Diccionario de alimentación.
	    output1 = tf.argmax(output,1)
	    #correct = tf.equal(tf.argmax(output,1),tf.argmax(y,1))
	    return dict(
	        x = x,
	        embeding=conv5,
	        output=output1,
	        saver = tf.train.Saver()
	    )

	def propagacion(self):
		""" Accepts a current character, initial state"""
		with tf.Session() as sess:
			writer = tf.summary.FileWriter('./Model/AreasVerdesTraining_v2/2METROS/CNNClass2m')
			tf.summary.FileWriter.add_graph(writer,sess.graph)
			#sess.run(tf.initialize_all_variables())
			self.arquitectura['saver'].restore(sess, self.checkpoint)
			feed_dict={self.arquitectura['x']: self.imagenes[:,0].tolist()}
			preds = sess.run([self.arquitectura['output']], feed_dict)
		return preds


if __name__ == '__main__':
	l_locs = []
	for item in range(1):
		clase_arquitectura = TT_modelo_RNC(300,'/home/israagus/Escritorio/Prueba/pickle/pickle_'+str(item),
		'/home/israagus/Escritorio/TT2_Cultivos/Paquete/Model/PESOS/Ejemplo1.ckpt')
		l = clase_arquitectura.propagacion()
		l_locs.append(list(l[0]))
		del clase_arquitectura
	print(type(l_locs[0]))
	print(l_locs[0])
	#print(np.argmax(clase_arquitectura.propagacion(),axis=0))
	#print(clase_arquitectura.deep_neural_convolutional_class_build())
	