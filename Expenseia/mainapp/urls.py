from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('credit/', credit, name='credit'),
    path('debit/', debit, name='debit'),
    path('delete/<int:pk>', delete, name='delete'),
]
