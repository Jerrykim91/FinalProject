from django.db import models


# Create your models here


# class data(models.Model): 
#     objects = models.Manager() # vs code 오류 제거용

#     user_name   = models.CharField(primary_key=True, max_length=50, blank=True) # 길이 50
#     res_name    = models.CharField(max_length=50)
#     food_name   = models.CharField(max_length=50)
#     rating      = models.IntegerField(max_length=5)
#     review      = models.CharField(max_length=30, blank=True)
#     PN        = models.BinaryField() # 바이너리 필드 
#     taste     = models.CharField(max_length=30, blank=True)


# class food_info(models.Model): 
#     objects = models.Manager() # vs code 오류 제거용

#     menu_kor   = models.TextField() # 길이 50
#     menu_eng   = models.TextField()
#     info       = models.TextField()
#     resource   = models.TextField()

    
'''
################################

#  데이터 필드 

# CharField    : 문자 타입 
# IntegerField : 숫자 타입
# BinaryField  : 바이너리 타입
# TextField    : 길이 제한 없음 

################################
# 모델 속성

## data

# user_name   : 사용자 이름
# res_name    : 사용자가 방문한 식당 이름
# food_name   : 사용자가 남긴 별점
# rating      : 사용자가 남긴 리뷰
# review      : 사용자가 남긴 리뷰에 대한 긍정/부정 여부
# PN          : 선호하는 맛 유형 
# taste       : 사용자가 남긴 맛 표용


## food_info

# menu_kor    : 한국음식 151종 한국어
# menu_eng    : 한국음식 151종 영어
# info        : 음식 설명
# resource    : 음식 설명 출처

################################

'''