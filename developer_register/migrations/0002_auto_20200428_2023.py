# Generated by Django 3.0.5 on 2020-04-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=20),
        ),
    ]
