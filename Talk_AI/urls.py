from django.urls import path
from . import views

urlpatterns = [
    path('mic/', views.speech_to_text, name='my_mic'),
    path('speaker/', views.speaker, name='speaker'),
]