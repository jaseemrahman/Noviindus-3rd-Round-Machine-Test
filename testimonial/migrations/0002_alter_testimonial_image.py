# Generated by Django 3.2.16 on 2023-01-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='testi'),
        ),
    ]