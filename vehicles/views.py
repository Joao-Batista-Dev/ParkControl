from rest_framework.permissions import DjangoModelPermissions
from core.permissions import IsOwnerOfVehicleRecord
from rest_framework import viewsets
from vehicles.models import Vehicle, VehicleType
from vehicles.serializers import VehicleSerializer, VehicleTypeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleRecord]

    # tratamento para apenas ver o veiculo do usuario logado - filtrando apenas o carro do usuario
    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Vehicle.objects.all()
        else:
            return Vehicle.objects.filter(owner__user=user)


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions,]





