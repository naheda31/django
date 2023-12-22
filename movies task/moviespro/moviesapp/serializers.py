from rest_framework import serializers
from . models import Movies



class Moviesserializers(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields=['id','name','language','hero']