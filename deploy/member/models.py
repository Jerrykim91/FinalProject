from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here
# 일단 주석 



# class join(AbstractUser): pass
    # objects  = UserManager() 

    # user_id    = models.CharField(primary_key=True, max_length=20, blank=True)
    # user_pw    = models.CharField(max_length=30, blank=True)
    # j_foodex   = models.BinaryField() # 안하는걸로 
    # j_taste    = models.CharField(max_length=50, blank=True)
    
'''
################################
# 모델 속성 

# user_id    : 유저 아이디
# user_pw    : 유저 패스워드 
# 안열것 같어

# user_pw_re : 패스워드 체크
# j_taste    : 선호하는 맛 유형 -> str()

################################

#  데이터 필드 

# CharField    : 문자 타입 
# IntegerField : 숫자 타입
# BinaryField  : 바이너리 타입
# TextField    : 길이 제한 없음 

################################

'''