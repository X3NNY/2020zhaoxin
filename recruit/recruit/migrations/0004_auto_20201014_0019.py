# Generated by Django 2.2.7 on 2020-10-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0003_user_solved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='solved',
            field=models.CharField(default='{}', max_length=512, null=True),
        ),
    ]