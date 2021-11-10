
from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if password != password2:
            # 패스워드가 같지 않다고 알람
            return render(request, 'user/signup.html',{'error' : '패스워드가 동일하지 않습니다!'})
        else:
            if username =='' or password == '':
                return render(request, 'user/signup.html', {'error' : '사용자 이름과 비밀번호는 필수 값입니다!'})
            exist_user = get_user_model().objects.filter(username=username)

            if exist_user:
                return render(request, 'user/signup.html', {'error' : '사용자가 이미 존재합니다!'})  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                UserModel.objects.create_user(username=username, password=password)
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error':'사용자이름 혹은 패스워드를 확인해주세요!'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

# user/views.py
