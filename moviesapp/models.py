from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    hero=models.CharField(max_length=50)


    def __str__(self):
        return self.name