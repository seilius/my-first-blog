#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import PostForm

from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-pk')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk);
    return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
    form = PostForm()

    if (request.method == "POST"):  # request method 가 무엇인가?
        form = PostForm(request.POST)
        if form.is_valid():  # 유효성 검사(null 체크 및 타입 체크)
            post = form.save(commit=False)  # 넘겨진 데이터를 바로 Post 모델에 저장하지 말것
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('/')  # 메인으로 요청을 보낸다.
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

