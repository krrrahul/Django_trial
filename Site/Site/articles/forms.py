'''
Created on Apr 19, 2017

@author: rahul
'''
from django import forms #this gets extends
from  .models import Articles

class ArticleForm(forms.ModelForm): #this model form is made to deal specifically with models
    class Meta: # used to define which is not a form field
        model=Articles
        fields={'title','body','thumbnail'}