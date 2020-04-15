from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    #path( '', views.index, name='index' ),

    path( '', views.admin_setting, name='admin_setting' ),

    path( 'admin_setting/', views.admin_setting, name='admin_setting' ),

    
 


    # For ClassSetup Model
    path( 'class_setup_add_edit/', views.class_setup_add_edit, name='class_setup_add_edit' ),
    path( 'class_setup_view/', views.class_setup_view, name='class_setup_view' ),
    path( 'class_setup_update/<int:id>', views.class_setup_add_edit, name='class_setup_update' ),
    path( 'class_setup_delete/<int:id>', views.class_setup_delete, name='class_setup_delete' ),
    path( 'dropdown_section_class_setup/', views.dropdown_section_class_setup, name='dropdown_section_class_setup' ),
    path( 'dropdown_subject_class_setup/', views.dropdown_subject_class_setup, name='dropdown_subject_class_setup' ),
    path( 'dropdown_teacher_class_setup/', views.dropdown_teacher_class_setup, name='dropdown_teacher_class_setup' ),




    # For SubjectCombination Model
    path( 'section_add_edit/', views.section_add_edit, name='section_add_edit' ),
    path( 'section_view/', views.section_view, name='section_view' ),
    path( 'section_update/<int:id>', views.section_add_edit, name='section_update' ),
    path( 'section_delete/<int:id>', views.section_delete, name='section_delete' ),

    # For Teacher Model
    path( 'teacher_add_edit/', views.teacher_add_edit, name='teacher_add_edit' ),
    path( 'teacher_view/', views.teacher_view, name='teacher_view' ),
    path( 'teacher_update/<int:id>', views.teacher_add_edit, name='teacher_update' ),
    path( 'teacher_delete/<int:id>', views.teacher_delete, name='teacher_delete' ),

    # For Student Model
    path( 'student_add_edit/', views.student_add_edit, name='student_add_edit' ),
    path( 'student_view/', views.student_view, name='student_view' ),
    path( 'student_update/<int:id>', views.student_add_edit, name='student_update' ),
    path( 'student_delete/<int:id>', views.student_delete, name='student_delete' ),
    path( 'dropdown_section_student/', views.dropdown_section_student, name='dropdown_section_student' ),


    # For SubjectCombination Model
    path( 'subject_add_edit/', views.subject_add_edit, name='subject_add_edit' ),
    path( 'subject_view/', views.subject_view, name='subject_view' ),
    path( 'subject_update/<int:id>', views.subject_add_edit, name='subject_update' ),
    path( 'subject_delete/<int:id>', views.subject_delete, name='subject_delete' ),



    #class_Summary
    path( 'class_summary/', views.class_summary, name='class_summary' ),



]
