from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django import forms

# Create your models here.

class Rack(models.Model):
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
    
class Review(models.Model):
    username = models.CharField(unique=False, max_length=50)
    rating = models.IntegerField(max_length=1, null='True')
    review = models.CharField(unique=False, max_length=1000)
    crime = models.BooleanField(default=False)
    rack = models.ForeignKey(Rack)
    date_created = models.DateTimeField(default=timezone.now, auto_now_add=True)
    
    
    class Meta(object):
        verbose_name_plural = "reviews"
        ordering = ('username', 'rating', 'review')
        
    def __unicode__(self):
        return u'%s, %s' % (self.username, self.rating)
    
class rackForm(ModelForm):
    lat = forms.CharField()
    
    class Meta:
        model = Rack
        fields = ['lat', 'lng','description', 'capacity', 'covered', 'intended']
        
class reviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rack','username', 'rating', 'review', ]
    

