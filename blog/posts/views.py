#Lab6

from django.shortcuts import render

# Create your views here.

#Lab 6 - listing 14 zaimportowanie Http404
from django.http import Http404, HttpResponse
import datetime
from .models import Topic, Category, Post

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def topic_list(request):
    # pobieramy wszystkie obiekty Topic z bazy poprzez QuerySet
    topics = Topic.objects.all()
    #Lab 6 - listing 9
    return render(request,
                  "posts/topic/list.html",
                  {'topics': topics})

#Lab 6 - listing 12    
def topic_detail(request, id):
    # pobieramy konkretny obiekt Topic
    #Lab 6 - listing 14
    try:
        topic = Topic.objects.get(id=id)
    except Topic.DoesNotExist:
        raise Http404("Obiekt Topic o podanym id nie istnieje")
    topic = Topic.objects.get(id=id)

    return render(request,
                  "posts/topic/detail.html",
                  {'topic': topic})
    
#Lab 6 Zad 1    
def category_list(request):
    # pobieramy wszystkie obiekty Topic z bazy poprzez QuerySet
    categories = Category.objects.all()
    #Lab 6 - listing 9
    return render(request,
                  "posts/category/list.html",
                  {'categories': categories})

#Lab 6 Zad 1  
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404("Obiekt Topic o podanym id nie istnieje")
    category = Category.objects.get(id=id)

    return render(request,
                  "posts/category/detail.html",
                  {'categories': category})