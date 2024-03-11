from rest_framework import serializers
from .models import todo

class todoSerializers(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('id','title','description','completed')