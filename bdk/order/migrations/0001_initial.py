# Generated by Django 2.1.5 on 2019-01-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=128)),
                ('name2', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('PT', models.CharField(max_length=128)),
                ('ADR', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('number', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('shoes', models.CharField(max_length=128)),
                ('SD', models.CharField(max_length=128)),
                ('CK1', models.CharField(max_length=128)),
                ('CK2', models.CharField(max_length=128)),
            ],
        ),
    ]