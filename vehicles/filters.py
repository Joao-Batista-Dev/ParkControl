from dj_rql.filter_cls import AutoRQLFilterClass
from vehicles.models import Vehicle, VehicleType


class VehicleFilter(AutoRQLFilterClass):
    MODEL = Vehicle


class VehicleTypeFilter(AutoRQLFilterClass):
    MODEL = VehicleType



