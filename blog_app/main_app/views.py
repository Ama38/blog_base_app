from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

User = get_user_model()
# Create your views here.


@login_required
def index_page(request):
    return render(request, 'main_app/index.html')
