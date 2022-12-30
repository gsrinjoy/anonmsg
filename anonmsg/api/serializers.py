from rest_framework import serializers
from mer.models import Msgstore


class MsgstoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Msgstore
        fields = "__all__"