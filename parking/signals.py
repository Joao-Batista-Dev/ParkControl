from django.db.models.signals import post_save
from django.dispatch import receiver
from parking.models import ParkingRecord


# essa funcao sera exercutada toda vez que for salvar dados na tabela parking record - na entrada de veiculo
# receiver - e para ouvir nossos eventos
@receiver(post_save, sender=ParkingRecord )
def update_parking_spot_status(sender, instance, created, **kwargs): # sender - é a tabela
    #  instance - e registro que foi salvo, apos salva, ou seja salvar no instace como se fosse uma variavel
    parking_spot = instance.parking_spot
    # usando a instace para acessar o nosso campo de ocupado - verificar se o carro ja saiu, se nao tem saida o carro ta entrando
    parking_spot.is_occupied = instance.exit_time is None
        
    parking_spot.save()



