from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .models import Person
from .serializers import PersonSerializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class createprofile(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    permission_classes = [IsAuthenticated]
    
class profiledetail(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    
