from rest_framework import serializers
from . models import *

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = "__all__"
