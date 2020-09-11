# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# another option using def endpoints
# from django.http import HttpResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from .models import Pictures
from .serializers import PicturesSerializer
from rest_framework import viewsets

# used to get db data
class PicturesViewSet(viewsets.ModelViewSet):
    queryset = Pictures.objects.all()
    serializer_class = PicturesSerializer


# another option used to get db data
# class PicturesList(APIView):
#     def get_picture(self, request):
#         pictures1 = Pictures.objects.all()
#         serializer = PicturesSerializer(pictures1, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post_picture(self, request):
#         pass

#     def download_picture(self, request):
#         pass

#     def delete_picture(request, picture_id):
#         try:
#             picture1 = Pictures.objects.get(id=picture_id)
#         except Pictures.DoesNotExist:
#             return HttpResponse(status=404)
#         if request.method == 'GET':
#             serializer = PicturesSerializer(post)
#             return Response(serializer.data)
#         elif request.method == 'DELETE':
#             picture1.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     #   pass


        

    

