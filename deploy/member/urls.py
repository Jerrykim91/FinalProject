
# member\urls.py
# 경로 설정 -> 장고의 urls -> path
from django.urls import path

# 현재 패키지 => view 모듈(views.py)에서 호출 
from . import views 



# 경로 생성 => 함수형 뷰를 호출 
# member/views.py로 부터 => html을 생성 할때 마다 경로 생성 
# path('urls이름', views.urls이름, name = 'urls이름')



urlpatterns = [

    # member - Public

    # path('main', views.main),
    # path('sign_up', views.sign_up),
    # path('sign_in', views.sign_in),

]