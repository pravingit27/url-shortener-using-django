from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import url

# Create your views here.
def hello(req):
    if req.method == "POST" :
        full_url = req.POST.get('full_url')
        obj = url.create(full_url)
        return render(req,'index.html' , {
            'full_url' : obj.full_url,
            'short_url': req.get_host() + '/' + obj.short_url
        })

    return render(req,'index.html')

def route_Url(req,key):
    try:
        obj = url.objects.get(short_url=key)
        return redirect (obj.full_url)
    except:
        return redirect(hello)

