#Lab 8 - listing 3
from django.urls import path, include
from . import api_views

# pamiętaj, że te reguły, mimo, że bardzo podobne do zdefiniowanych w poprzednich
# zadaniach dotyczą endpointów dla REST API, a nie widoków dla szablonów HTML
urlpatterns = [
    path('topics/', api_views.topic_list),
    path('topics/<int:pk>/', api_views.topic_detail),
    path('categories/', api_views.category_list),
    path('categories/<int:pk>/', api_views.category_detail),
]