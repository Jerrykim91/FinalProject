from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

"""
# 모델 설계전 구상 

#
  # 1. 회원가입 페이지에 사용자 정보 수집
    -  유저아이디, 유저 패스워드, 패스워드 체크, 
# 2. 다 입력하고 회원가입 클릭 => 메인페이지 혹은 팝업으로 가입 확인 메세지 출력

# 3. 확인 메세지 이동 관련 클릭 => 메인이동 & 로그인 

# 4. 로그인 화면 이동 => 입력 => 사용자 계정 패스워드 입력후 로그인 클릭 => '로그인하세요'가 뜬 그 화면으로 이동  

# 4-1. 아이디, 비밀번호 찾기, 뒤로가기(혹은 홈으로) (번외)

# 5. 록인 세션 유지 => 자유로운 위치에서 로그아웃 

# 6. 회원 정보수정 => 회원정보 수정 페이지 이동 => 비밀번호, 풀네임, 생년월일, 이메일, 성별, 수정 

"""

# Create your views here.

def sign_up():
    '''
    회원가입
    '''
    pass


def sign_in():
    '''
    로그인
    '''
    pass

 
def main():
    '''
    메인
    '''
    pass
