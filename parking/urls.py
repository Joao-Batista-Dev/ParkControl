from django.urls import path, include
from rest_framework.routers import DefaultRouter
from parking.views import  ParkingRecordViewSet, ParkingSpotViewSet


router = DefaultRouter()
router.register('parking/records', ParkingRecordViewSet, basename='parking-record')
router.register('parking/spots', ParkingSpotViewSet, basename='parking-spot')

urlpatterns = [
    path('', include(router.urls)),
]
