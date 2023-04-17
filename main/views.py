from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Company, Employee
from main.forms import EmployeeForm

def companies_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee']
            company_id = request.POST['company_id']
            company = Company.objects.get(pk=company_id)
            employee = Employee.objects.get(pk=employee_id)
            employee.company = company
            employee.save()
            return redirect('companies_view')
    else:
        companies = Company.objects.all()
        employee_form = EmployeeForm()
        return render(request, 'companies.html', {'companies': companies, 'employee_form': employee_form})
