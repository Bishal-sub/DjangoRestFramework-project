from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path
from .views import check

urlpatterns = [
    
    path('token_obtain',TokenObtainPairView.as_view(),name='token_obtain'),
    path('token_refresh',TokenRefreshView.as_view(),name='token_refresh'),
    
    path('check',check,name='check')
]
