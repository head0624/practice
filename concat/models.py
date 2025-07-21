from django.db import models

class Concat(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return f'[{self.pk}]{self.name}'
