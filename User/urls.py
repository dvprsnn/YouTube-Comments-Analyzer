from .views import user_create,login_view
from django.urls import path

urlpatterns = [
    path("create", user_create),
    path("login", login_view)
]
