from rest_framework import permissions


class IsOwnerOfVehicleRecord(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # capturando o usuario logado
        user = request.user 

        # verificar se o usuario e dono do veiculo
        if hasattr(obj, 'owner'):
            return obj.owner and obj.owner.user == user
        
        # verificar se o dono do veiculo e o usuario
        if hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner'):
            return obj.vehicle.owner and obj.vehicle.owner.user == user



# class IsOwnerOfVehicleRecord(permissions.BasePermission):
    # metodo padrao para criar perimissoes
  #  def has_object_permission(self, request, view, obj):
        # pegando o usuario que esta logado - capturando o usuario
   #     user = request.user
        # objeto e o carro que o usuario que acessar - verficar se o dono do carro e igual ao usuario logado = quem esta aceesando o carro e o dono do veiculo
    #    has_permission = obj.owner.user == user

     #   return has_permission









