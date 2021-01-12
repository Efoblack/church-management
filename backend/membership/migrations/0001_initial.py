# Generated by Django 3.1.5 on 2021-01-11 18:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import membership.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=150, null=True)),
                ('contact_1', models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number be entered in the format: +233123456789', regex='^\\+?1?\\d{10,13}$')])),
                ('contact_2', models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number be entered in the format: +233123456789', regex='^\\+?1?\\d{10,13}$')])),
                ('occupation', models.CharField(blank=True, max_length=120, null=True)),
                ('student', models.BooleanField(default=False)),
                ('picture', models.ImageField(upload_to=membership.models.upload_path)),
                ('mothers_contact', models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number be entered in the format: +233123456789', regex='^\\+?1?\\d{10,13}$')])),
                ('fathers_contact', models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number be entered in the format: +233123456789', regex='^\\+?1?\\d{10,13}$')])),
                ('marital_status', models.CharField(choices=[('MARRIED', 'Married'), ('SINGLE', 'Single')], default='SINGLE', max_length=7)),
                ('children_no', models.IntegerField(blank=True, null=True)),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.ministry')),
            ],
        ),
    ]
