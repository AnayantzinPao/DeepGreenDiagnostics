import tensorflow as tf
import numpy as np
import pickle
from sklearn.metrics import confusion_matrix

###############
##Red neuronal
###############
class TT_modelo_retrain:
    def __init__(self, batch_size, path_pickle, path_checkpoint):
        self.checkpoint = path_checkpoint
        self.imagenes = " "
        #np.array(pickle.load(open(path_pickle+".pickle","rb"))) #Es todo el archivo pickle que contenga las imágenes
        self.batch_size = batch_size #tamaño del pickle

    def conv2d(self,x, W,name,padd,strid=[1,1,1,1]):
    #El stride de esa función no reduce el tamaño de la imagen
        return tf.nn.conv2d(x, W, strides=strid, padding=padd,name=name)

    def maxpool2d(self,x,ks,st):
    #           El st de esta función reduce la imagen a la mitad
        return tf.nn.max_pool(x, ksize=ks, strides=st, padding='SAME')

    def reset_graph(self):
        """
        Limpia la grafica de tensorboard.
        """
        if 'sess' in globals() and sess:
            sess.close()
        tf.reset_default_graph()

    def deep_neural_convolutional_class(self,
                                        batch_size=20,
                                        image_size=[200,200],
                                        Drop_prob=1.0,
                                        learning_rate = 1e-2,
                                        n_nodes_hl0 = 2000,
                                        n_nodes_hl1 = 1000,
                                        n_nodes_hl2 = 500,
                                        n_nodes_hl3 = 100,
                                        n_classes=8
                                        ):
    
        self.reset_graph()
        #Place holder de entrada 
        x= tf.placeholder(tf.float32,[batch_size,image_size[0],image_size[1],3], name='placeholder_img_entrada')
        y=tf.placeholder('float',name='placeholder_one_hot')
      
        #Diccionario de pesos convolucionales 
        with tf.name_scope('pesos_bias') as scope1:
            weigths={"w_conv1":tf.Variable(tf.random_normal([5,5,3,32]),name='Pesos_1_32'),
                     "w_conv2":tf.Variable(tf.random_normal([5,5,32,64]),name='Pesos_1_64'),
                     "w_conv3":tf.Variable(tf.random_normal([3,3,64,128]),name='Pesos_1_128'),   
                     "w_conv4":tf.Variable(tf.random_normal([5,5,128,256]),name='Pesos_1_256'),
                     "w_conv5":tf.Variable(tf.random_normal([5,5,256,512]),name='Pesos_1_512'),
                     #"w_conv6":tf.Variable(tf.random_normal([5,5,512,1024]),name='Pesos_1_1024'),
                    }
            #Diccionario de bias
            biases={"b_conv1":tf.Variable(tf.random_normal([32]),name='Bias_1_32'),
                    "b_conv2":tf.Variable(tf.random_normal([64]),name='Bias_1_64'),
                    "b_conv3":tf.Variable(tf.random_normal([128]),name='Bias_1_128'),
                    "b_conv4":tf.Variable(tf.random_normal([256]),name='Bias_1_256'),
                    "b_conv5":tf.Variable(tf.random_normal([512]),name='Bias_1_512'),
                    #"b_conv6":tf.Variable(tf.random_normal([1024]),name='Bias_1_1024'),
                   }

        #Extractor de características
        with tf.name_scope('capas_conv') as scope2:
            conv1=tf.nn.relu(self.conv2d(x,weigths["w_conv1"],'Capa_Conv_1','SAME')+biases["b_conv1"],name='Func_relu_1')
            conv1=tf.nn.dropout(conv1,Drop_prob)
            conv1=self.maxpool2d(conv1,ks=[1,2,2,1],st=[1,2,2,1])
            #imagen resultante de 100x100x32
            print(conv1)

            conv2=tf.nn.relu(self.conv2d(conv1,weigths["w_conv2"],'Capa_Conv_2','SAME')+biases["b_conv2"],name='Func_relu_2')
            conv2=tf.nn.dropout(conv2,Drop_prob)
            conv2=self.maxpool2d(conv2,ks=[1,2,2,1],st=[1,2,2,1])
            #imagen resultante de 50x50x64
            print(conv2)

            conv3=tf.nn.relu(self.conv2d(conv2,weigths["w_conv3"],'Capa_Conv_3','VALID')+biases["b_conv3"],name='Func_relu_3')
            conv3=tf.nn.dropout(conv3,Drop_prob)
            conv3=self.maxpool2d(conv3,ks=[1,2,2,1],st=[1,2,2,1])
            #imagen resultante de 24x24x128
            print(conv3)

            conv4=tf.nn.relu(self.conv2d(conv3,weigths["w_conv4"],'Capa_Conv_4','SAME')+biases["b_conv4"],name='Func_relu_4')
            conv4=tf.nn.dropout(conv4,Drop_prob)
            conv4=self.maxpool2d(conv4,ks=[1,2,2,1],st=[1,2,2,1])
            #imagen resultante de 12x12x256
            print(conv4)

            conv5=tf.nn.relu(self.conv2d(conv4, weigths["w_conv5"],'Capa_Conv_5','SAME')+biases["b_conv5"],name='Func_relu_5')
            conv5=tf.nn.dropout(conv5,Drop_prob)
            conv5=self.maxpool2d(conv5,ks=[1,2,2,1],st=[1,2,2,1])
            #vector para clasificar de 6x6x512
            print(conv5)
            
            #conv6=tf.nn.relu(conv2d(conv5, weigths["w_conv6"],'Capa_Conv_6','SAME')+biases["b_conv6"],name='Func_relu_6')
            #conv6=tf.nn.dropout(conv6,Drop_prob)
            #conv6=maxpool2d(conv6,ks=[1,4,4,1],st=[1,4,4,1])
            #vector para clasificar de 1x1x1024
            #print(conv6)

            #Embeding, son las caracteristicas fonales que se pasarán al MLP o red completamente conectada para clasifiacar
            embdeding=tf.reshape(conv5,[batch_size,6*6*512],name='Embeding')
            print(embdeding)
        
        #Red perceptron, declaración de capas, son diccionarios de pesos y bias.
        with tf.name_scope('capas_clasificador') as scope3:
            hidden_0_layer = {'weights':tf.Variable(tf.random_normal([6*6*512, n_nodes_hl0]),name='Capa_oculta_pesos_0'),
                              'biases':tf.Variable(tf.random_normal([n_nodes_hl0]),name='Capa_oculta_bias_0')}

            hidden_1_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl0, n_nodes_hl1]),'Capa_oculta_pesos_1'),
                              'biases':tf.Variable(tf.random_normal([n_nodes_hl1]),name='Capa_oculta_bias_1')}

            hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2]),'Capa_oculta_pesos_2'),
                              'biases':tf.Variable(tf.random_normal([n_nodes_hl2]),name='Capa_oculta_bias_2')}
            
            hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3]),'Capa_oculta_pesos_3'),
                              'biases':tf.Variable(tf.random_normal([n_nodes_hl3]),name='Capa_oculta_bias_3')}

            output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes]),'Capa_salida_pesos'),
                            'biases':tf.Variable(tf.random_normal([n_classes]),name='Capa_salida_bias'),}
        
        #W*P + B 
        with tf.name_scope('op_clasificador') as scope4:
            
            l0 = tf.add(tf.matmul(embdeding,hidden_0_layer['weights'],name='Matmul_l0'), hidden_0_layer['biases'],name='Suma_Pesos_Bias_0')
            l0 = tf.nn.relu(l0,name='l0_relu_0')

            l1 = tf.add(tf.matmul(l0,hidden_1_layer['weights'],name='Matmul_l1'), hidden_1_layer['biases'],name='Suma_Pesos_Bias_1')
            l1 = tf.nn.relu(l1,name='l1_relu_1')

            l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights'],name='Matmul_l2'), hidden_2_layer['biases'],name='Suma_Pesos_Bias_2')
            l2 = tf.nn.relu(l2,name='l2_relu_2')
            
            l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights'],name='Matmul_l3'), hidden_3_layer['biases'],name='Suma_Pesos_Bias_3')
            l3 = tf.nn.relu(l3,name='l3_relu_3')

            output = tf.matmul(l3,output_layer['weights'],name='Matmul_out') + output_layer['biases']
            output1 = tf.argmax(output,1)

        with tf.name_scope('costo_y_optimizador') as scope5:
            cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits_v2(logits=output, labels=y,name='cross_entropy_with_logits'),name='reduce_mean')
            optimizer = tf.train.AdamOptimizer(name='Adam').minimize(cost,name='minimo')

        tf.summary.scalar("costo",cost)
        correct = tf.equal(tf.argmax(output,1),tf.argmax(y,1),name='valores_correctos')
        accuracy = tf.reduce_mean(tf.cast(correct,'float'),name='Promedio_exactitud') #porcentaje de error
        tf.summary.scalar("accuracy",accuracy)
        summaries = tf.summary.merge_all()
        
        return dict(
            x = x,
            y = y,
            embeding=conv5,
            output=output1,
            saver = tf.train.Saver(),
            total_loss = cost,
            train_step = optimizer,
            summaries = summaries,
            accuracy = accuracy
        )

    def training(self, G,
                nameBatch,
                numbatch, 
                num_epochs,
                learning_rate = 1e-2, 
                num_steps = 15, 
                batch_size = 20, 
                verbose = True, 
                save = None,
                checkpoint = None,
                path_restore = None):
        """This is the method to retrain the model. The method needs
        the name of the principal training model to load the last wights
        and biases.
        Param: 
        G - Feed dictionary
        nameBatch - The path of the pickle file
        num_epochs - How many batch will be load
        learning_rate - The deaful learning rate for this model 
        num_steps - The number of iteration for the model 
        batch_size = The number of images that will be propagation  
        verbose - Show the number of data in one iteration 
        save - The new name of the cktp file (wights and biases)
        checkpoint - Is the name of the last file of wights and biases
        """
        tf.set_random_seed(2345)
        print('Start training')
        total_loss = 0
        with tf.Session() as sess:
            if path_restore != None:
                writer = tf.summary.FileWriter(path_restore)
                tf.summary.FileWriter.add_graph(writer,sess.graph)
            else:
                writer = tf.summary.FileWriter("./Model/New")
                tf.summary.FileWriter.add_graph(writer,sess.graph)
            sess.run(tf.global_variables_initializer())
            if checkpoint != None:
                ENCname=checkpoint
                G['saver'].restore(sess, ENCname)
            training_losses = []
            for epoch in range(int(num_epochs)):
                epoch_loss = 0
                for key in range(numbatch):
                    data=np.array(pickle.load(open(nameBatch+"Train_"+str(key)+".pickle","rb")))
                    dim,var=data.shape
                    for j in range(int(dim/batch_size)):
                        epoch_x=data[batch_size*(j):batch_size*(j+1),0].tolist()
                    
                        epoch_Y=data[batch_size*(j):batch_size*(j+1),1].tolist()

                        feed_dict={G['x']: epoch_x,
                                   G['y']: epoch_Y,
                                  }
                    
                        total_loss,_,summ = sess.run([G["total_loss"],G["train_step"],G["summaries"]],feed_dict)#""",G["summaries"]"""
                    epoch_loss += total_loss
                    writer.add_summary(summ,epoch)
                if verbose:
                    print("Average training loss for Epoch", epoch, ":", epoch_loss)
                training_losses.append(epoch_loss)

            if save != None:
                ENCname=save
                G['saver'].save(sess, ENCname)
        return training_losses

    def check_net(self, g, test, checkpoint, path_writer):
        """This function allows to meet the accuracy and the list of predictions
        g - Is the feed dict used to train the net
        test - Is the batch of testing
        checkpoint - Is the path to the file of Weights and biases"""
        with tf.Session() as sess:
            writer = tf.summary.FileWriter(path_writer)
            tf.summary.FileWriter.add_graph(writer,sess.graph)
            g['saver'].restore(sess, checkpoint)
            feed_dict={g['x']: test[:,0].tolist(),g['y']: test[:,1].tolist()}
            preds,accuracy = sess.run([g['output'],g['accuracy']], feed_dict)
        return preds,accuracy