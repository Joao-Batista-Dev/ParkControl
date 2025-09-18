from parking.models import ParkingRecord, ParkingSpot
from rest_framework import serializers

class ParkingRecordSerializer(serializers.ModelSerializer):
   class Meta:
        model = ParkingRecord
        fields = '__all__'


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'