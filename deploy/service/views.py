import numpy as np
import logging

from PIL import Image
from threading import Thread
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# from keras.preprocessing.image import image, ImageDataGenerator
# from keras.models import load_model


# logger = logging.getLogger(__name__)
# cursor = connection.cursor()
# model =load_model('.\\food_keras_model.h5')
# # Create your views here.
# print( '모델을 올린다 => ', type( model) )

# 텍스트 서비스 -> 여기 넣어줘 
def text(food_name):
    """
    food_img에서 던져 주는 값을 제대로 아웃풋을 낼 것
    """
    meau = '메뉴'
    return meau


# 음식 모델
@csrf_exempt
def food_img(request):
    """
    음식 모델
    """ 
    pass
    # if request.method == 'GET':
    #         print(1)
    #         return render(request, 'service/camera.html') 

    # elif request.method=='POST':
        
    #     print('123456')
    #     logger.debug('uplaod calll')
    #     print(request)
        
    #     img = request.FILES['img']

    #     #img = ContentFile(img.read())
    #     #img = image.(PATH, target_size=(224,224))
        
    #     path = default_storage.save('img.jpg', ContentFile(img.read()))
    #     print('.\\'+path)
    #     img = image.load_img('.\\'+path, target_size=(224,224))
    #     #print(img.size)# 이미지는 잘 읽어 와짐
    #     img_t = image.img_to_array(img)
    #     print('111')
    #     img_t = np.expand_dims(img_t, axis=0)
    #     print('222')
    #     img_num = img_t.astype('float32')/255.
        
    #     # PATH='C:\\Users\\admin\\Desktop\\편집\\김치찌개\\Img_119_0085.jpg'
    #     # pic = Image.open(PATH)
    #     # img = image.load_img(PATH, target_size=(224,224))
    #     # img_t = image.img_to_array(img)
    #     # img_t = np.expand_dims(img_t, axis=0)
    #     # img_num = img_t.astype('float32')/255.
    #     # print(img_num.size)

    #     print( '모델을 올린다 => ', type( model) )
    #     pred = model.predict_classes(img_num)
    #     print(pred)
        
    #     return render(request, 'service/camera.html') #redirect('/service/camera.html')

# 사진 촬영
def take_pic(click):
    """
    이미지 촬영 코드 
    """ 
    img ='이미지 촬영 데이터 '

    return img
