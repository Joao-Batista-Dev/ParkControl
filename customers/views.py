from django.shortcuts import render
from customers.models import Customer
from rest_framework import viewsets
from customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer






