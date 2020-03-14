from django.db import models

# Create your models here.

class product(models.Model) : 
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=200, unique=True)
    img = models.ImageField('image',upload_to='image_product')
    price = models.FloatField('price')
    detail = models.CharField('detail', max_length=200)
    state = models.BooleanField('state', default=True)
    def __str__(self) : 
        return self.name 

class user(models.Model) : 
    name = models.CharField('name', max_length=200, unique=True)
    email = models.EmailField('email', unique=True)
    password = models.CharField('password',max_length=200)

    def __str__(self) : 
        return self.name 
    class Meta : 
        db_table = u'user'

class appointment(models.Model) : 
    name = models.CharField('name', max_length=200)
    service =  models.CharField('service',max_length=200)
    barder = models.CharField('barder',max_length=200)
    email = models.EmailField('email',max_length=200)
    date = models.CharField('date',max_length=200)
    time = models.CharField('time',max_length=200)
    phone = models.CharField('phone', max_length=20)
    def __str__(self) :
        return self.name  
    class Meta : 
        db_table = u'appointment'
        
class post(models.Model) : 
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __str__(self) : 
        return self.title
