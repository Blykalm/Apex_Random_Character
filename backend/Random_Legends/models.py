from django.db import models

# Create your models here.

class Legend(models.Model):
    name = models.CharField(max_length=25 , default= '0', primary_key= True)
    legend_class = models.CharField(max_length=25, default='0')

    def __str__(self):
        return self.name

