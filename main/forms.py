from django import forms
from .models import Class

class GradeCalculatorForm(forms.Form):
    SECTION_CHOICES = [
        ('Homework', 'Homework'),
        ('Quiz', 'Quiz'),
        ('Midterm', 'Midterm'),
        ('Final', 'Final'),
    ]

    section = forms.ChoiceField(choices=SECTION_CHOICES)
    grade_percentage = forms.DecimalField(
        max_digits=5, decimal_places=2, min_value=0, max_value=100,
        label="Grade Percentage (%)"
    )
    weight = forms.DecimalField(
        max_digits=5, decimal_places=2, min_value=0, max_value=100,
        label="Weight (%)"
    )

class AddClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'grade', 'credits']
        widgets = {
            'grade': forms.Select(choices=Class.GRADE_CHOICES)
        }

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if grade == 'A+' or grade == 'F-':
            raise forms.ValidationError("A+ and F- grades are not allowed.")
        return grade