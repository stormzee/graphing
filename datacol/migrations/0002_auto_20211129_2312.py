# Generated by Django 3.2.9 on 2021-11-29 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacol', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdmissionOutcome',
        ),
        migrations.DeleteModel(
            name='AgeCategory',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='CountryList',
        ),
        migrations.DeleteModel(
            name='Datapoints',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='PeopleData',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
