# Generated by Django 3.2.5 on 2021-08-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20210809_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='detail_address',
            field=models.TextField(blank=True, null=True, verbose_name='상세 주소'),
        ),
    ]