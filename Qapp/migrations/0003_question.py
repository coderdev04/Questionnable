# Generated by Django 3.1 on 2020-08-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qapp', '0002_accounts_acc_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qtitle', models.CharField(max_length=100)),
                ('Qdesc', models.CharField(max_length=300)),
                ('Qdrive_link', models.CharField(max_length=300)),
            ],
        ),
    ]