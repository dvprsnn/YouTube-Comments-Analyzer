from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Home view
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),  # Home page route
    path("admin/", admin.site.urls),  # Admin page route
    path("user/", include("User.urls")),  # User section route
    path("youtube/", include("Vid_Comment.urls")),  # YouTube analysis section route
]
