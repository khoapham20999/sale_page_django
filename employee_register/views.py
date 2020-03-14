from django.shortcuts import render, redirect, HttpResponse
from .forms import employeeForm
from .models import employee

# Create your views here.


def employee_list(request):
    context = {'employee_list': employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id =0) : 
    if request.method == 'GET' : 
        if id ==0 : 
            form = employeeForm() 
        else : 
            try : 
                emp_get = employee.objects.get(id=id)
                form = employeeForm(instance=emp_get)
            except employee.DoesNotExist : 
                return HttpResponse("<h2>User with user_id = {} found or has been deleted before</h2>".format(id))
        return render(request, 'employee_register/employee_form.html', {'form' : form}) 
    else : 
        if id == 0 : 
            form = employeeForm(request.POST)  
        else : 
            emp_get = employee.objects.get(id=id)
            form = employeeForm(request.POST, instance = emp_get)
        if form.is_valid(): 
            form.save()
        return redirect('user:list')

def employee_delete(request, id) : 
    employee1 = employee.objects.get(id=id)
    employee1.delete()
    return redirect('user:list')




