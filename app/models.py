from django.db import models
from django.contrib.auth.models  import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,full_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, full_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.email, filename)
    # return '{0}/{1}'.format(instance.album.album_name, filename)
    case_name = instance.user.email
    file_name = filename.lower().replace(" ", "_")
    return "Users/{}/{}".format(case_name, file_name)

class user(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=100, primary_key=True)
    full_name = models.CharField(max_length=160, blank=True)
    mobile_number = models.CharField(max_length=13,blank=True)
    is_admin = models.BooleanField(default=False)
    is_login = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    kadiv = models.ForeignKey('self',blank=True, null=True, on_delete=models.CASCADE)
    objects = UserManager()
    date_joined = models.DateTimeField(default=timezone.now)
    user_photo = models.ImageField(upload_to=user_directory_path, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    def __str__(self):
        return "%s - %s " % (self.email, self.full_name)

    @property
    def is_staff(self):
        "Is the user a member of teacher?"
        # Simplest possible answer: All admins are teacher
        return self.is_admin

def excel_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.email, filename)
    # return '{0}/{1}'.format(instance.album.album_name, filename)
    # case_name = instance.students.nis_student
    file_name = filename.lower().replace(" ", "_")
    return "Excel/{}/{}".format( file_name)

class uploadrecords(models.Model):
    file_name = models.CharField(max_length=160)
    file = models.FileField(upload_to=excel_directory_path)
    uploaded_date = models.DateField(default=timezone.now)
    uploaded_by = models.ForeignKey(user, on_delete=models.CASCADE)

class parents(models.Model):
    parent_email = models.CharField(max_length=160, primary_key=True)
    parent_name = models.CharField(max_length=100)
    parent_mobile = models.CharField(max_length=14)
    parent_add = models.TextField(blank=True, null=True)
    def __str__(self):
        return "%s - %s " % (self.parent_name, self.parent_email)

def student_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.email, filename)
    # return '{0}/{1}'.format(instance.album.album_name, filename)
    case_name = instance.nis_student
    file_name = filename.lower().replace(" ", "_")
    return "Students/{}/{}".format(case_name, file_name)

class students(models.Model):
    GENDER = (
        ('P', 'Perempuan'),
        ('L', 'Laki-Laki'),
    )
    CLASS = (
        ('1 (Satu)', 'I'),
        ('2 (Dua)', 'II'),
        ('3 (Tiga)', 'III'),
        ('4 (Empat)', 'IV'),
        ('5 (Lima)', 'V'),
        ('6 (Enam)', 'VI'),
    )
    SEMESTER = (
        ('Ganjil', 'Ganjil'),
        ('Genap', 'Genap'),
    )
    parent = models.ForeignKey(parents,related_name='parent', on_delete=models.CASCADE, blank=True, null=True)
    nis_student = models.CharField(max_length=20, primary_key=True)
    name_student = models.CharField(max_length=100)
    pob_student = models.CharField(max_length=20)
    dob_student = models.DateField(default=timezone.now, blank=True,null=True)
    sex_student = models.CharField(max_length=1,choices=GENDER)
    add_student = models.TextField(blank=True)
    class_student = models.TextField(blank=True, max_length=30, choices=CLASS)
    sem_student = models.TextField(blank=True, max_length=10, choices=SEMESTER)
    photo_student = models.ImageField(upload_to=student_directory_path, blank=True, null=True)

    @property
    def pdob(self):
        return '{0}, {1}'.format(self.pob_student, self.dob_student)
    
    def __str__(self):
        return '{0}, {1}'.format(self.nis_student, self.name_student)

class bill_types(models.Model):
    bill_type = models.CharField(max_length=20)

def bill_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.email, filename)
    # return '{0}/{1}'.format(instance.album.album_name, filename)
    case_name = instance.bill_type
    file_name = filename.lower().replace(" ", "_")
    return "Bill/{}/{}".format(case_name, file_name)


class bills(models.Model):
    BILL_TYPE = (
        ('S', 'Uang Bulanan'),
        ('P', 'Uang Pangkal'),
        ('L', 'Lain-Lain'),
    )
    student = models.ForeignKey(students,on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=1, choices=BILL_TYPE)
    fee = models.DecimalField(decimal_places=2, max_digits=12)
    updated_date = models.DateField(default=timezone.now)
    attachment = models.FileField(upload_to=bill_directory_path,blank=True,null=True)

def rapor_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.email, filename)
    # return '{0}/{1}'.format(instance.album.album_name, filename)
    case_name = instance.plp_name
    file_name = filename.lower().replace(" ", "_")
    return "Rapor/{}/{}".format(case_name, file_name)

class plps(models.Model):
    plp_code = models.CharField(max_length=10, primary_key=True)
    plp_name = models.CharField(max_length=20)
    plp_rapor_qbs = models.FileField(blank=True, upload_to=rapor_directory_path, null=True)
    plp_rapor_fq = models.FileField(blank=True, upload_to=rapor_directory_path, null=True)
    plp_leader = models.ForeignKey(user, on_delete=models.CASCADE, blank=True,null=True)
    def __str__(self):
        return '{0}, {1}'.format(self.plp_code, self.plp_name)

