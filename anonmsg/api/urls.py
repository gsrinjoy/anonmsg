from django.contrib import admin
from django.urls import path,include
from mer import urls
from api.views import MsgstoreViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'msgstore', MsgstoreViewSet)


urlpatterns = [
    path('',include(router.urls))
    
]