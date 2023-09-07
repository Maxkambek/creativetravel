from .models import Region, Hotel, AmenityGroup, DescriptionStruct, RoomGroups, PolicyStruct
from rest_framework import serializers


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class AmenityGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenityGroup
        fields = '__all__'


class RoomGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomGroups
        fields = '__all__'


class DescriptionStructSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionStruct
        fields = '__all__'


class PolicyStructSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyStruct
        fields = '__all__'


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
