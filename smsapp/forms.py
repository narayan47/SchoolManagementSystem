from django import forms
from .models import*


class ClassSetupForm(forms.ModelForm ):
    class Meta:
        model = ClassSetup
        fields = '__all__'
        # exclude = ('section_name',)

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        
        self.fields['section_name'].queryset = Section.objects.none()
        self.fields['subject_name'].queryset = Subject.objects.none()
        self.fields['class_teacher'].queryset = Teacher.objects.none()


        
        print('I am here in form')




        if 'class_name' in self.data and 'subject_name' in self.data:
            
            try:
                class_name_id = int( self.data.get( 'class_name' ) )
                print('Now im going to save data in section with class id ', class_name_id)
               
                self.fields['section_name'].queryset = Section.objects.filter(standard_name_id=class_name_id )
                self.fields['subject_name'].queryset = Subject.objects.filter(class_name_id=class_name_id )


                subject_name_id = int(self.data.get('subject_name'))
                print('Now im going to save data in teacher with sub id ', subject_name_id)
                self.fields['class_teacher'].queryset = Teacher.objects.filter(teaching_subjects=subject_name_id )

            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            print('I am here in instance pk')
            # self.fields['section_name'].queryset = self.instance.section_name.set
            # self.fields['subject_name'].queryset = self.instance.subject_name
            # self.fields['class_teacher'].queryset = self.instance.class_teacher
            pass
        else:
           pass




class SectionForm( forms.ModelForm ):
    class Meta:
        model = Section
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super( SectionForm, self ).__init__( *args, **kwargs )
        self.fields['standard_name'].empty_label = 'Select class'


class TeacherForm( forms.ModelForm ):
    class Meta:
        model = Teacher
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super( TeacherForm, self ).__init__( *args, **kwargs )
        self.fields['roles'].empty_label = 'Select role'




class StudentForm( forms.ModelForm ):

    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        print('ma first yeha xu')
        self.fields['current_section'].queryset = Section.objects.none()

        if 'current_class' in self.data:
            try:
                class_name_id = int( self.data.get( 'current_class' ) )
                print(class_name_id)
                print('ma save huna jadoi xu')
                self.fields['current_section'].queryset = Section.objects.filter(standard_name_id=class_name_id )
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['current_section'].queryset = self.instance.class_name.section_name_set        



class SubjectForm( forms.ModelForm ):
    class Meta:
        model = Subject
        fields = '__all__'

    