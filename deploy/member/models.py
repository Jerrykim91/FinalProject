from django.db import models

# Create your models here.



# 일단 주석 
# from django.db import models
# from django.contrib.auth.models import AbstractUser, UserManager


class join(AbstractUser): pass
    # objects  = UserManager() 

    # birth_date = models.CharField(max_length=6, null=True , blank= True)
    # name  = models.CharField( '성명', max_length=30, blank=True ) # 본명


'''

# 모델 속성 

# user_id    : 유저 아이디
# user_pw    : 유저 패스워드 
# user_pw_re : 패스워드 체크
# j_foodex   : 한국 음식 먹어본 경험 
# j_taste    : 선호하는 맛 유형 

'''