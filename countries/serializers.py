from rest_framework import serializers
from countries.models import Countries

class CountrisSelializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('id', 'name', 'capital')