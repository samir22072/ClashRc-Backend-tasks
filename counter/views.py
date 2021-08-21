from django.shortcuts import render
from django.http import HttpResponse
from counter.forms import number_form


def index(request):
    return render(request,"counter/index.html")


def number(request):
    value=number_form()
    if request.method=="POST":
        value= number_form(request.POST)
        if value.is_valid:
            num=int(value.data['num'])
            
            context={
                "num":[n for n in range(1,num+1)]
            }
        
            return render(request,"counter/number.html",context)
    
        value=number_form()
    return render(request,"counter/form1.html",{'counter_form':value})

