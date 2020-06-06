"""
Login Urls
"""
from django.urls import path

from login.views import (
    CustomLoginView
)

urlpatterns = [
    path('login', CustomLoginView.as_view()),
]
