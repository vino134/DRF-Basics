from rest_framework import serializers
from .models import *

class Products_serializers(serializers.ModelSerializer):

    class Meta:

        model=Product
        fields='__all__'

class Products_serializers2(serializers.ModelSerializer):

    class Meta:

        model=Product
        fields=['product_name']


        
