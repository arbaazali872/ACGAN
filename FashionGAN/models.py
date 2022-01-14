from django.db import models
import datetime
import os
def filepath(request,filename):
    old_filename=filename
    timeNow=datetime.datetime.now()
    filename='%s%s' %(timeNow,old_filename)
    # return os.path.join("uploads/",filename)
    return os.path.join(filename)

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField(null=True,default=0)
    image=models.ImageField(upload_to=filepath,blank=True)
    discription=models.CharField(max_length=50,blank=True)
    

