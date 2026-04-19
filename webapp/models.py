from django.db import models

# Create your models here.


#category model

class Category(models.Model):
    name = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    
#client moderl 

class Record(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phone= models.IntegerField()
    tall = models.IntegerField()
    wedight = models.IntegerField()
    address = models.CharField(max_length=500)
    create_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
   