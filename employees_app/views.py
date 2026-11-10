from django.shortcuts import render
from .models import Employee
from django.db.models import Avg
from datetime import date


def employee_overview(request):
    employees = Employee.objects.all()

    employees_with_department = Employee.objects.values(
        "name", "department__name", "salary"
    )
    salary_gt_3000_employees = employees.filter(salary__gt=3000)
    count_salary_gte_5000 = employees.filter(salary__gte=5000).count()
    avg_salary_department_sales = employees.filter(department__name="Sales").aggregate(
        Avg("salary")
    )["salary__avg"]
    pre_2022_non_hr_employees = employees.filter(
        hire_date__lt=date(2022, 1, 1)
    ).exclude(department__name="HR")

    context = {
        "employees_with_department": employees_with_department,
        "salary_gt_3000_employees": salary_gt_3000_employees,
        "count_salary_gte_5000": count_salary_gte_5000,
        "avg_salary_department_sales": avg_salary_department_sales,
        "pre_2022_non_hr_employees": pre_2022_non_hr_employees,
    }

    return render(request, "employee_list.html", context)
