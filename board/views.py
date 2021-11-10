from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.

def index(request):
    board_list = Board.objects.all().order_by("-created_date")
    boards = {'boards': board_list}
    return render(request, 'board/board.html', boards)

def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('board'))
    else:
        return render(request, 'board/write.html')
    
    
def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'board/detail.html', {'board': board})

def edit(request,id):
    board = Board.objects.get(pk=id)
    if(request.method=="POST"):
        board.author = request.POST['author']
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.save()
        return HttpResponseRedirect(reverse('board'))
    else:    
        return render(request, 'board/edit.html')


@csrf_exempt
def delete(request, id):
    board = Board.objects.get(pk=id)
    board.delete()
    return HttpResponseRedirect(reverse('board'))