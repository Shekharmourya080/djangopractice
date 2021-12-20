from rest_framework import viewsets,mixins,status
from rest_framework.decorators import action
from rest_framework.response import  Response
import datetime
from core.models import Newproject,Employee, Designation, Department, ProjectDetails,Assignment, Topic,Routine
from employeemanagement.searilizer import EmployeeSerializer,DesignationSerializer,DepartmentSerializer\
    ,ProjectDetailsSerializer,AssignmentSerializer,TopicSerializer,RoutineSerializer,NewprojectSerializer

# Create your views here.

class NewprojectView(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Newproject.objects.all()
    serializer_class = NewprojectSerializer

    def get_queryset(self):
        return Newproject.objects.all()

    @action(methods=['GET'], detail=False, url_path='searchByNewprojectName')
    def Newproject(self,request):
        NewprojectName = self.request.query_params.get('NewprojectName')
        queryset = Newproject.objects.all().filter(NewprojectName__icontains=NewprojectName)
        serializer = NewprojectSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)









class EmployeeView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get_queryset(self):
        queryset = Employee.objects.all().filter()
        return queryset
    #
    # @action(methods=['GET'], detail=False,url_path='findByFirstName')
    # def findByFirstName(self,request):
    #     firstName = self.request.query_params.get('firstName')
    #     queryset = Employee.objects.all().filter(firstName=firstName)
    #     serializer = EmployeeSerializer(queryset,many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=False,url_path='searchByFirstName')
    def findByFirstName(self, request):
        firstName = self.request.query_params.get('firstName')
        queryset = Employee.objects.all().filter(firstName__contains=firstName)
        serializer = EmployeeSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=False,url_path='findBylastName')
    def searchBylastName(self,request):
        lastName = self.request.query_params.get('lastName')
        queryset = Employee.objects.all().filter(lastName__icontains=lastName)
        if queryset.count()>0:
           serializer = EmployeeSerializer(queryset,many=True)
           return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    @action(methods=['GET'],detail=False,url_path='searchByLastName')
    def finfbylastName(self,request):
        lastName = self.request.query_params.get('lastName')
        queryset = Employee.objects.all().filter(lastName=lastName)
        serializer = EmployeeSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=False,url_path='findByDept')
    def findByDepartment(self,request):
        deptName = self.request.query_params.get('deptName')
        """SELECT * from employee inner join department on department.id = employee.deptId where
         department.deptName = 'deptName' """
        """SELECT * from employee where deptId.deptName='deptName'"""
        queryset = Employee.objects.all().filter(deptId__deptName__contains=deptName)
        serializer = EmployeeSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='findEmpDesandDept')
    def Department(self, request):
        departmentName = self.request.query_params.get('Department')
        designation = self.request.query_params.get('Designation')
        queryset = Employee.objects.all().filter(deptId__deptName__contains=departmentName,
                                                 desId__designationName__contains=designation)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(methods=['GET'], detail=False, url_path='findByAge')
    def age(self,request):
        """20/12/2021 - gives current date"""
        currentDate = datetime.date.today()
        """11 - given age"""
        age = int(self.request.query_params.get('age'))
        """(2021-11,12,20)= 20/12/2010 - reducing year by given age"""
        currentDate = datetime.date(currentDate.year-age, currentDate.month, currentDate.day)
        """SELECT * FROM employee where dob <= '2010-12-20'"""
        queryset = Employee.objects.all().filter(dob__lte=currentDate)
        """SERIALIZE MODEL TO JSON"""
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='findByDoj')
    def doj(self,request):
        currentDate = datetime.date.today()
        totalExp = int(self.request.query_params.get('doj'))
        """20-12-2019"""
        currentDate = datetime.date(currentDate.year-totalExp,currentDate.month,currentDate.day)
        queryset = Employee.objects.all().filter(dateOfJoining__lte=currentDate)
        serializer = EmployeeSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)












class DesignationView(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = DesignationSerializer
    queryset = Designation.objects.all()

    def get_queryset(self):
        queryset = Designation.objects.all().filter()
        return queryset


    @action(methods=['GET'],detail=False,url_path='getDesignation')
    def Designation(self, request):
        designation = self.request.query_params.get('Designation')
        queryset = Designation.objects.all().filter(designationName__contains=designation)
        if queryset.count() > 0:
            serializer = DesignationSerializer(queryset[0])
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['GET'],detail=False,url_path='findAllEmployee')
    def searchByDesignation(self,request):
        designation = self.request.query_params.get('Designation')
        queryset = Employee.objects.all().filter(desId__designationName__contains=designation)
        serializer = EmployeeSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)









class DepartmentView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_queryset(self):
     queryset = Department.objects.all()
     return queryset


    @action(methods=['GET'],detail=False,url_path='findAllEmployee')
    def Department(self,request):
        departmentName = self.request.query_params.get('Department')
        queryset = Employee.objects.all().filter(deptId__deptName__contains= departmentName)
        serializer = EmployeeSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)








class ProjectDetailsView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ProjectDetailsSerializer
    queryset = ProjectDetails.objects.all();

    def get_queryset(self):
        return ProjectDetails.objects.all();

    @action(methods=['GET'],detail=False,url_path='SearchByProjectName')
    def ProjectDetails(self,request):
        projectName = self.request.query_params.get('prjectNmae')
        queryset = ProjectDetails.objects.all().filter(ProjectName=projectName)
        if queryset.count() > 0:
            serializer = ProjectDetailsSerializer(queryset[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)









class AssignmentView(viewsets.GenericViewSet,
                     mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def get_queryset(self):
        return Assignment.objects.all()

    @action(methods=['GET'], detail=False, url_path='SearchByAssignmentName')
    def Assignment(self, request):
      assignmentName = self.request.query_params.get('AssignmentName')
      """ Select * from core_assignment where assigmnent_topic = 'Model' """
      queryset = Assignment.objects.all().filter(assignmentTopic=assignmentName)
      if queryset.count() > 0:
        serializer = AssignmentSerializer(queryset[0])
        return Response(serializer.data, status=status.HTTP_200_OK)
      else:
            return Response(status=status.HTTP_404_NOT_FOUND)










class TopicView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.all()

    @action(methods=['GET'], detail=False, url_path='TopicName')
    def Topic(self, request):
        topicName = self.request.query_params.get('topicName')
        queryset = Topic.objects.all().filter(topicName=Topic)
        if queryset.count() > 0:
            serializer = TopicSerializer(queryset[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RoutineViews(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def get_queryset(self):
        return Routine.objects.all()