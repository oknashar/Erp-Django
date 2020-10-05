from django.shortcuts import get_object_or_404, redirect, render
from .models import Employe,Absense
from .filters import EmployeFilter
from .forms import EmployeForm
import datetime
from employe.filters import AbsenseFilter
# Create your views here.



def Employe_list(request):
    ListEmploye = Employe.objects.all()

     ##filters##
    my_filter = EmployeFilter(request.GET ,queryset=ListEmploye)
    EmploteList = my_filter.qs

    absense = Absense.objects.filter(date=datetime.date.today().strftime("%Y-%m-%d"))
    ab =[abs.name for abs in absense ]
    print(ab)

    context = {
        'employes':EmploteList,
        'my_filter':my_filter,
        'absense':ab

    }
    return render(request,'employes.html',context)

def addEmploye(request):
    if request.method=='POST':
        form = EmployeForm(request.POST)

        if form.is_valid:
            myform = form.save(commit=False)
            myform.save()
            return redirect('/employe')
    else:
        form = EmployeForm()
    context={'form':form}
    return render(request,'add_employe.html',context)

def edit_Employe(request,id):
    post = get_object_or_404(Employe ,id=id )
    if request.method=='POST':
        form=EmployeForm(request.POST,instance=post)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.save()
            return redirect('/employe')

    else:
        form = EmployeForm(instance=post)
    
    context = {
        'form': form ,
    }

    return render(request,'editEmploye.html',context)

def delete_Employe(request,id):
    employe =Employe.objects.get(id=id).delete()

    return redirect('/employe')

def SignIn(request,id):
    employe = Employe.objects.get(id=id)
    absense = Absense(
        name=employe,
        date=datetime.date.today().strftime("%Y-%m-%d"),
        timeIn=datetime.datetime.now().time(),
        timeOut=None
    )
    absense.save()
    return redirect('/employe/absense/day')

def Absense_list(request):
    ListAbsense = Absense.objects.all()

    my_filter = AbsenseFilter(request.GET ,queryset=ListAbsense)
    AbsenseList = my_filter.qs
   

    context = {
        'Absenses':AbsenseList,
        'my_filter':my_filter
    }
    return render(request,'absense.html',context)

def AbsenseDay_list(request):
    ListAbsense = Absense.objects.filter(date=datetime.date.today().strftime("%Y-%m-%d"))
    # ListAbsense = Absense.objects.filter(date__month=10)

    my_filter = AbsenseFilter(request.GET ,queryset=ListAbsense)
    AbsenseList = my_filter.qs
   

    context = {
        'Absenses':AbsenseList,
        'my_filter':my_filter
    }
    return render(request,'absense.html',context)



def Signout(request,id):
    absense = Absense.objects.get(id=id)
    Absense.objects.filter(id=id).update(timeOut=datetime.datetime.now().time())
    absense.refresh_from_db()
    return redirect('/employe/absense/day')




