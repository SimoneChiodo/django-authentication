from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def home(request):
  posts = Post.objects.all().order_by('-data_creazione')
  return render(request, "index.html", { "posts": posts })

def postDetail(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  return render(request, "postDetail.html", {"post": post})

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
