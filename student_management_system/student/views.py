from django.shortcuts import render
from .models import Student
from django.shortcuts import render, redirect 
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm


def students_list(request):
    # Filter students based on query parameters
    query_params = request.GET
    full_name = query_params.get('full_name', '')
    course = query_params.get('course', '')
    gender = query_params.get('gender', '')
    age_from = query_params.get('age_from', '')
    age_to = query_params.get('age_to', '')

    # Filter students based on provided filters
    students = Student.objects.all()
    if full_name:
        students = students.filter(first_name__icontains=full_name) | students.filter(last_name__icontains=full_name)
    if course:
        students = students.filter(course=course)
    if gender:
        students = students.filter(gender=gender)
    if age_from:
        students = students.filter(age__gte=age_from)
    if age_to:
        students = students.filter(age__lte=age_to)

    context = {
        'students': students,
    }
    return render(request, 'student/students_list.html', context)

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        course = request.POST['course']
        gender = request.POST['gender']
        age = request.POST['age']

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            course=course,
            gender=gender,
            age=age,
        )
        return redirect('student_list')

    context = {}
    return render(request, 'student/add_student.html', context)

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    context = {'form': form, 'student': student}
    return render(request, 'student/update_student.html', context)

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')  # Redirect to the student list page after deletion