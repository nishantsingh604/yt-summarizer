from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('generate-sum', views.generate_blog, name='generate-sum'),
    path('all-sum', views.blog_list, name='blog-list'),
    path('sum-details/<int:pk>/', views.blog_details, name='sum-details'),
]