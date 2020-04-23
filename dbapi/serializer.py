from rest_framework import serializers


class Spending_Serializer(serializers.Serializer):
    """Formats data from ORM objects to JSON dict"""
    id = serializers.IntegerField()
    date = serializers.DateField(format="%d-%m-%Y")
    category = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    sum = serializers.IntegerField()
    common = serializers.BooleanField()
