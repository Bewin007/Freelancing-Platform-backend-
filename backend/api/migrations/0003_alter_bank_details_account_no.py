# Generated by Django 4.2.5 on 2023-09-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_bank_details_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_details',
            name='account_no',
            field=models.IntegerField(),
        ),
    ]