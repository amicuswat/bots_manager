# Generated by Django 4.1.3 on 2022-11-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_bots', '0005_bot'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Название группы')),
                ('telegram_id', models.IntegerField(verbose_name='ID группы в Телеграм')),
                ('is_notification_list', models.BooleanField(default=False, verbose_name='Получает уведомление')),
            ],
        ),
    ]
