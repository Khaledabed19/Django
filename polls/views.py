from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def home (request):
    backavar=" hello  word "
    jiji="chaima va al l ecole"
    data={"student1":1,"studient2":2,"studient3":3,"studient4":4,"studient5":5}
    context = {"frontVar": backavar,"var1": 10,"List1":[10,20,30],"data":data}
    return render(request, "index.html", context)


