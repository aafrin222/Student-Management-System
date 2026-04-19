from django.shortcuts import render, redirect
from.models import Student
from.forms import StudentForm
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .serializers import StudentSerializer

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request,'students/student_list.html',{'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()
    return render(request,'students/student_add.html',{'form':form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_add.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer