# Generated by Django 3.2.6 on 2021-09-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_bloguser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='age',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
    ]