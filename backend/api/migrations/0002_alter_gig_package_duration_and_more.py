# Generated by Django 4.2.5 on 2023-09-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig_package',
            name='duration',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]