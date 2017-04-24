from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from .models import Articles
from .forms import ArticleForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
# Create your views here


def articles(request):
    
#this section is for cookie
    language='en-gb'  #this is for cookie
    session_language='en-gb' #this is for session
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language=request.session['lang']
    
    return render_to_response('articles.html',{'articles':Articles.objects.all(),'language':language,'session_lang':session_language})

def language(request,language='en-gb'):
    response=HttpResponse("Setting language to %s" %language)
    response.set_cookie('lang',language) #for cookies we use response onject
    request.session['lang']=language# for session we use request object
    return response

def article(request,article_id=1):
    return render_to_response('article.html',{'article':Articles.objects.get(id=article_id)})


def create(request):
    if request.POST:
        form=ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
        else:
            print("not valid data")
    #else:
    #    form=ArcticleForm()
    
    args ={}
    args.update(csrf(request))
    args['form']=ArticleForm()
    return render_to_response('create_article.html',args)

#http://.django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/    
def like_article(request,article_id):  #url(r'^likes/(?P<article_id>\d+)/$', 'viewname', name='urlname').From url this articleeid is passed as a parameter to view
    if article_id:
        a=Articles.objects.get(id=article_id)
        count=a.likes
        count+=1
        a.likes=count
        a.save()    #if you want to save anything save is the command to remember
        return HttpResponseRedirect('/articles/get/%s' %article_id)




############################################################################################
################################################################################################
######################################################################################
################################################################################
################################################################################
def hello(request):
    name='Rahul'
    html="<html><body>Hi %s, this seems to have worked</body></html>" %name
    return HttpResponse(html)

def hello_template(request):
    name='rahul'
    t=get_template('hello.html')
    html=t.render(Context({'name':name}))
    return HttpResponse(html)
#both of them are same
def hello_template_simple(request):
    name='rahul'
    return render_to_response('hello.html',{'name':name})

class HelloTemplate(TemplateView):
    template_name='hello_class.html'
    def get_context_data(self, **kwargs):
        context=super(HelloTemplate,self).get_context_data(**kwargs)
        context['name']='Rahul'
        return context