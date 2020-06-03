
# member\urls.py
from django.urls import path
from . import views 

# member 
urlpatterns = [

    # path('main', views.main),
    path('sign_up', views.sign_up),
    path('sign_in', views.sign_in),

]