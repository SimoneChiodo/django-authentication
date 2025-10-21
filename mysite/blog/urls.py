from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>/', views.postDetail, name='post_detail'),
    path('new/', views.postCreate, name="post_create"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
