from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import render

class UserListView(ListView):
    model = User
    template_name = 'firstapp/home.html' 
    context_object_name = 'users'  
    paginate_by = 4
    queryset = User.objects.all()