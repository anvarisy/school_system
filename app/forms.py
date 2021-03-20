from django import forms
from django.contrib.auth.forms import PasswordChangeForm, ReadOnlyPasswordHashField, UserChangeForm, UserCreationForm
from app.models import bills, parents, plprecord, plps, students, subject_doc, subjects, uploadrecords, user
# from searchableselect.widgets import SearchableSelect
# from dal import autocomplete

class RegisterForm(UserCreationForm):
    class Meta:
        model = user
        fields = ('full_name', 'email','mobile_number','kadiv','is_admin')

class UpdateForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            'Raw passwords are not stored, so there is no way to see this '
            'user’s password '
        ),
    )
    class Meta:
        model = user
        fields = ('full_name', 'email','mobile_number','kadiv','is_admin')


class ParentForm(forms.ModelForm):
    class Meta:
        model = parents
        fields = ('parent_email', 'parent_name','parent_mobile')

class StudentForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        queryset=parents.objects.all(),
        widget=forms.Select(attrs={
          'class': 'select2-show-search' #is this POSSIBLE?
          })
        
    )
    dob_student = forms.DateField(
                           widget= forms.DateInput
                           (attrs={
                           'class':'fc-datepicker'}))
    
    class Meta:
        model = students
        fields = '__all__'

class FileForm(forms.ModelForm):
    class Meta:
        model = uploadrecords
        fields = ('file_name','file',)

class BillForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=students.objects.all(),
        widget=forms.Select(attrs={
          'class': 'select2-show-search' #is this POSSIBLE?
          })
    )
    class Meta:
        model = bills
        fields = '__all__'
        exclude= ('updated_date',)

class PlpForm(forms.ModelForm):
    plp_leader = forms.ModelChoiceField(
        queryset=user.objects.all(),
        widget=forms.Select(attrs={
          'class': 'select2-show-search' #is this POSSIBLE?
          })    
    )
    class Meta:
        model = plps
        fields = '__all__'

class PlpRecordForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=students.objects.all(),
        widget=forms.Select(attrs={
          'class': 'select2-show-search' #is this POSSIBLE?
          })
    )

    plp = forms.ModelChoiceField(
        queryset=plps.objects.all(),
        widget=forms.Select(attrs={
          'class': 'select2-show-search' #is this POSSIBLE?
          }) 
    )
    join_plp = forms.DateField(
                           widget= forms.DateInput
                           (attrs={
                           'class':'fc-datepicker'}))
    
    class Meta:
        model = plprecord
        fields = '__all__'
        exclude= ('report_result','o_nilai')

def get_param(param):
    return param

class RaporForm(forms.Form):

    def __init__(self, qs, *args, **kwargs):
        get_param(qs)
        print(qs)
        super().__init__(*args, **kwargs)
        for item in qs:
            self.fields[item] = forms.CharField(max_length=2)
        self.fields['sakit'] = forms.CharField(max_length=2)
        self.fields['izin'] = forms.CharField(max_length=2)
        self.fields['alpha'] = forms.CharField(max_length=2)
           
class SubjectForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        queryset=user.objects.all(),
        widget=forms.Select(attrs={
          'class': 'select2-show-search' #is this POSSIBLE?
          })    
    )
    class Meta:
        model = subjects
        fields = '__all__'

class SubjectDocForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        queryset=user.objects.all(),
        widget=forms.Select(attrs={
          'class': 'select2-show-search' #is this POSSIBLE?
          })    
    )
    class Meta:
        model = subject_doc
        fields = '__all__'


