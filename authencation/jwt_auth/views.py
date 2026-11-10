from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import render

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def check(request):

    if request.method == "GET":
        return Response({
            "message": "This is public API"
        })

    elif request.method == "POST":
        return Response({
            "message": f"Welcome {request.user.username}"
        })
        
def home(request):
    return render(request,'index.html')