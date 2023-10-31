from django.urls import path
from .views import *

urlpatterns = [
    path('', frontpage, name='home'),
    path('short_courses/', Short, name='short'),


]
