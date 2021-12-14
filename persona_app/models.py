from django.db import models

# Create your models here.
class Persona(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_street = models.CharField(max_length=100)
    address_number = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    age = models.IntegerField()
    picture = models.CharField(max_length=200)
    
    def __str__(self):
        return f"({self.id}) {self.first_name} {self.last_name}" 