# Generated by Django 2.2.7 on 2020-02-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part4',
            fields=[
                ('part4_id', models.AutoField(primary_key=True, serialize=False)),
                ('part4_heading', models.CharField(max_length=250)),
                ('part4_body', models.TextField()),
            ],
        ),
    ]