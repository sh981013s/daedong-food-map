# Generated by Django 3.2.5 on 2021-08-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action_trackings', '0002_auto_20210803_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionpointrule',
            name='name',
            field=models.CharField(choices=[('회원가입', 'signup'), ('제보 등록', 'add_report'), ('제보 삭제', 'delete_report'), ('승인된 제보', 'selected_repport')], default='제보 등록', max_length=20, verbose_name='행동'),
        ),
    ]
