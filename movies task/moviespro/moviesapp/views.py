from django.shortcuts import render
from . models import Movies
from . serializers import Moviesserializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
@api_view(['GET','POST'])
def movie_data(request):
    if request.method == 'GET':
        movie=Movies.objects.all()
        serializer=Moviesserializers(movie,many=True)
        return JsonResponse (serializer.data,safe=False)
    if request.method == 'POST':
        serializer=Moviesserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def movie_details(request,id):
    try:
        movie=Movies.objects.get(pk=id)
    except movie.DoesnotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=Moviesserializers(movie)
        return JsonResponse (serializer.data)
    elif request.method == 'PUT':
        serializer=Moviesserializers(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


