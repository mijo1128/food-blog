"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    # ====================AUTHENTICATION==================== #
    path("admin/", admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # ====================CREATE==================== #
    path("create_my_blog/", views.create_my_blog, name="create"),
    path("register/", views.register_view, name="register"),
    # ====================READ==================== #
    path("filter_results/", views.filter_results, name="filter results"),
    path("blog/blog_detail/<str:pk>", views.blog_detail, name="detail"),
    path("members/view_members", views.view_members, name="view_members"),
    path("myprofile/", views.my_profile, name="my_profile"),
    path("viewprofile/", views.view_profile, name="view profile"),
    path("comment/<str:pk>/", views.blogcomment_detail, name="comment"),
    path("my-posts/", views.myblogposts, name="my-blog-posts"),
    # ====================UPDATE==================== #
    path("updateprofile/", views.updateprofile, name="update"),
    # ====================DELETE==================== #
    path("delete_blog/<str:pk>", views.delete_post, name="delete_blog"),
    path("members/delete.html/<str:pk>/", views.deleteMember, name="delete_member"),
    path(
        "members/delete_comment/<str:pk>/", views.delete_comment, name="delete_comment"
    ),
]
