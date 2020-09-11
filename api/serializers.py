from rest_framework import serializers
from . models import Pictures

# used to map db data
class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = '__all__'
        # fields = ('title')