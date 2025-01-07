from django.urls import path
from . import views
from .views import LoginView
from .views import TestView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('test', TestView.as_view(), name='test'),
]
