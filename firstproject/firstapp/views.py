from django.shortcuts import render
from .models import Place,Team
from django.http import HttpResponse
# Create your views here.
def demo(request):
    obj1 = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request,'index.html',{'result':obj1,'team_result':obj2})

