from django.apps import AppConfig


class ParkingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parking'
    verbose_name = 'estacionamento'
    verbose_name_plural = 'estacionamentos'

    # para ativar o nosso signal
    def ready(self):
        import parking.signals


