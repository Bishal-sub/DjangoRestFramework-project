from django.urls import path
from . import views

urlpatterns = [
    path("createprofile/", views.createprofile.as_view(), name="create"),
    path("profiledetail/", views.profiledetail.as_view(), name="profiledetail"),
]
