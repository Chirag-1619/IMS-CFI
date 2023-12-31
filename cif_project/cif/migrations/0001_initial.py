# Generated by Django 4.2.2 on 2023-07-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('branch_code', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_details', models.CharField(max_length=100)),
                ('date_of_purchase', models.DateField()),
                ('date_of_installation', models.DateField()),
                ('bills', models.TextField()),
            ],
        ),
    ]
