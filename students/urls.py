from django.urls import path, include
from. import views
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'api/students', StudentViewSet)

urlpatterns = [
    path('', views.student_list, name = 'student_list'),
    path('add/',views.student_add, name ='student_add'),
    path('edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('',include(router.urls)),
]