# Generated by Django 3.2.5 on 2021-08-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_eventreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPractice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]
