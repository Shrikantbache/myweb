from typing import ContextManager
from django.shortcuts import render

# Create your views here.
def skill(request):
    Context = {'skill':'active'}
    return render(request,'edu/skill.html',Context)