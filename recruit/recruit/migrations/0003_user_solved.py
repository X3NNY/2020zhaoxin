# Generated by Django 2.2.7 on 2020-10-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='solved',
            field=models.CharField(max_length=512, null=True),
        ),
    ]