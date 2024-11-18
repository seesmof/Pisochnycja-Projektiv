from django import template
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    given_members=Member.objects.all().values()
    template=loader.get_template('all_members.html')
    context={
        'given_members':given_members
    }
    return HttpResponse(template.render(context=context,request=request))

def details(request,id):
    member=Member.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'member':member
    }
    return HttpResponse(template.render(context=context,request=request))

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def testing(request):
    template=loader.get_template('template.html')
    context={
        'first_name':'John'
    }
    return HttpResponse(template.render(context=context,request=request))