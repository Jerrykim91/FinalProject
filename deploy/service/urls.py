
# service\urls.py

from django.urls import path
from . import views 

# service
urlpatterns = [

    # path('take_pic', views.take_pic),
    path('food_img', views.food_img),
    path('text', views.text),

]