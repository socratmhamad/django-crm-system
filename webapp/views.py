from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateUserForm,LoginForm,CreateRecordForm
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.db.models import Q
from django.contrib import messages




# Create your views here.


def index(request):
    return render(request, 'web/index.html')


def register(request):
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('login')
        
    else:
        form = CreateUserForm()
        
    context = {'form':form}
    return render(request, 'web/register.html', context)    




#login user


def my_login(request):
    
    if request.method == 'POST':
        form = LoginForm(request, data =request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username , password = password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            
    else:
        form =  LoginForm()  
        
    context = {'form':form}    
    
    return render(request ,'web/login.html',context)



@login_required(login_url = 'login')
def dashboard(request):
    records = Record.objects.all
    context = {'records' : records}
    return render(request,'web/dashboard.html',context)

@login_required(login_url='login')
def view_record(request, record_id):
    all_records = get_object_or_404(Record, id = record_id)
    context = {
        'record' : all_records
    }
    return render(request, 'web/view_record.html',context)


def my_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def Creat_Record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record created successfully ✔")
            return redirect('dashboard')
        
        
    else:
        form = CreateRecordForm()   
    context = {
        'form' : form
    }        
    
    return render(request , 'web/create-record.html',context=context)
    
    
def update_record(request,record_id):
    record = get_object_or_404(Record,id=record_id)
    form = CreateRecordForm(instance=record)
    if request.method == 'POST':
        form = CreateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully ✏️")
            return redirect('dashboard')
            
    return render(request, 'web/update-record.html',{'form' : form})        
        
        
        
def delete_record(request,record_id):
    record = get_object_or_404(Record,id=record_id)#جبلي الجدول صاحب الأي دي هذا        
    if request.method == 'POST':
        record.delete()
        messages.success(request, "Record deleted successfully ❌")
        return redirect('dashboard')
    
    return render(request, 'web/delete-record.html',)




def search_records(request):

    query = request.GET.get('q')

    if query:
        records = Record.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
    else:
        records = Record.objects.all()

    context = {
        'records': records
    }

    return render(request, 'web/dashboard.html', context)