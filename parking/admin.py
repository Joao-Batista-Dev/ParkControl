from django.contrib import admin
from parking.models import ParkingRecord, ParkingSpot

@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_time',]
    search_fields = ['vehicle__license_plate', 'parking_spot__spot_number']

    # para manipular o admin do django 
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # para campo parking_spot e a url nao for change, que faz um registro
        if db_field.name == 'parking_spot' and not request.resolver_match.url_name('change'):
            # filtrando as vagas apenas que nao foram preenchidas ainda
            kwargs['queryset'] = ParkingSpot.objects.filter(is_occupied=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)    


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied',]
    search_fields = ['spot_number',]
    list_filter = ['is_occupied',]

