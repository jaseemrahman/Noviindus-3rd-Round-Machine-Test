from django.db import models

# Create your models here.
class Testimonial(models.Model):

    SLIDER=1
    BOX=0
    ACTIVE = 0
    INACTIVE = 1
    SECTIONS =   (
                     (SLIDER, 'slider'),
                     (BOX, 'box')
                     )   
                     
    STATUS =   (
                     (ACTIVE, 'active'),
                     (INACTIVE, 'inactive')
                     )                 
    image=models.ImageField(upload_to='testi', blank=True,null=True)
    title = models.CharField(max_length=300,unique=True)
    description = models.TextField(max_length=3000,unique=True)
    name = models.CharField(max_length=300,unique=True)

    position = models.CharField(max_length=300)
    section = models.IntegerField(choices=SECTIONS,default=SLIDER)

    status = models.IntegerField(choices=STATUS,default=ACTIVE)
 
    def __str__(self):
        return self.title