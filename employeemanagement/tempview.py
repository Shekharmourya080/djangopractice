from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, status
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import Employee, Department
from employeemanagement.searilizer import EmployeeSerializer, DepartmentSerializer


class EmployeeView(GenericViewSet,ListModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()

    @action(methods=['GET'], detail=False, url_path='findByFirstName')
    def filter_by_first_name(self, request):
        firstname = self.request.query_params.get('firstName')
        query = Employee.objects.all().filter(firstName=firstname)
        serialize = EmployeeSerializer(query, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='findByLastName')
    def filter_by_last_name(self, request):
        lastname = self.request.query_params.get('lastName')
        query = Employee.objects.all().filter(lastName__icontains=lastname)
        serialize = EmployeeSerializer(query, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)


class DepartmentView(GenericViewSet, ListModelMixin):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.all()


