
from django.contrib import admin
from django.urls import include, path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('payroll/', views.home, name="home"),
    path('departments/', views.department_list, name="departments"),
    path('department/', views.create_department, name="department"),
    path('position/', views.position_list, name='position_index'),
    path('create_position/', views.PositionCreate.as_view(), name='position_create'),
    path('employees/', views.employee_list, name="employees"),
    path('create_employee/', views.create_employee, name="create_employee"),
]
