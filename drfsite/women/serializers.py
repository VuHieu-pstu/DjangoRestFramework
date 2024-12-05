import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


'''Механизм работы сериализатора
class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = WomenModel('Thanh Thao', 'Thanh Thao sinh nam 1983, que o Long An')
    moder_sr = WomenSerializer(model)
    print(moder_sr.data, type(moder_sr.data), sep='\n')
    json = JSONRenderer().render(moder_sr.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"title": "Thanh Thao", "content": "Thanh Thao sinh nam 1983, que o Long An"}')
    data = JSONParser().parse(stream)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
'''
# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')


# сейчас работать с реальным моделью
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()