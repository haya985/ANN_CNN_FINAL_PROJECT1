from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import gdal
from keras.layers import Dense
from keras import Sequential
from keras.utils import np_utils
from PIL import Image
import filereader
import tempreader
#import scipy.misc
def main(row,col,bands,datapath,imgpath):
    train_cycle,c_c,neurons=tempreader.main()
    def ReadBilFile(bil,bands,pixels):
        extract_band=1
        image=np.zeros([pixels,bands], dtype=np.uint8)
        gdal.GetDriverByName('EHdr').Register()
        img = gdal.Open(bil)
        while bands>=extract_band:
            bandx = img.GetRasterBand(extract_band)
            datax = bandx.ReadAsArray()
            temp=datax
            store=temp.reshape(pixels)
            for i in range(pixels):
                image[i][extract_band-1]=store[i]
            extract_band=extract_band+1
        return image


    """to load label and training data here"""
    
    pixels=row*col
    #imgpath='mnist\subfebformosat2'
    x_test = ReadBilFile(imgpath,bands,pixels)
    y_test = np.zeros([220616], dtype=np.uint8)
    '''this is to be generalised'''
    y_train = np.zeros([60], dtype=np.uint8)
    for i in range (10):
        y_train[i]=1
    for i in range (10):
        y_train[10+i]=2
    for i in range (10):
        y_train[20+i]=3
    for i in range (10):
        y_train[30+i]=4
    for i in range (10):
        y_train[40+i]=5
    for i in range (10):
        y_train[50+i]=6
    '''
    till here
    '''
    values=[]
    for address in datapath:
        with open(address,"rb") as f:
            block = f.read()
            for ch in block:
                # x = ord(ch)
                values.append(ch)

    #print(len(values))
    
    ll=(len(values))
    #l=ll/2
    '''from here'''
    f_in=np.zeros([240], dtype=np.uint8)
    x=0
    for i in range(ll):
        if(i%2==1):
            f_in[x]=values[i]
            x+=1

    rex=60

    x_train=f_in.reshape(rex,bands)  
    
    
    
    """loading of data ends here"""

    print(x_train.shape)
    print(y_train.shape)
    print(x_test.shape)
    print(y_test.shape)
    
    
    
    seed = 7
    np.random.seed(seed)
    
    
    # normalize inputs from 0-255 to 0-1
    x_train = x_train / 255
    x_test = x_test / 255
    
    num_pixels = bands
    
    
    # one hot encode outputs
    
    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)
    num_classes = c_c
    y_test_new=np.zeros([pixels,c_c], dtype=np.uint8)
    
    # define baseline model
    
    def baseline_model():
	    # create model
	    model = Sequential()
	    model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
	    model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
	    # Compile model
	    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	    return model



    # build the model
    model = baseline_model()
    # Fit the model
    #model.fit(x_train, y_train, validation_data=(x_test, y_test_new), epochs=10, batch_size=2, verbose=0)
    # Final evaluation of the model
    #scores = model.evaluate(x_test, y_test_new, verbose=0)
    
    model.fit(x_train, y_train, batch_size=32, epochs=train_cycle, verbose=2)
    y_test_new = model.predict(x_test, batch_size=32)
    y_test=np.argmax(y_test_new, axis = 1)

    print ("this is predicted output")
        #print("Baseline Error: %.2f%%" % (100-scores[1]*100))

                    
    img=x_test.reshape(row, col,bands)
    
    plt.imshow(img)
    plt.show()
    result = Image.fromarray((img*255).astype('uint8'))
    result.save('image.tiff')
    
    img=y_test.reshape(row, col)
    plt.imshow(img)
    plt.show()
    result = Image.fromarray(((img*255)/c_c).astype('uint8'))
    result.save('cnn.tiff')
    #print ("img created") 
    #scipy.misc.toimage(img).save('cnn_classified.jpg')
    print ("img created") 
    