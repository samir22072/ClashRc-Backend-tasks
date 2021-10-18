
from django.shortcuts import render,redirect
from django.http import HttpResponse
from task_3.forms import UserRegisterForm,loginform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import NewUser
import re


def checkPassword(password,cap):
    password=str(password)
    if type(cap)==int:
        if cap>48:
            for i in range(cap,cap+26):
                if password.__contains__(chr(i))==True:
                    return True
            else:
                return False
        else:
            for i in range(cap,cap+10):
                if password.__contains__(chr(i))==True:
                    return True
            else:
                return False
    else:
        for i in cap:
            if password.__contains__(i)==True:
                return True
        else:
            return False

def emailValidation(email):
    pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    matches=pattern.finditer(email)
    flag=False
    for match in matches:
        if match.group(0)==email:
            return True
    return False

    


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
        return render(request,'task_3/register.html',{'form':reg_form})
        '''
        if request.method=="POST":
            email=request.POST.get('email')
            user_name=request.POST.get('username')
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            password=request.POST.get('password1')
            password_confirm=request.POST.get('password2')
            flag=True
            if not email:
                messages.error(request,f'You need to enter an email address')
                flag=False
            if not user_name:
                messages.error(request,f'You need to enter an Username')
                flag=False
            if not password:
                messages.error(request,f'You need to enter a password')
                flag=False
            if not first_name:
                messages.error(request,f'You need to enter a first name')
                flag=False
            if not last_name:
                messages.error(request,f'You need to enter a last name')
                flag=False
            if password!=password_confirm:
                flag=False
                messages.info(request,f'The passwords did not match')
            if len(password)<8:
                messages.error(request,f'The password should be atleast 8 characters long')
                flag=False
            else:
                password1=str(password)
                capital=checkPassword(password1,65)
                small=checkPassword(password1,97)
                numeric=checkPassword(password1,48)
                special=checkPassword(password1,['#','@'])
                if capital==True and small==True and numeric==True and special==True:
                    pass
                else:
                    flag=False
                    messages.error(request,f'The password should contain atleast 1 small letter, 1 capital letter, 1 number and atleast one special character') 

            if NewUser.objects.filter(email=email).exists():
                flag=False
                messages.error(request,f'A user with given email already exists')
            if NewUser.objects.filter(user_name=user_name).exists():
                flag=False
                messages.error(request,f'An account with the given username exists.') 
            if emailValidation(str(email))==False:
                flag=False
                messages.error(request,f'The email entered is Invalid.')
            if flag==False:
                return redirect('register')
            else:
                user=NewUser.objects.create_user(email,user_name,first_name,last_name,password)
                user.save()
                return redirect('login')

            
        return render(request,'task_3/register.html')


        



def loginpage(request):
    if request.method=='POST':
        email=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'Successfully logged into the account of {email}')
            return render(request,'task_3/profile.html',{'email':email,'username':user.user_name})
        else:
            messages.info(request,f'Username or password is incorrect')
    context={}
    return render(request,'task_3/login.html',context)
            
              
def logoutUser(request):
    logout(request)
    return redirect('login')

def searchUser(request):
    if request.method=='POST':
        email=request.POST.get('email')
        if NewUser.objects.filter(email=email).exists():
            user=NewUser.objects.get(email=email)
            username=user.user_name
            emailId=user.email
            first_name=user.first_name
            last_name=user.last_name
            return render(request,'task_3/infopage.html',{'username':username,'email':emailId,'first_name':first_name,'last_name':last_name})
        else:
            messages.error(request,f'The searched user does not exist')
    return render(request,'task_3/searchpage.html')



    
    