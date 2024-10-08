# Generated by Django 4.1.3 on 2024-08-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('love_story', '0002_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customuser_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customuser_user_permissions', to='auth.permission'),
        ),
    ]
