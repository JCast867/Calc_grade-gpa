from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Class, GRADE_TO_GPA
from .forms import GradeCalculatorForm, AddClassForm
from django import forms

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def add_class(request):
    if request.method == 'POST':
        form = AddClassForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.user = request.user
            new_class.save()
            return redirect('view_gpa')
    else:
        form = AddClassForm()
    return render(request, 'add_class.html', {'form': form})

@login_required
def view_gpa(request):
    classes = Class.objects.filter(user=request.user)
    total_points = 0
    total_credits = 0
    classes_with_gpa = []

    for cls in classes:
        gpa_points = GRADE_TO_GPA.get(cls.grade, 0)
        total_points += gpa_points * cls.credits
        total_credits += cls.credits
        classes_with_gpa.append({
            'id': cls.id,  # Include the class ID
            'name': cls.name,
            'grade': cls.grade,
            'gpa_points': gpa_points,
            'credits': cls.credits
        })

    gpa = total_points / total_credits if total_credits > 0 else 0
    return render(request, 'view_gpa.html', {'classes': classes_with_gpa, 'gpa': round(gpa, 2)})

@login_required
def grade_calculator(request):
    if request.method == 'POST':
        form = GradeCalculatorForm(request.POST)
        if form.is_valid():
            section = form.cleaned_data['section']
            grade_percentage = form.cleaned_data['grade_percentage']
            weight = form.cleaned_data['weight']
            calculated_grade = (grade_percentage * weight) / 100
            return render(request, 'grade_calculator.html', {
                'form': form,
                'calculated_grade': calculated_grade
            })
    else:
        form = GradeCalculatorForm()
    return render(request, 'grade_calculator.html', {'form': form})

@login_required
def delete_class(request, class_id):
    cls = get_object_or_404(Class, id=class_id, user=request.user)
    if request.method == 'POST':
        cls.delete()
        return redirect('view_gpa')
    return render(request, 'delete_class.html', {'class': cls})
