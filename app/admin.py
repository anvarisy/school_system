from django.contrib import admin
from app.models import parents, students, user
from django.contrib.auth.models import Permission
from django import forms
# from searchableselect.widgets import SearchableSelect
# Register your models here.

# class StudentForm(forms.ModelForm):
#     parent = forms.ModelChoiceField(
#         queryset=parents.objects.all(),
#         widget=SearchableSelect(model='app.models.parents', search_field='parent_name', many=True, limit=10)
#     )
#     class Meta:
#         model = students
#         fields = ('nis_student','parent')

# @admin.register(students)
# class StudentAdmin(admin.ModelAdmin):
#     form = StudentForm

admin.site.register(user)
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('content_type')