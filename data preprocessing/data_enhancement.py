import os
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator,array_to_img,img_to_array,load_img
datagen=ImageDataGenerator(
      rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      rescale=1./255,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')
      
path='/home/zdf/workspace/Machine_Learning/scene_classification/keras/train1/1/'
imglist = os.listdir(path)
for img in imglist:
    filename=os.path.splitext(img)[0]
    img = os.path.join(path, img)
    img=load_img(img)
    img = img.resize((224, 224))
    x=img_to_array(img)
    x=x.reshape((1,)+x.shape)

    i=0
    for batch in datagen.flow(x,batch_size=1,
                         save_to_dir='123/',save_prefix=filename,save_format='jpg'):
        i+=1
        if i>=1:
            break
            
print('========done=====')
