from django.db import models
import datetime
# Create your models here.

class product(models.Model):#ORM established
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=2000)
    count = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100, default='warehouse')
    date_added = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name