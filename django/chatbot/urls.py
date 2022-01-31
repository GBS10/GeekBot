from django.urls import path
from chatbot import views

urlpatterns = [
    path('', views.chatbot, name = 'chatbot'),
    path('get', views.get_response, name = 'response'),
    path('loginform', views.login_form, name = 'loginform'),
    path('formword', views.word_form, name = 'formword')
]