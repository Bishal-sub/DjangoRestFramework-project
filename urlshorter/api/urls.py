from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.urlview.as_view(), name='post'),
    path('<str:code>/', views.redirectview.as_view(), name='shorturl'),
]