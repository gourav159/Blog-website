from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.bloghome, name='home'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('detail', views.detail, name='detail'),
    path('<str:slug>/', views.blogpost, name="blogpost"),
    path('postComment', views.postComment, name="postComment"),


]