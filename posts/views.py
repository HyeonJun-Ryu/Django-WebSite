from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def list(request):
    posts = {'posts': Post.objects.all()}
    return render(request, 'list.html', posts)

def posting(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        post = Post(author=author, title=title, content=content)
        post.save()
        return HttpResponseRedirect('/posts')
    else:
        return render(request, 'posting.html')

