# Generated by Django 4.0.6 on 2022-08-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(choices=[('BUSINESS', 'B'), ('ECONOMIC', 'E'), ('LOW', 'L')], max_length=10),
        ),
    ]
