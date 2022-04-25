from django import forms
from .models import Student, Department


class StudentForms(forms.ModelForm):
    code = forms.CharField(
        label='MSSV',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'place-holder': 'MSSV'
        }))
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'place-holder': 'Fullname'
        })
    )
    address = forms.CharField(
        initial='Viet Nam',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'rows': 10,
            'cols': 10
        })
    )

    class Meta:
        model = Student
        fields = ['code', 'name', 'address', 'department']

    def __init__(self, *args, **kwargs):
        super(StudentForms, self).__init__(*args, **kwargs)

        departmentObjs = Department.objects.all()
        departments = [(i.id, i.name) for i in departmentObjs]
        self.fields['department'].choices = departments

    def clean_code(self, *args, **kwargs):
        code = self.cleaned_data.get('code')
        if not code.isnumeric():
            raise forms.ValidationError("The code should be digit only")
        return code


class RawStudentForms(forms.Form):
    code = forms.CharField(
        label='MSSV',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'place-holder': 'MSSV'
        }))
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'place-holder': 'Fullname'
        })
    )
    address = forms.CharField(
        initial='Viet Nam',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'rows': 10
        })
    )
