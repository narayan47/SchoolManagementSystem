# Generated by Django 2.2 on 2020-04-15 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Section Name')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(choices=[('One', 'One'), ('Two', 'Two'), ('Three', 'Three'), ('Four', 'Four'), ('Five', 'Five'), ('Six', 'Six')], max_length=20, verbose_name='Class Name')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Subject Name(s)')),
                ('class_name', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='smsapp.Standard', verbose_name='Class Name')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Teacher Name')),
                ('roles', models.CharField(choices=[('CT', 'Class Teacher'), ('ST', 'Subject Teacher'), ('PT', 'Part Time Teacher'), ('NT', 'Normal Teacher'), ('P', 'Principle')], max_length=20, verbose_name='Role(s)')),
                ('teaching_subjects', models.ManyToManyField(to='smsapp.Subject', verbose_name='Teaching Subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Student Name')),
                ('roll_no', models.IntegerField(verbose_name='Roll No.')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, verbose_name='Select Gender')),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsapp.Standard', verbose_name='Current Class')),
                ('current_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsapp.Section', verbose_name='Current Section')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='standard_name',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='smsapp.Standard', verbose_name='Class Name'),
        ),
        migrations.CreateModel(
            name='ClassSetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.ForeignKey(max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='smsapp.Standard', verbose_name='Class Name')),
                ('class_teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='smsapp.Teacher', verbose_name='Teacher')),
                ('section_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsapp.Section', verbose_name='Section Name')),
                ('subject_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsapp.Subject', verbose_name='Subject Name')),
            ],
        ),
    ]
