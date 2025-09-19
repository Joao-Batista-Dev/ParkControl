from dj_rql.filter_cls import AutoRQLFilterClass
from customers.models import Customer


# adicionar filtros automaticamente nos nossos endpoints
class CustomerFilterClass(AutoRQLFilterClass):
    MODEL = Customer






