# Generated by Django 3.2.6 on 2021-09-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_datatime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datatime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
