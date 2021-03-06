# Generated by Django 2.2 on 2020-04-26 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='section',
            name='standard_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sections', to='smsapp.Standard'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='names',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterModelTable(
            name='section',
            table='section',
        ),
        migrations.AlterModelTable(
            name='standard',
            table='standard',
        ),
    ]
