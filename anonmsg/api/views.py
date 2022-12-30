from django.shortcuts import render
from mer import models
from rest_framework import viewsets
from api.serializers import MsgstoreSerializer
from mer.models import Msgstore
class MsgstoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Msgstore.objects.all()
    serializer_class = MsgstoreSerializer


# Create your views here.
