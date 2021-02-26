from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def posts(request):
    postlist = Post.objects.all()
    return render(request, 'posts.html', {'postlist':postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post':post})

def newpost(request):
    if request.method == 'POST':
        if request.FILES['images']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                images=request.FILES['images'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                images=request.FILES['images'],
            )
        return redirect('/posts/')
    return render(request, 'newpost.html')