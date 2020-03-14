from django.db import models


class Position(models.Model) : 
    title = models.CharField(max_length=50) 
    def __str__(self) : 
        return self.title

# Create your models here.
class employee(models.Model) : 
    fullname = models.CharField(max_length=200)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self) : 
        return self.fullname
