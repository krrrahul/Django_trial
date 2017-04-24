from django.db import models

# Create your models here.
#now we have create article through web pages not admin pages
"""
class Articles(models.Model):
    title= models.CharField(max_length=254)
    body=models.TextField()
    pub_date=models.DateTimeField('date Published')
    likes=models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title """