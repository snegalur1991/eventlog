# Generated by Django 4.0.4 on 2022-06-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventlogapp', '0007_servers_vipip_servers_vipname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='Application',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='ServerType',
            field=models.CharField(blank=True, choices=[('Production', 'Production'), ('Staging', 'Staging'), ('Development', 'Development'), ('Pre-Production', 'Pre-Production'), ('Decommissioned', 'Decommissioned')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='servers',
            name='ServerType',
            field=models.CharField(blank=True, choices=[('Production', 'Production'), ('Staging', 'Staging'), ('Development', 'Development'), ('Pre-Production', 'Pre-Production'), ('Decommissioned', 'Decommissioned')], default='', max_length=20, null=True),
        ),
    ]
