# Generated by Django 4.1.2 on 2022-10-26 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamplanner', '0003_remove_user_is_active_remove_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=240, unique=True),
        ),
    ]
