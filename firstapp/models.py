from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    dob = models.DateField()
    age = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name




 