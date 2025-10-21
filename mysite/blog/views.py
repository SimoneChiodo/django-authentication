from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
  posts = Post.objects.all().order_by('-data_creazione')
  return render(request, "index.html", { "posts": posts })

@login_required(login_url='login')
def postDetail(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  return render(request, "postDetail.html", {"post": post})

@login_required(login_url='login')
def postCreate(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Post creato con successo!")
      return redirect('home') 
  else:
    form = PostForm()
  
  return render(request, "postCreate.html", {"form": form})

# Login
def login_view(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('home')
  else:
    form = AuthenticationForm()
  return render(request, "login.html", {"form": form})

def logout_view(request):
  logout(request)
  return redirect('login')
