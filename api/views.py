from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from etapp.models import item
from .serializers import itemserializer, userserializer
from django.contrib.auth.models import User


class itemCreateView(generics.CreateAPIView):
    queryset = item.objects.all()
    serializer_class = itemserializer


@api_view(['GET'])
def getdata(request):
    person = item.objects.all()
    serializer = itemserializer(person, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getuser(request):
    user = User.objects.all()
    serializer = userserializer(user, many=True)
    return Response(serializer.data)