
from django.shortcuts import render, redirect

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/result')
    else:
        return redirect('/sign-in')

def result(request):

    return render(request, 'result/test.html')


