from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from  .models import Person

# Create your views here.
def demo(request):
   # return HttpResponse("Hello world")
   # name="india"
   obj=Place.objects.all()
   obv=Person.objects.all()
   return  render(request,"index.html",{'res':obj,'res1':obv})
# def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    add=x+y
#    sub=x-y
#    mul=x*y
#    divi=x/y
#    return render(request,"about.html",{'result':add,'result1':sub,'result2':mul,'result3':divi})
#
# def contact(request):
#    return HttpResponse("Haiii")