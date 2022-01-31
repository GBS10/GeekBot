from django.urls import path
from addwords import views

urlpatterns = [
    path('addword', views.add_word, name = 'addword'),
]