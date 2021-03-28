from django.urls import path,re_path, include
from django.conf.urls import url
from app.views import AddBill, AddFile, AddParent, ImportPlpRecord, AddPlp,ViewCleanExport, AddPlpRecord, AddStudent, AddSubject, AddSubjectDoc, AddUser, CheckAPi, DeleteAllBill, DeleteAllParent, DeleteAllPlp, DeleteAllPlpRecord, DeleteAllStudent, DeleteAllSubject, DeleteAllSubjectDoc, DeleteBill, DeleteParent, DeletePlp, DeletePlpRecord, DeleteStudent, DeleteSubject, DeleteSubjectDoc, DeleteUser, FillRapor, ImportParent, ImportStudent, ListBill, ListFile, ListParent, ListPlp, ListPlpRecord, ListStudent, ListSubject, ListSubjectDoc, ListUser, PrintPlpRecord, UpdateBill, UpdateParent, UpdatePassword, UpdatePlp, UpdatePlpRecord, UpdateStudent, UpdateSubject, UpdateSubjectDoc, UpdateUser, ViewExportBundle, ViewExportList, ViewHomepage, ViewLogin, ViewLogout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,\
PasswordResetCompleteView,PasswordChangeView
from django.contrib.auth import views as auth_views
from app import models
urlpatterns = [
    path('',ViewHomepage.as_view(),name='home'),
    path('login/',ViewLogin.as_view(), name='login'),
    path('logout/',ViewLogout.as_view(), name='logout'),
    path('forget-password/',PasswordResetView.as_view(), name='forget-password'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/(<str:uidb64>/<str:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('list-user/',ListUser.as_view(),name='list-user'),
    path('add-user/',AddUser.as_view(),name='add-user'),
    path('update-password/',UpdatePassword.as_view(template_name = "registration/password_change_form.html"),name='update-password'),
    path('delete-user/<str:pk>/', DeleteUser.as_view(), name='delete-user'),
  
    path('update-user/<str:pk>/', UpdateUser.as_view(), name='update-user'),
    #parent
    path('list-parent/',ListParent.as_view(),name='list-parent'),
    path('add-parent/',AddParent.as_view(),name='add-parent'),
    path('update-parent/<str:pk>/',UpdateParent.as_view(),name='update-parent'),
    path('delete-parent/<str:pk>/',DeleteParent.as_view(),name='delete-parent'),
    path('searchableselect/', include('searchableselect.urls')),
    path('del-par/',DeleteAllParent.as_view(),name='delpar'),
    path('import-parent/',ImportParent.as_view(),name='import-parent'),
    #extra
    path('list-file/',ListFile.as_view(),name='list-file'),
    path('add-file/',AddFile.as_view(),name='add-file'),
    #student
    path('list-student/',ListStudent.as_view(),name='list-student'),
    path('add-student/',AddStudent.as_view(),name='add-student'),
    path('del-stud/',DeleteAllStudent.as_view(),name='del-stud'),
    path('update-student/<str:pk>/',UpdateStudent.as_view(),name='update-student'),
    path('delete-student/<str:pk>/',DeleteStudent.as_view(),name='delete-student'),
    path('import-student/',ImportStudent.as_view(),name='import-student'),
    #bill
    path('list-bill/',ListBill.as_view(),name='list-bill'),
    path('add-bill/',AddBill.as_view(),name='add-bill'),
    path('del-bill/',DeleteAllBill.as_view(),name='del-bill'),
    path('update-bill/<str:pk>/',UpdateBill.as_view(),name='update-bill'),
    path('delete-bill/<str:pk>/',DeleteBill.as_view(),name='delete-bill'),
    #plp
    path('list-plp/',ListPlp.as_view(),name='list-plp'),
    path('add-plp/',AddPlp.as_view(),name='add-plp'),
    path('del-plp/',DeleteAllPlp.as_view(),name='del-plp'),
    path('update-plp/<str:pk>/',UpdatePlp.as_view(),name='update-plp'),
    path('delete-plp/<str:pk>/',DeletePlp.as_view(),name='delete-plp'),
    #plp record
    path('list-plp-record/',ListPlpRecord.as_view(),name='list-plp-record'),
    path('add-plp-record/',AddPlpRecord.as_view(),name='add-plp-record'),
    path('del-plp-record/',DeleteAllPlpRecord.as_view(),name='del-plp-record'),
    path('import-plp-record/',ImportPlpRecord.as_view(),name='import-plp-record'),
    path('print-plp-record/<str:pk>/',PrintPlpRecord.as_view(),name='print-plp-record'),
    path('update-plp-record/<str:pk>/',UpdatePlpRecord.as_view(),name='update-plp-record'),
    path('delete-plp-record/<str:pk>/',DeletePlpRecord.as_view(),name='delete-plp-record'),
    #Test
    path('test/',CheckAPi.as_view(),name='test'),
    #RaporFill
    path('fill-rapor/<str:pk>/',FillRapor.as_view(),name='fill-rapor'),
     #subject
    path('list-subject/',ListSubject.as_view(),name='list-subject'),
    path('add-subject/',AddSubject.as_view(),name='add-subject'),
    path('del-subject/',DeleteAllSubject.as_view(),name='del-subject'),
    path('update-subject/<str:pk>/',UpdateSubject.as_view(),name='update-subject'),
    path('delete-subject/<str:pk>/',DeleteSubject.as_view(),name='delete-subject'),

         #subject document
    path('list-subject-doc/',ListSubjectDoc.as_view(),name='list-subject-doc'),
    path('add-subject-doc/',AddSubjectDoc.as_view(),name='add-subject-doc'),
    path('del-subject-doc/',DeleteAllSubjectDoc.as_view(),name='del-subject-doc'),
    path('update-subject-doc/<str:pk>/',UpdateSubjectDoc.as_view(),name='update-subject-doc'),
    path('delete-subject-doc/<str:pk>/',DeleteSubjectDoc.as_view(),name='delete-subject-doc'),
    #Export
    path('export-excel/',ViewExportList.as_view(),name='export-excel'),
    path('export-bundle/',ViewExportBundle.as_view(),name='export-bundle'),
    path('export-delete/',ViewCleanExport.as_view(),name='export-delete')
]