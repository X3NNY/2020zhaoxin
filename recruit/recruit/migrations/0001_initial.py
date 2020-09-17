# Generated by Django 2.2.7 on 2020-09-16 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=16)),
                ('userPassword', models.CharField(max_length=512)),
                ('userEmail', models.EmailField(max_length=254)),
                ('userQQ', models.IntegerField(null=True)),
                ('userFlagSum', models.IntegerField(default=0)),
                ('userLatestFlag', models.CharField(default='NSS{W3LCOM3_TO_SWPU}', max_length=32)),
            ],
        ),
    ]
