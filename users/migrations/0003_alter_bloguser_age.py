# Generated by Django 3.2.6 on 2021-09-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_bloguser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
