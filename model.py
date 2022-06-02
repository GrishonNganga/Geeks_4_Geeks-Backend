from tensorflow import keras
model = keras.models.load_model('election_model.h5')
# from keras.preprocessing import image
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import PIL

def predict(imgage1):
    img = tf.keras.utils.load_img(imgage1, target_size = (180,180))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images)
    names = ["AFANDI", "CELINE", "GRISHON", "JULIUS", "KEITH", "NEIL", "SOLOMON"]
    pred = names[np.argmax(classes)]
    return pred