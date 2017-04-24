'''
Created on Apr 19, 2017

@author: rahul
'''
from django import forms # bring form framwork
from django.contrib.auth.admin import User #when we do registration form we will fill user form and save it.
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm): # this form inherits from the existing Usercreationform
    #now we will defind what we are going to put in HTMl page but not with simple HTML tags
    #whatever extra you need like email firstname you should do like below one first
    email=forms.EmailField(required=True) #Truemeansrequire make it compulsory to enter a field
    class Meta(): #embeded class and used to hold form fields and used to define which is not in form field
        model=User
        fields=("username","email","password1","password2")#you want add anything like email add here too
        
        def save(self,commit): 
            user = super(MyRegistrationForm, self).save(commit=False)#false means not to fill data right now
            user.email=self.cleaned_data["email"]
            
            user.set_password(self.cleaned_data["password1"])#cleaned menas validated
            if commit:
                user.save()
            return user

        
        
