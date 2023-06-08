from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template('all_members.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember=Member.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template= loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template= loader.get_template('template.html')
    context={
        'fruits' : ['Apple','Banana','Cherry'],
    }
    return HttpResponse(template.render(context,request))

def testing1(request):
    template =loader.get_template('template1.html')
    context={
        'firstname' :'Christina',
    }
    return HttpResponse(template.render(context,request))

def testing2(request):
    template =loader.get_template('template2.html')
    return HttpResponse(template.render())

def testing3(request):
    mymember=Member.objects.get(id=id)
    template= loader.get_template('template3.html')
    context= {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context,request))


