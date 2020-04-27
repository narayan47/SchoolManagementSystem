from django.db import models

# HELPER MODELS BEGIN HERE

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

CLASS_CHOICES = (
    ('One', 'One'),
    ('Two', 'Two'),
    ('Three', 'Three'),
    ('Four', 'Four'),
    ('Five', 'Five'),
    ('Six', 'Six'),
)

ROLE_CHOICES = (
    ('CT', 'Class Teacher'),
    ('ST', 'Subject Teacher'),
    ('PT', 'Part Time Teacher'),
    ('NT', 'Normal Teacher'),
    ('P', 'Principle'),
)

SUBJECT_CHOICES = (
    ('Eng', 'English'),
    ('Math', 'Math'),
    ('Sci', 'Science'),
    ('Soc', 'Social'),
    ('EHP', 'Environment Health and Population'),
    ('OPT1', 'Optional Math'),
    ('OPT2', 'Economics'),
)


class Subject( models.Model ):
    class_name = models.ForeignKey('Standard', max_length=20, on_delete=models.CASCADE, verbose_name='Class Name' )
    name = models.CharField(max_length=20, verbose_name='Subject Name(s)' )



    def __str__(self):
        return str( self.name )


class Standard(models.Model):  # standard

    names = models.CharField(max_length=255,choices=CLASS_CHOICES)

    class Meta:
        db_table = 'standard'

    def __str__(self):
        return self.names

    def get_sections(self):
        return ', '.join(self.sections.all().values_list('name', flat=True))


class Section(models.Model):  # section

    name = models.CharField(max_length=255, verbose_name='Section Name')
    standard_name = models.ForeignKey(
        Standard,
        related_name='sections', on_delete=models.CASCADE,
        null=True)

    class Meta:
        db_table = 'section'

    def __str__(self):
        return self.name


class ClassSetup( models.Model ):
    class_name      = models.ForeignKey(Standard, on_delete=models.CASCADE, null=True, max_length=20,verbose_name='Class Name' )
    section_name    = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, verbose_name='Section Name' )
    subject_name    = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, verbose_name='Subject Name' ) 

    class_teacher   = models.ForeignKey('Teacher', on_delete=models.CASCADE, blank=True, verbose_name='Teacher' )

   

    def __str__(self):
        return str( self.section_name )


class Student( models.Model ):
    name = models.CharField( max_length=50, verbose_name='Student Name' )
    roll_no = models.IntegerField( verbose_name='Roll No.' )
    gender = models.CharField( max_length=10, choices=GENDER_CHOICES, verbose_name='Select Gender' )
    current_class = models.ForeignKey(Standard, on_delete=models.CASCADE, verbose_name='Current Class' )
    current_section = models.ForeignKey( Section, on_delete=models.CASCADE,verbose_name='Current Section' )

    def __str__(self):
        return str( self.name )


class Teacher( models.Model ):
    name = models.CharField( max_length=20, verbose_name='Teacher Name' )
    roles = models.CharField( max_length=20, choices=ROLE_CHOICES, verbose_name='Role(s)' )
    teaching_subjects = models.ManyToManyField(Subject, verbose_name='Teaching Subjects' )

    def __str__(self):
        return str( self.name )

    # def save(self, *args, **kwargs):
    #     for s in ClassSetup.objects.all():
    #         if s.sub_names in self.name:
    #             self.sub_names = s
    #             break
    #     super().save(*args, **kwargs)


