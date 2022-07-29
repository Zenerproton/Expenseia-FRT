from django.db import models
from django.contrib.auth.models import User
# Create your models here.


TRANSACTION_CHOICE = (
    ('credit', 'credit'),
    ('debit', 'debit')
)


class Transaction(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    description = models.CharField(max_length=20, default='No Description')
    date = models.DateField()
    transaction_type = models.CharField(choices=TRANSACTION_CHOICE, max_length=10)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('date',)
