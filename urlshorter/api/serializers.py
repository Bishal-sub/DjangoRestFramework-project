from rest_framework import serializers
from .models import shorturls


class shorturlsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = shorturls
        fields = ['id','original_url','short_url','create_at']
        read_only_fields = ['id','short_url','create_at']