from django.db import models
from django.forms import ModelForm

# Create your models here.

class rack(models.Model):
    lat = models.CharField(unique=False, max_length=50)
    lng = models.CharField(unique=False, max_length=50)
    description = models.CharField(unique=False, max_length=1000)
    capacity = models.IntegerField (max_length=3, null='True')
    covered = models.BooleanField (default=False)
    intended = models.BooleanField (default=True)
    
    class Meta(object):
        verbose_name_plural = "racks"
        ordering = ('lat', 'lng', 'description', 'capacity', 'covered', 'intended')
        
    def __unicode__(self):
        return u'%s, %s' % (self.description, self.capacity)
    
class review(models.Model):
    username = models.CharField(unique=False, max_length=50)
    rating = models.IntegerField(max_length=1, null='True')
    review = models.CharField(unique=False, max_length=1000)
    crime = models.BooleanField(default=False)
    rack = models.ForeignKey(rack)
    
    
    class Meta(object):
        verbose_name_plural = "reviews"
        ordering = ('username', 'rating', 'review')
        
    def __unicode__(self):
        return u'%s, %s' % (self.username, self.rating)
    
class rackForm(ModelForm):
    class Meta:
        model = rack
        fields = ['lat', 'lng','description', 'capacity', 'covered', 'intended']
        
class reviewForm(ModelForm):
    class Meta:
        model = review
        fields = ['username', 'rating', 'review']
    

