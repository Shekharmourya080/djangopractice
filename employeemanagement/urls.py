from django.urls import path,include
from rest_framework.routers import DefaultRouter


from employeemanagement import  views
from employeemanagement import  tempview

router = DefaultRouter()

router.register('employee', viewset=views.EmployeeView)
router.register('designation', viewset=views.DesignationView)
router.register('department', viewset=views.DepartmentView)
router.register('project',viewset=views.ProjectDetailsView)
router.register('assignment',viewset=views.AssignmentView)
router.register('topic',viewset=views.TopicView)
router.register('routine',viewset=views.RoutineViews)
router.register('tempEmp',viewset=tempview.EmployeeView)
router.register('tempDepCHeck',viewset=tempview.DepartmentView)
router.register('newproject',viewset=views.NewprojectView)
router.register('EmployeeAdd',viewset=views.EmployeeAddView)


app_name = 'employee'

urlpatterns = [
    path('',include(router.urls))
]
