import os
import cv2
import pandas as pd
import numpy as np
from keras.applications import DenseNet121
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from keras.utils.np_utils import to_categorical
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential, load_model, Model
from keras.layers import AveragePooling2D, Dropout, Flatten, Dense, Input, Activation
from keras.applications import NASNetMobile
from keras.optimizers import Adam

from keras.layers import  MaxPooling2D
from keras.layers import Convolution2D
from lime import lime_image
from skimage.segmentation import mark_boundaries
import matplotlib.pyplot as plt

X = []
Y = []
path = "Dataset"
'''
for root, dirs, directory in os.walk(path):
    for j in range(len(directory)):
        if 'Thumbs.db' not in directory[j]:
            img = cv2.imread(root+"/"+directory[j])
            img = cv2.resize(img, (32, 32))
            label = 0
            name = os.path.basename(root)
            if name == "real":
                label = 1
            X.append(img)
            Y.append(label)
            print(j)
    
X = np.asarray(X)
Y = np.asarray(Y)

np.save('model/X',X)
np.save('model/Y',Y)
'''
X = np.load('model/X.npy')
Y = np.load('model/Y.npy')


X = X.astype('float32')
X = X/255

indices = np.arange(X.shape[0])
np.random.shuffle(indices)
X = X[indices]
Y = Y[indices]
Y = to_categorical(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2) #split dataset into train and test

print(X.shape)
print(Y.shape)
print(np.unique(Y, return_counts=True))
'''
densenet = DenseNet121(input_shape=(X_train.shape[1], X_train.shape[2], X_train.shape[3]), include_top=False, weights='imagenet')
for layer in densenet.layers:
    layer.trainable = False
headModel = densenet.output
headModel = AveragePooling2D(pool_size=(1, 1))(headModel)
headModel = Flatten(name="flatten")(headModel)
headModel = Dense(128, activation="relu")(headModel)
headModel = Dropout(0.3)(headModel)
headModel = Dense(y_train.shape[1], activation="softmax")(headModel)
densenet_model = Model(inputs=densenet.input, outputs=headModel)
densenet_model.compile(optimizer = Adam(learning_rate=0.0001), loss = 'categorical_crossentropy', metrics = ['accuracy'])
if os.path.exists("model/densenet_weights.hdf5") == False:
    model_check_point = ModelCheckpoint(filepath='model/densenet_weights.hdf5', verbose = 1, save_best_only = True)
    hist = densenet_model.fit(X_train, y_train, batch_size = 64, epochs = 40, validation_data=(X_test, y_test), callbacks=[model_check_point], verbose=1)
    f = open('model/densenet_history.pckl', 'wb')
    pickle.dump(hist.history, f)
    f.close()    
else:
    densenet_model.load_weights("model/densenet_weights.hdf5")
predict = densenet_model.predict(X_test)
predict = np.argmax(predict, axis=1)
y_test1 = np.argmax(y_test, axis=1)
acc = accuracy_score(y_test1, predict)
print(acc)
'''

nasnet_model = NASNetMobile(input_shape=(X_train.shape[1], X_train.shape[2], X_train.shape[3]), include_top=False, weights=None)
for layer in nasnet_model.layers:
    layer.trainable = False
nasnet_model = Sequential()
nasnet_model.add(Convolution2D(32, (3 , 3), input_shape = (X_train.shape[1], X_train.shape[2], X_train.shape[3]), activation = 'relu'))
nasnet_model.add(MaxPooling2D(pool_size = (2, 2)))
nasnet_model.add(Convolution2D(32, (3, 3), activation = 'relu'))
nasnet_model.add(MaxPooling2D(pool_size = (2, 2)))
nasnet_model.add(Flatten())
nasnet_model.add(Dense(units = 256, activation = 'relu'))
nasnet_model.add(Dense(units = y_train.shape[1], activation = 'softmax'))
nasnet_model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
if os.path.exists("model/nasnet_weights.hdf5") == False:
    model_check_point = ModelCheckpoint(filepath='model/nasnet_weights.hdf5', verbose = 1, save_best_only = True)
    hist = nasnet_model.fit(X_train, y_train, batch_size = 64, epochs = 40, validation_data=(X_test, y_test), callbacks=[model_check_point], verbose=1)
    f = open('model/nasnet_history.pckl', 'wb')
    pickle.dump(hist.history, f)
    f.close()    
else:
    nasnet_model.load_weights("model/nasnet_weights.hdf5")
'''
predict = nasnet_model.predict(X_test)
predict = np.argmax(predict, axis=1)
y_test1 = np.argmax(y_test, axis=1)
acc = accuracy_score(y_test1, predict)
print(acc)
'''

image = cv2.imread("Dataset/fake/008BYSE725.jpg")
img = cv2.resize(image, (32,32))
im2arr = np.array(img)
im2arr = im2arr.reshape(1,32,32,3)
img = np.asarray(im2arr)
img = img.astype('float32')
img = img/255
preds = nasnet_model.predict(img)
predict = np.argmax(preds)
print(predict)

# Create LIME image explainer
explainer = lime_image.LimeImageExplainer()

# Generate explanation
explanation = explainer.explain_instance(img[0], nasnet_model.predict, top_labels=2, hide_color=0, num_samples=1000)

# Visualize the explanation
temp, mask = explanation.get_image_and_mask(explanation.top_labels[0], positive_only=True, num_features=5, hide_rest=True)
print(temp.shape)
print(mask.shape)
cv2.imshow("t", cv2.resize(temp, (128, 128)))
cv2.imshow("m", cv2.resize(mask (128, 128)))
cv2.waitKey(0)
plt.figure(figsize=(3,3))
plt.imshow(mark_boundaries(temp / 2 + 0.5, mask))
plt.axis('off')
plt.title("LIME Explanation")
plt.show()


                   
