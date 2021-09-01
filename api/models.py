from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return f'Nome: {self.name}\nIdade: {self.age}\n'
