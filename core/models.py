from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class Department(models.Model):
    """Department Table"""
    objects = models.Manager()
    deptName = models.CharField(unique=True, db_column='dept_name',max_length=100)
    deptContactPerson = models.CharField(max_length=100,db_column='dept_contact_person')

    def __str__(self):
        return self.deptName

class Designation(models.Model):
    """Designation Database"""
    id = models.IntegerField(primary_key=True, auto_created=True, db_column='Des_id')
    designationName = models.CharField(max_length=100, db_column='Des_name')

    objects = models.Manager()

    def __str__(self):
        return self.designationName



class ProjectDetails(models.Model):
    """Employee project Details"""
    id = models.AutoField(primary_key=True, auto_created=True, db_column='project_id')
    ProjectName = models.CharField(max_length=50, db_column='project_name')
    ProjectIncharge = models.CharField(max_length=50, db_column='project_incharge')
    ProjectStartDate = models.DateField(db_column='project_start_date')

class Newproject(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,db_column='Newproject_id')
    NewprojectName = models.CharField(max_length=100,db_column='newproject_name')
    NewprojectIncharge = models.CharField(max_length=50,db_column='Newproject_incharge')
    NewprojectStartDate= models.DateField(db_column='Newproject_Start_Date')








class Employee(models.Model):
    """Employee Database rep"""
    id = models.AutoField(primary_key=True,auto_created=True,db_column='emp_id')
    firstName = models.CharField(max_length=100,db_column='first_name')
    lastName = models.CharField(max_length=100,db_column='last_name')
    middleName = models.CharField(max_length=100,db_column='middle_name', null=True)
    dob = models.DateField()
    salary = models.DecimalField(max_digits=19,decimal_places=6 ,db_column='Emp_salary')
    dateOfJoining = models.DateField(db_column='date_of_joining')
    deptId = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, db_column='dept_id')
    desId = models.ForeignKey(to=Designation,on_delete=models.CASCADE,null=True,db_column='des_id')
    projectId = models.ForeignKey(to=ProjectDetails,on_delete=models.CASCADE,null=True,db_column='Project_id')
    # designation = models.ForeignObject(to=Designation,from_fields='desId',to_fields='id',on_delete=models.CASCADE)
    objects = models.Manager()


class PunchinDetails(models.Model):
    """Punch Dtabase"""
    id = models.IntegerField(primary_key=True, auto_created=True, db_column='punch_id')
    punchinTime = models.DateTimeField(db_column='date_and_time_of_punch')
    empid = models.ForeignKey(to=Employee, on_delete=models.CASCADE,null=True,db_column='emp_id')




class EmployeetoProject(models.Model):
    """Employee to Project Database"""
    id = models.IntegerField(primary_key=True,auto_created=True,db_column='Emp_Project_id')
    ProjectId = models.ForeignKey(to=ProjectDetails,on_delete=models.CASCADE,null=True,db_column='Project_id')
    empId = models.ForeignKey(to=Employee, on_delete=models.CASCADE, null=True, db_column='emp_id')


class Assignment(models.Model):
    """Assignment Database"""
    id = models.AutoField(primary_key=True, auto_created=True, db_column='Assi_id')
    assignmentName = models.CharField(max_length=100,db_column='assignment_Name')
    assignmentTopic = models.CharField(max_length=100,db_column='assignment_Topic')
    assignmentStartDate = models.DateField(db_column='assignment_start_date')
    assignmentEndDate = models.DateField(db_column='assignment_end_date',null=True)
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, db_column='emp_id')


class Topic(models.Model):
    topicName = models.CharField(max_length=100,db_column='topic_name')
    topicDesc = models.CharField(max_length=1000,db_column='topic_desc')

class Routine(models.Model):

     routineName = models.CharField(max_length=100, db_column='routine_name')
     routineDesc = models.CharField(max_length=1000, db_column='routine_desc')















