from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from dogs.models import *
from dogs.serializers import *
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'dogs': reverse('dogs:dog-list', request=request, format=format),
        'breeds': reverse('dogs:breed-list', request=request, format=format)
    })


class DogList(generics.ListCreateAPIView):
    
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedList(generics.ListCreateAPIView):
    
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer





# @api_view(['GET', 'POST'])
# def dog_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         dogs = Dog.objects.all()
#         serializer = DogSerializer(dogs, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = DogSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @api_view(['GET', 'PUT', 'DELETE'])
# def Dog_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         dog = Dog.objects.get(pk=pk)
#     except Dog.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = DogSerializer(dog)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = DogSerializer(dog, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         dog.delete()
#         return HttpResponse(status=204)        



# @api_view(['GET', 'POST'])
# def breed_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         breeds = Breed.objects.all()
#         serializer = BreedSerializer(breeds, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BreedSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @api_view(['GET', 'PUT', 'DELETE'])
# def breed_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         breed = Breed.objects.get(pk=pk)
#     except Breed.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = BreedSerializer(breed)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BreedSerializer(breed, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         breed.delete()
#         return HttpResponse(status=204)             