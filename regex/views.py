from django.shortcuts import render
from django.contrib import messages
import re
def Regex(request):
    matched=[]
    RegText=''
    Task=''
    if request.method=='POST':
        RegText=str(request.POST.get('regText'))
        Task=str(request.POST.get('Task'))
        context=dict()
        if not RegText and not Task:
            return render(request,'regex/reg.html',{})
        else:
            if Task=='Task_2':
                pattern=re.compile(r'([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])')
                matches=pattern.finditer(RegText)
                for match in matches:
                    if match.group(1)=='0000':
                        continue
                    matched.append(match.group(0))
                
            if Task=='Task_1':
                pattern=re.compile(r'[1-9][0-9][0-9]+')
                matches=pattern.finditer(RegText)
                for match in matches:
                    if match.group(0)=='100':
                        continue
                    matched.append(match.group(0))
                
            if Task=='Task_7':
                pattern=re.compile(r'([A-Z][a-z]+)([A-Z][a-z]+)')
                matches=pattern.finditer(RegText)
                for match in matches:
                   x =  match.group(1).lower()
                   y =  match.group(2).lower()
                   matched.append(f'{x}_{y}')
                
            
            if Task=='Task_3':
                pattern=re.compile(r'["\'](.*?)["\']')
                matches=pattern.finditer(RegText)
                for match in matches:
                    matched.append(match.group(0)[1:len(match.group(0))-1])
                
            if Task=='Task_5':
                pattern = re.compile(r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]|[1-9]?[0-9])')
                matches=pattern.finditer(RegText)
                for match in matches:
                    if(match.group(0)==RegText):
                        matched.append(match.group(0))
                
            if Task=='Task_6':
                pattern=re.compile(r'(([0-9A-F]{2}[-:]){5}[0-9A-F]{2}|([0-9A-F]{4}[.]){2}[0-9A-F]{4})')
                matches=pattern.finditer(RegText)
                for match in matches:
                    if(match.group(0)==RegText):
                        matched.append(match.group(0))
          
         
    if(matched and RegText and Task):
            return render(request,'regex/reg.html',{'Dataset':matched})         
    else:
            return render(request,'regex/reg.html',{})
                  
                    






