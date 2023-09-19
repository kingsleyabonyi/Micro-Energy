from rest_framework import serializers


class CarbonSerializer(serializers.Serializer):
    diesel =  serializers.IntegerField()
    hydrogen = serializers.IntegerField()
    annual = serializers.IntegerField()
    carbonsavings = serializers.IntegerField()


    def multiple_of_num(diesel, hydrogen, annual):
        if diesel >= 20 or hydrogen  >= 20 or annual  >= 20:
            raise serializers.ValidationError('Not a multiple of ten')
