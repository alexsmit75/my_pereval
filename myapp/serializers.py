from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import CustomUser, Coords, Image, PerevalAdded

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'fam', 'name', 'otc', 'phone']

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['id', 'latitude', 'longitude', 'height']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'data', 'title']

class PerevalAddedSerializer(WritableNestedModelSerializer):
    user = CustomUserSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = ['id', 'beautyTitle', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'winter_level', 'summer_level', 'autumn_level', 'spring_level', 'images', 'status']
