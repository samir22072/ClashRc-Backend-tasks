from django.shortcuts import render,redirect
from django.http import HttpResponse
from counter.forms import number_form
from counter.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required(login_url='login')
def index(request):
    return render(request,"task_2/index.html")


def number(request):
    value=number_form()
    if request.method=="POST":
        value= number_form(request.POST)
        if value.is_valid():
            num=int(value.data['num'])
            
            context={
                "num":[n for n in range(1,num+1)]
            }
        
            return render(request,"task_2/number.html",context)
    
        value=number_form()
    return render(request,"task_2/form1.html",{'counter_form':value})

def register(request):
    '''
    reg_form=UserRegisterForm()
    if request.method=="POST":
        reg_form=UserRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username=reg_form.cleaned_data.get('username')
            messages.success(request,f'Account was created for {username}')
            return redirect('Home')
    return render(request,'task_2/register.html',{'form':reg_form})
    '''
    

            
              

