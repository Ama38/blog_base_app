from django.urls import path
from main_app.views import *
from main_app.models import *


urlpatterns = [
    path('', index_page, name='home-page')
]