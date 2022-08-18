# Generated by Django 4.0.6 on 2022-08-02 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('B', 'BUSINESS'), ('E', 'ECONOMIC'), ('L', 'LOW')], max_length=2)),
                ('beds', models.IntegerField(choices=[('one', 1), ('two', 2)])),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_code', models.CharField(max_length=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=16)),
                ('id_number', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('book_date', models.DateTimeField(auto_now=True)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.room')),
            ],
        ),
    ]
