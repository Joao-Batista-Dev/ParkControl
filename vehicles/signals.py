from django.db.models.signals import post_save
from django.dispatch import receiver
from vehicles.models import Vehicle
from vehicles.tasks import complete_vehicle_data

# criando o signals
@receiver(post_save, sender=Vehicle)
def complete_vehicle_data_receiver(sender, instance, created, **kwargs):
    # se ao criar/atualizar nao tiver a marca, modele ou cor do veiculo, chamar a minha tasks de buscar os dados apartir da placa
    if created and not instance.brand and not instance.model and not instance.color: 
        complete_vehicle_data.delay(instance.license_plate)

















