from rest_framework import generics, permissions

from .models import Employee
from .serializers import EmployeeSerializer 

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # for jwt
    permission_classes = [permissions.IsAuthenticated]

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    #jwt protection
    permission_classes = [permissions.IsAuthenticated]   # 🔒