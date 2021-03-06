# Generated by Django 4.0.4 on 2022-06-07 18:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventlogapp', '0008_servers_application_alter_details_servertype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Comments',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='PerformedBy',
            field=models.CharField(blank=True, choices=[('karvinth', 'Arvinth'), ('ahegde', 'Ashik'), ('sdey', 'Saikat'), ('vsatisha', 'Vinay'), ('snegalur', 'Santosh'), ('cursu', 'Catalina'), ('jlove', 'Joe')], max_length=20, null=True),
        ),
    ]
