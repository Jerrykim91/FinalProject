from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from django.views.decorators.csrf import csrf_exempt

"""
# 모델 설계전 구상 

# url을 치면 메인페이지가 뜬다. 

"""


# Create your views here.

def sign_up(request):
    '''
    회원가입
    '''
    if request.method == 'GET':
        return render(request,'member/sign_up.html')
    elif request.method == 'POST':
        # id = request.POST['username']
        # pw = request.POST['password']
        pass


def sign_in(request):
    '''
    로그인
    '''
    if request.method == 'GET':
        return render(request,'member/sign_in.html')
    elif request.method == 'POST':
        # id = request.POST['username']
        # pw = request.POST['password']
        pass
 

def home(request):
    '''
    메인 
    '''
    if request.method == 'GET':
        return render(request,'member/home.html')
    
