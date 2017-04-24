from django.db import models
from time import time
# Create your models here.

def get_upload_file_name(instance,filename):
    #please read doc to knon more about upload to https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.FileField.upload_to
    #https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
    print(instance,filename)
    return("%s" %(filename))
            
class Articles(models.Model):
    title= models.CharField(max_length=254)
    body=models.TextField()
  #  pub_date=models.DateTimeField('date Published')
    likes=models.IntegerField(default=0)
    thumbnail=models.FileField(upload_to=get_upload_file_name)#get_upload_file_name is function that we are going to write
    
    def __unicode__(self):
        return self.title 
    
    
    
class Comment(models.Model):
    article=models.ForeignKey(Articles)
    text =models.TextField()
    
"""Note the upload_to parameter. The files will be automatically uploaded to MEDIA_ROOT/PATH_That_You_HAVE_GIVEN_IN SETTING_FILE/.

It is also possible to do something like:

The upload_to can also be a callable that returns a string. This callable accepts two parameters, instance and filename.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
    """