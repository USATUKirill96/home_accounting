from rest_framework import serializers

"""Предназначен для форматирования данных из базы в формат REST API. Объявленные классы соответствуют моделям, поля 
аналогичны. Поле TextField заменяется на CharField без указания максимальной длины. Названия атрибутов
соответствуют таковым у преобразуемой модели."""


class Spending_Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateTimeField()
    category = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    sum = serializers.IntegerField()
    common = serializers.BooleanField()
