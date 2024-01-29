from django.urls import path
from users.views import *


urlpatterns = [
    path('register/', register_view, name='register-page'),
    path('login/', login_view, name='login-page'),
    path('home/', home_page_view, name='home-page'),
    path('logout/', logout_view, name='logout-page')
]