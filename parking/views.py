from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsOwnerOfVehicleRecord
from rest_framework import viewsets
from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleRecord,]

    # tratamento para apenas ver o veiculo do usuario logado - filtrando apenas o carro do usuario
    def get_queryset(self):
        user = self.request.user

        if user.is_staff: # se o usuario esta autenticado
            return ParkingRecord.objects.all()
        else:
            return ParkingRecord.objects.filter(vehicle__owner__user=user)



class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser,]







