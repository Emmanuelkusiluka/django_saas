# Generated by Django 3.1 on 2020-10-23 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]