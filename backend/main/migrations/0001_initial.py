# Generated by Django 5.0.6 on 2024-06-05 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('years_at_comapany', models.IntegerField()),
                ('last_perfomance_rating', models.IntegerField()),
            ],
        ),
    ]