"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import debug_toolbar
from django.urls import path
from django.urls import path, include

from BorderPay import views

# views.empty_table(1)
# views.hardcode('saksham')
error_message = ""
error=""
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('BorderPay/', ),
    # path('', include('BorderPay.urls')),
    path('', views.homepage),
    path('employersignup/', views.employersignup, name = 'employersignup'),
    path('employeelogin/', views.employeelogin, name = 'employeelogin'),
    path('employerlogin/', views.employerlogin, name = 'employerlogin'),
    path('employeesignup/', views.employeesignup, name = 'employeesignup'),
    path('employeewin/', views.employeewin, name = 'employeewin'),
    path('employerwin/', views.employerwin, name = 'employerwin'),
    path('createcontract/', views.createcontract, name = 'createcontract'),
    path('contract/', views.employeewin, name = 'contract'),
    path('empty/', views.empty, name = 'empty'),
    path('withdraw/', views.withdraw, name = 'withdraw'),
    path('advance/', views.advance, name='advance'),
    path('approve_advance/', views.approveadvance, name='approve_advance'),
    path('decline/', views.decline, name='decline')
    # path("__debug__/", include("debug_toolbar.urls"))

    # path('BorderPay/index', views.index, name='index'),
]
