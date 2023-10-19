from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import webSerializer
from rest_framework.response import Response
from rest_framework import status

class webView(APIView):
    def get(self, request):
        get_data = webModel.objects.all()
        serializeData = webSerializer(get_data, many=True)
        return Response(serializeData.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializeData = webSerializer(data=request.data)
        if serializeData.is_valid():
            serializeData.save()
            return Response(serializeData.data, status=status.HTTP_201_CREATED)
        return Response(serializeData.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            getdata = webModel.objects.get(id=pk)
            serializdata = webSerializer(getdata, data=request.data, partial=True)
            if serializdata.is_valid():
                serializdata.save()
                return Response(serializdata.data, status=status.HTTP_200_OK)
            return Response(serializdata.errors, status=status.HTTP_400_BAD_REQUEST)
        except webModel.DoesNotExist:
            return Response({"status": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            getdata = webModel.objects.get(id=pk)
            getdata.delete()
            return Response({"status": "Data deleted"}, status=status.HTTP_204_NO_CONTENT)
        except webModel.DoesNotExist:
            return Response({"status": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