def rapor_record_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.email, filename)
    # return '{0}/{1}'.format(instance.album.album_name, filename)
    case_name = instance.student
    file_name = filename.lower().replace(" ", "_")
    return "Rapor/{}/{}".format(case_name, file_name)

class plprecord(models.Model):
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    plp = models.ForeignKey(plps, on_delete=models.CASCADE)
    join_plp = models.DateField(default=timezone.now)
    status = models.BooleanField(default=True)
    report_excel = models.FileField(upload_to=rapor_record_directory_path,  blank=True, null=True)
    report_result = models.FileField(upload_to=rapor_record_directory_path, blank=True, null=True)
    position = models.IntegerField()
    o_nilai = models.TextField(blank=True, null=True)
    def __str__(self):
        return '{0}, {1}'.format(self.student, self.plp)

# class content_rapor(models.Model):
#     plprecord = models.ForeignKey(plprecord, on_delete=models.CASCADE)
#     # plp = models.ForeignKey(plps,on_delete=models.CASCADE, blank=True, null=True)
#     # student = models.ForeignKey(students,on_delete=models.CASCADE, blank=True, null=True)
#     o_nilai = models.TextField(blank=True)
#     date = models.DateField(default=timezone.now)
#     user = models.ForeignKey(user, on_delete=models.CASCADE, blank=True, null=True)

class subjects(models.Model):
    teacher = models.ForeignKey(user, related_name='subject_teacher',on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    def __str__(self):
        return self.subject_name

# class plpreport(models.Model):
#     record = models.ForeignKey(plprecord, on_delete=models.CASCADE)

def subject_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.email, filename)
    # return '{0}/{1}'.format(instance.album.album_name, filename)
    case_name = instance.subject
    file_name = filename.lower().replace(" ", "_")
    return "Subjects/{}/{}".format(case_name, file_name)

class subject_doc(models.Model):
    subject = models.ForeignKey(subjects, on_delete=models.CASCADE)
    title = models.CharField(max_length=360)
    file = models.FileField(upload_to=subject_directory_path)


# class plp_rapor(models.Model):
#     plp = models.ForeignKey(plps, on_delete=models.CASCADE)
#     rapor_section = models.CharField(max_length=100)
#     section_file = models.FileField(upload_to=rapor_directory_path)
#     def __str__(self):
#         return "%s - %s " % (self.plp, self.rapor_section)
# class subjects(models.Model):
#     subject_name = models.CharField(max_length=30)

# class reports(models.Model):

    
# def subject_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     # return 'user_{0}/{1}'.format(instance.user.email, filename)
#     # return '{0}/{1}'.format(instance.album.album_name, filename)
#     case_name = instance.subjects.subject_name
#     file_name = filename.lower().replace(" ", "_")
#     return "Subject/{}/{}".format(case_name, file_name)

# class subjects(models.Model):
#     teacher = models.ForeignKey(user, related_name='subject_teacher',on_delete=models.CASCADE)
#     subject_name = models.CharField(max_length=100)
#     subject_icon = models.ImageField(upload_to=subject_directory_path)

# def plp_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     # return 'user_{0}/{1}'.format(instance.user.email, filename)
#     # return '{0}/{1}'.format(instance.album.album_name, filename)
#     case_name = instance.plp.plp_name
#     file_name = filename.lower().replace(" ", "_")
#     return "Classes/{}/{}".format(case_name, file_name)

# class plps(models.Model):
#     teacher = models.ForeignKey(user, related_name='plp_teacher', on_delete=models.CASCADE)
#     plp_name = models.CharField(max_length=30)
#     plp_icon = models.ImageField(upload_to=plp_directory_path, blank=True)

# class rec_plp(models.Model):
#     plp = models.ForeignKey(plps,related_name='rec_plp',on_delete=models.CASCADE)
#     student = models.ForeignKey(students,related_name='rec_plp_student',on_delete=models.CASCADE)
#     rec_date = models.DateField(default=timezone.now)
#     is_active = models.BooleanField(default=True)

# class schedules(models.Model):
#     day = models.CharField(max_length=15)
#     subject = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='subjects')
#     plp = models.ForeignKey(plps, related_name='schedule_plp',on_delete=models.CASCADE)
#     start_time = models.TimeField(blank=True)
#     end_time = models.TimeField(blank=True)

# class absences(models.Model):
#     schedule = models.ForeignKey(schedules, related_name='absence_schedule', on_delete=models.CASCADE)
#     student = models.ForeignKey(student,related_name='absence_student', on_delete=models.CASCADE)
#     is_attend = models.BooleanField(default=False)
#     is_alpha = models.BooleanField(default=False)
#     is_permit = models.BooleanField(default=False)
#     is_ill = models.BooleanField(default=False)
#     detail = models.TextField(blank=True)

# class exams(models.Model):
#     subject = models.ForeignKey(subjects,on_delete=models.CASCADE,related_name='exam_subject')
#     student = models.ForeignKey(students,on_delete=models.CASCADE,related_name='exam_student')
#     value = models.DecimalField()
#     exam_date = models.DateField(default=timezone.now)
#     exam_type = models.CharField(max_length=30)
#     detail = models.TextField(blank=True)






