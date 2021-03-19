import django_tables2 as tables
from app.models import bills, parents, plprecord, plps, students, subject_doc, subjects, user
from django_tables2.utils import A
from django.utils.html import format_html

class UserTable(tables.Table):
    delete = tables.LinkColumn("delete-user", text="Delete", args=[A("pk")],orderable=False)
    update = tables.LinkColumn("update-user", text="Update", args=[A("pk")],orderable=False)
    class Meta:
        model = user
        template_name = "django_tables2/bootstrap4.html"
        fields = ('full_name','email','mobile_number','is_admin')
        exclude= ('password',)

class ParentTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)
    delete = tables.LinkColumn("delete-parent", text="Delete", args=[A("pk")],orderable=False)
    update = tables.LinkColumn("update-parent", text="Update", args=[A("pk")],orderable=False)
    class Meta:
        model = parents
        template_name = "django_tables2/bootstrap4.html"
        fields = ('selection','parent_email','parent_name','parent_mobile')

class ImageColumnStudent(tables.Column):
    def render(self, value):
        return format_html(
               '<img src="/media/{url}"/>',
                url=value
                )

class StudentTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)
    delete = tables.LinkColumn("delete-student", text="Delete", args=[A("pk")],orderable=False)
    update = tables.LinkColumn("update-student", text="Update", args=[A("pk")],orderable=False)
    pdob = tables.Column(accessor='pdob', verbose_name='Place, Date Of Birth')
    photo_student = ImageColumnStudent()
    class Meta:
        model = students
        template_name = "django_tables2/bootstrap4.html"
        fields = ('selection','nis_student','name_student','parent','pdob','photo_student')

class FileTable(tables.Table):
    file = tables.LinkColumn("delete-user", text="File", args=[A("pk")])
    view = tables.LinkColumn("delete-user", text="View", args=[A("pk")],orderable=False)
    imported = tables.LinkColumn("delete-user", text="Import", args=[A("pk")],orderable=False)
    class Meta:
        model = parents
        template_name = "django_tables2/bootstrap4.html"
        fields = ('file_name','file','uploaded_date','uploaded_by')

class BillTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)
    delete = tables.LinkColumn("delete-bill", text="Delete", args=[A("pk")],orderable=False)
    update = tables.LinkColumn("update-bill", text="Update", args=[A("pk")],orderable=False)
    class Meta:
        model = bills
        template_name = "django_tables2/bootstrap4.html"
        fields = ('selection','student','bill_type','fee','updated_date')

class PlpTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)
    delete = tables.LinkColumn("delete-plp", text="Delete", args=[A("pk")],orderable=False)
    update = tables.LinkColumn("update-plp", text="Update", args=[A("pk")],orderable=False)
    class Meta:
        model = plps
        template_name = "django_tables2/bootstrap4.html"
        fields = ('selection','plp_code','plp_name','plp_rapor_qbs','plp_rapor_fq','plp_leader')

class PlpRecordTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)
    delete = tables.LinkColumn("delete-plp-record", text="Delete", args=[A("pk")],orderable=False)
    update = tables.LinkColumn("update-plp-record", text="Update", args=[A("pk")],orderable=False)
    fill = tables.LinkColumn("fill-rapor", text="Manual", args=[A("pk")],orderable=False)
    # result = tables.LinkColumn("print-plp-record", text="Print", args=[A("pk")],orderable=False)
    class Meta:
        model = plprecord
        template_name = "django_tables2/bootstrap4.html"
        fields = ('selection','student','plp','join_plp','status','report_result')

class SubjectTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)
    delete = tables.LinkColumn("delete-subject", text="Delete", args=[A("pk")],orderable=False)
    update = tables.LinkColumn("update-subject", text="Update", args=[A("pk")],orderable=False)
    class Meta:
        model = subjects
        template_name = "django_tables2/bootstrap4.html"
        fields = ('selection','subject_name','teacher')

class SubjectDocTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)
    delete = tables.LinkColumn("delete-subject-doc", text="Delete", args=[A("pk")],orderable=False)
    update = tables.LinkColumn("update-subject-doc", text="Update", args=[A("pk")],orderable=False)
    class Meta:
        model = subject_doc
        template_name = "django_tables2/bootstrap4.html"
        fields = ('selection','subject_name','teacher')