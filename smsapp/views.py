from django.contrib import messages
from django.shortcuts import render, redirect
import re
from .forms import*

from .models import*


app_name = 'smsapp'


def get_verbose_name(model_name):
    verbose_name_list = []
    for f in model_name._meta.get_fields():
        if hasattr(f, 'verbose_name' ):
            verbose_name_list.append( f.verbose_name )
    return verbose_name_list


def camel_case_split(CamelCaseStr):
    strlist = re.findall( r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', CamelCaseStr )
    class_name = ""
    lower_class_name = ""
    for item in strlist:
        class_name += " " + item
        lower_class_name += item.lower() + "_"
    return class_name, lower_class_name


def get_class_name(model_name):
    return camel_case_split( model_name.__name__ )


def get_class_fields(model_name):
    return [f.get_attname() for f in model_name._meta.fields]


# Create your views here.
def index(request):
    return render( request, 'smsapp/base.html' )


def admin_setting(request):
    return render( request, 'smsapp/admin_setting.html' )


#  CRUD Operation Class Model
def class_setup_add_edit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ClassSetupForm()
        else:
            obj = ClassSetup.objects.get( pk=id )
            form = ClassSetupForm( instance=obj )
        return render( request, 'smsapp/class_setup_add_edit.html',
                       {"form": form} )
    else:
        if id == 0:
            form = ClassSetupForm(request.POST )
           
        else:
            obj = ClassSetup.objects.get( pk=id )
            form = ClassSetupForm( request.POST, instance=obj )
        
        if form.is_valid():
            form.save()
            messages.info( request, "Data saved Sucessfully!" )
        else:
            messages.warning( request, "Data is not saved!" )
        return redirect( 'smsapp:class_summary' )


def class_setup_view(request):
    verbose_names = get_verbose_name( ClassSetup )
    context = {'view_list': ClassSetup.objects.all(),
               'verbose_names': verbose_names}

    return render( request, 'smsapp/class_setup_view.html', context )


def class_setup_delete(request, id):
    obj = ClassSetup.objects.get( pk=id )
    obj.delete()
    messages.success( request, "Data deleted Sucessfully!" )
    return redirect( 'smsapp:class_summary' )


#  CRUD Operation Section Model
def section_add_edit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = SectionForm()
        else:
            obj = Section.objects.get( pk=id )
            form = SectionForm( instance=obj )
        return render( request,
                       'smsapp/section_add_edit.html',
                       {"form": form} )
    else:
        if id == 0:
            form = SectionForm( request.POST )
        else:
            obj = Section.objects.get( pk=id )
            form = SectionForm( request.POST, instance=obj )
        if form.is_valid():
            form.save()
            messages.success( request, "Data Added Successfully!" )
        return redirect( 'smsapp:section_view' )


def section_view(request):
    class_name, lower_class_name = get_class_name( Section )

    verbose_name = get_verbose_name( Section )

    field_names = get_class_fields( Section )
    # print(field_names)

    view_list = Section.objects.all()

    context = {'view_list': view_list,
               'verbose_names': verbose_name,
               'class_name': class_name,
               'lower_class_name': lower_class_name
               }
    return render( request, 'smsapp/section_view.html',
                   context )


def section_delete(request, id):
    obj = Section.objects.get( pk=id )
    obj.delete()
    messages.warning( request, "Data Deleted Successfully!" )
    return redirect( 'smsapp:section_view' )


#  CRUD Operation Teacher Model
def teacher_add_edit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TeacherForm()
        else:
            obj = Teacher.objects.get( pk=id )
            form = TeacherForm( instance=obj )
        return render( request, 'smsapp/teacher_add_edit.html', {"form": form} )
    else:
        if id == 0:
            form = TeacherForm( request.POST )
        else:
            obj = Teacher.objects.get( pk=id )
            form = TeacherForm( request.POST, instance=obj )
        if form.is_valid():
            form.save()
        messages.success( request, "Data Added Successfully!" )
        return redirect( 'smsapp:teacher_view' )


def teacher_view(request):
    class_name, lower_class_name = get_class_name( Teacher )

    verbose_name = get_verbose_name( Teacher )

    field_names = get_class_fields( Teacher )
    # print(field_names)

    view_list = Teacher.objects.all()

    context = {'view_list': view_list,
               'verbose_names': verbose_name,
               'class_name': class_name,
               'lower_class_name': lower_class_name
               }
    return render( request, 'smsapp/teacher_view.html', context )


def teacher_delete(request, id):
    obj = Teacher.objects.get( pk=id )
    obj.delete()
    messages.warning( request, "Data Deleted Successfully!" )
    return redirect( 'smsapp:teacher_view' )


#  CRUD Operation student Model
def student_add_edit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            obj = Student.objects.get( pk=id )
            form = StudentForm( instance=obj )
        return render( request, 'smsapp/student_add_edit.html', {"form": form} )
    else:
        if id == 0:
            form = StudentForm( request.POST )
            print("I am at Post")
        else:
            obj = Student.objects.get( pk=id )
            form = StudentForm( request.POST, instance=obj )
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success( request, "Data Added Successfully!" )
        else:
            messages.warning( request, "Failed to Add Data!" )
        return redirect( 'smsapp:student_view' )


def student_view(request):
    class_name, lower_class_name = get_class_name( Student )

    verbose_name = get_verbose_name( Student )

    field_names = get_class_fields( Student )
    # print(field_names)

    view_list = Student.objects.all()

    context = {'view_list': view_list,
               'verbose_names': verbose_name,
               'class_name': class_name,
               'lower_class_name': lower_class_name
               }
    return render( request, 'smsapp/student_view.html', context )


def student_delete(request, id):
    obj = Student.objects.get( pk=id )
    obj.delete()
    messages.warning( request, "Data Deleted Successfully!" )
    return redirect( 'smsapp:student_view' )



#  CRUD Operation subject Model
def subject_add_edit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = SubjectForm()
        else:
            obj = Subject.objects.get( pk=id )
            form = SubjectForm( instance=obj )
        return render( request,
                       'smsapp/subject_add_edit.html',
                       {"form": form} )
    else:
        if id == 0:
            form = SubjectForm( request.POST )
        else:
            obj = Subject.objects.get( pk=id )
            form = SubjectForm( request.POST, instance=obj )
        if form.is_valid():
            form.save()
            messages.success( request, "Data Added Successfully!" )
        return redirect( 'smsapp:subject_view' )


def subject_view(request):
    class_name, lower_class_name = get_class_name( Subject )

    verbose_name = get_verbose_name( Subject )

    field_names = get_class_fields( Subject )
    # print(field_names)

    view_list = Subject.objects.all()

    context = {'view_list': view_list,
               'verbose_names': verbose_name,
               'class_name': class_name,
               'lower_class_name': lower_class_name
               }
    return render( request, 'smsapp/subject_view.html',
                   context )


def subject_delete(request, id):
    obj = Subject.objects.get( pk=id )
    obj.delete()
    messages.warning( request, "Data Deleted Successfully!" )
    return redirect( 'smsapp:subject_view' )



def class_summary(request):
    verbose_names = get_verbose_name( ClassSetup )
    
    view_list_obj = ClassSetup.objects.all()
    class_id =list(set(sorted([item.class_name_id for item in view_list_obj])))
    class_list = list(set([str(item.class_name) for item in view_list_obj]))   
    
    def get_section_list(id):
        section_obj = ClassSetup.objects.filter(class_name_id = id)
        sec_list=[str(item_section.section_name) for item_section in section_obj]        
        return sec_list

    section_list= [get_section_list(id = item) for item in class_id]
    
    print(class_list)
    print(section_list)

    # context = {'view_list': ClassSetup.objects.all(),'verbose_names': verbose_names}
    context = {'view_list': ClassSetup.objects.all(),
                'class_list': class_list,
                'section_list': section_list,
                'verbose_names': verbose_names,
                
                }




    return render( request, 'smsapp/class_summary.html', context )



# for drop down selection
def dropdown_section_class_setup(request):
    class_name_id = request.GET.get('class_name' )
    #print("i am from", class_name_id)
    forms = Section.objects.filter(standard_name_id=class_name_id )
    #print(forms)

    #for var in forms:
        #print(var.name)

    return render( request, 'smsapp/section_dropdown_class_setup.html', {'forms': forms})


def dropdown_subject_class_setup(request):
    class_name_id = request.GET.get('class_name' )
    #print("i am from", class_name_id)
    forms = Subject.objects.filter(class_name_id=class_name_id )
    #print(forms)

    #for var in forms:
        #print(var.name)

    return render( request, 'smsapp/subject_dropdown_class_setup.html', {'forms': forms})



def dropdown_teacher_class_setup(request):
    subject_name_id = request.GET.get('subject_name' )
    #print(subject_name_id +'        is selected Subject ID kaskasfjkkfsajfkasjfkjasfjk')
    forms = Teacher.objects.filter(teaching_subjects=subject_name_id )
    # print(forms)

    # for var in forms:
    #     print(var.name)

    return render( request, 'smsapp/teacher_dropdown_class_setup.html', {'forms': forms})



def dropdown_section_student(request):
    current_class_id = request.GET.get('current_class')
    forms = Section.objects.filter(standard_name_id=current_class_id )

    return render( request, 'smsapp/section_dropdown_class_setup.html', {'forms': forms})
