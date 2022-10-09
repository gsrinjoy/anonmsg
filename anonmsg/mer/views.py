from django.shortcuts import render
from django.http import HttpResponse
import string
import random
from .models import Login
from .models import Msgstore 

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == "POST":
     # getting input with name = fname in HTML form
     name = request.POST['nme']
     res = ''.join(random.choices(string.ascii_uppercase , k=5))
     pss = ''.join(random.choices(string.digits , k=5))
     b=Login(name=name,slg=res,pas=pss)
     b.save()
     ulr="127.0.0.1:8000"+res
     params={'yul':ulr,'yps':pss,'nom':name}
     return render(request,'dash.html',params)
    
    else :
        params={'yul': 0 ,'yps': 0,'name':''}
        return render(request,'create.html',params)

def send(request,slugs):
    if request.method == "POST":
        msg= request.POST['mg']
        slgs= slugs
        b=Msgstore(txt=msg,slu=slgs)
        s="Your Messege sent suceessfully"
        params={'re':s}
        return render(request,'resp.html',params)
    else :
        params={'re':''}
        return render(request,'resp.html',params)

def logn(request):
    if request.method == "POST":
        pss= request.POST['pus']
        lgn=Login.objects.all()
        if(lgn.objects.filter(pas=pss).exists()):
         con=Login.objects.get(pas=pss)
         nme=con.name
         slo=con.slg
         con1=Msgstore.objects.get(slu=slo)
         msgo=con1.txt
         l=len(msgo)
         params={'leno':l,'mxg':msgo}
         return render(request,'dash.html',params)
    else :
        params={'re':''}
        return render(request,'login.html',params)




     
