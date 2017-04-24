from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect #
from django.contrib import auth #authorization
 #cross site request forgery
from django.template.context_processors import csrf
#from django.contrib.auth.forms import UserCreationForm #for user registration there is inbuilt form in django
from .forms import MyRegistrationForm
 
CSRF_COOKIE_SECURE= False     
# Create your views here.
def login(request):
    c={} #dictionary
    c.update(csrf(request))#send a unique URL to login page in {%csrf_token%} and when form return the it is checked here
    return render(request,'login.html')
    #return render_to_response('login.html')
def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user = auth.authenticate(username=username,password=password) #user is object 
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/django/accounts/loggedin')# redirect to logged in page
    else:
        return HttpResponseRedirect('/django/accounts/invalid')
    
    
def loggedin(request):
    return render_to_response('loggedin.html',{'full_name':request.user.username})#user is member variable of request

def invalid(request):
    return render_to_response("invalid.html")

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    
    if request.method=='POST':  #first time it will not go here
        form=MyRegistrationForm(request.POST)
        #form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/django/accounts/register_success')
        
     # first time it will go here 
    args={}
    args.update(csrf(request))
    #args['form']=UserCreationForm()#send a usercreationform as a dic value in form
    args['form']=MyRegistrationForm()#This is our new customised form form forms.py file which contain email address too.
    print (args)
    return render_to_response('register.html',args)

def register_success(request):
    return render_to_response('register_success.html')

