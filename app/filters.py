import django_filters
from app.models import bills, parents, plprecord, plps, students, subject_doc, user

class UserFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(field_name='full_name', lookup_expr='contains', label='Full Name')
    email = django_filters.CharFilter(field_name='email', lookup_expr='contains', label='Email')
    mobile_number = django_filters.CharFilter(field_name='mobile_number', lookup_expr='contains', label='Mobile Number')
    class Meta:
        model = user
        fields=('full_name','email','mobile_number')

class ParentFilter(django_filters.FilterSet):
    parent_email = django_filters.CharFilter(field_name='parent_email', lookup_expr='contains', label='Email')
    parent_name = django_filters.CharFilter(field_name='parent_name', lookup_expr='contains', label='Full Name')
    parent_mobile = django_filters.CharFilter(field_name='parent_mobile', lookup_expr='contains', label='Mobile Number')
    class Meta:
        model = parents
        fields=('parent_email','parent_name','parent_mobile')

class StudentFilter(django_filters.FilterSet):
    student_nis = django_filters.CharFilter(field_name='student_nis', lookup_expr='contains', label='Nis')
    student_name = django_filters.CharFilter(field_name='student_name', lookup_expr='contains', label='Name')
    class Meta:
        model = students
        fields=('student_nis','student_name')

class BillFilter(django_filters.FilterSet):
    class Meta:
        model = bills
        fields=('bill_type','fee')

class PlpFilter(django_filters.FilterSet):
    class Meta:
        model = plps
        fields=('plp_code','plp_name')

class PlpRecordFilter(django_filters.FilterSet):
    class Meta:
        model = plprecord
        fields=('student','plp')

class SubjectDocFilter(django_filters.FilterSet):
    class Meta:
        model = subject_doc
        fields=('title',)

