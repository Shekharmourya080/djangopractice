from rest_framework import serializers

from core.models import Employee,Designation, Department,ProjectDetails,Assignment,Topic,Routine,Newproject


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ('id', 'designationName')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('deptName','deptContactPerson')


class EmployeeSerializer(serializers.ModelSerializer):
    # department = serializers.RelatedField(many=False,queryset=Department.objects.all())
    class Meta:
        model = Employee
        fields = ('firstName', 'lastName', 'middleName', 'dob','dateOfJoining','deptId','desId','salary',)
        # extraKwargs =('department',)



class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetails
        fields = ('id','ProjectName','ProjectIncharge','ProjectStartDate')
        read_only_fields = ('id',)





class NewprojectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newproject
        fields = ('id','NewprojectName','NewprojectIncharge','NewprojectStartDate')
        read_only_field = ('id',)






class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id','assignmentName','assignmentTopic','assignmentStartDate','assignmentEndDate')
        read_only_fields = ('id',)
class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields=('topicName','topicDesc')

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields =('routineName','routineDesc')
