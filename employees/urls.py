from django.urls import path 

from .views import EmployeeListCreateView, EmployeeDetailView 

urlpatterns = [
    path("<int:pk>/", EmployeeDetailView.as_view(), name='employee-detail'),
    path("", EmployeeListCreateView.as_view(), name='employee-list')
]