
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from .models import shorturls
from .serializers import shorturlsSerializer

import secrets
import string


class urlview(APIView):

    def post(self, request):

        serializer = shorturlsSerializer(data=request.data)

        if serializer.is_valid():

            # Generate a unique short code
            while True:
                code = ''.join(
                    secrets.choice(
                        string.ascii_letters + string.digits
                    )
                    for _ in range(7)
                )

                if not shorturls.objects.filter(short_url=code).exists():
                    break

            # Save original URL and short code
            instance = serializer.save(short_url=code)

            # Generate working short URL
            short_link = request.build_absolute_uri(
                reverse('shorturl', kwargs={'code': code})
            )

            return Response(
                {
                    "message": "Short URL created successfully",
                    "original_url": instance.original_url,
                    "short_code": code,
                    "short_url": short_link
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class redirectview(APIView):

    def get(self, request, code):

        instance = get_object_or_404(
            shorturls,
            short_url=code
        )

        return redirect(instance.original_url)
