# Generated by Django 4.1.7 on 2023-05-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='./media/'),
        ),
    ]
