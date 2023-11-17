from django.shortcuts import render

def data(request):
    data="hello"
    d={'ass':data}
    return render(request,'data.html',context=d)

def login(request):
    
    d={'name':'ashu','age':12}
    return render(request,'login.html',context=d)

# Create your views here.
