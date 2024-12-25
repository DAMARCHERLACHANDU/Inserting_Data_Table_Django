from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert(request):
    
    topic = Topic.objects.create(topic_name="Html")

    webpage = Webpage.objects.create(topic_name=topic, name="Html Documentation", url="https://docs.djangoproject.com/")

    access_record = AccessRecords.objects.create(name=webpage, Author="Uday", date="2024-12-25")

   
    return HttpResponse("Data inserted successfully!")