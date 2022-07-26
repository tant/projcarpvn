# Generated by Django 4.0.6 on 2022-07-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_navlinks_activated_alter_navlinks_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navlink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50, verbose_name='text hiện ra trên menu')),
                ('link', models.CharField(max_length=100, verbose_name='link của menu')),
                ('activated', models.BooleanField(default=False, verbose_name='cho biết đang ở trang nào')),
            ],
        ),
        migrations.DeleteModel(
            name='Navlinks',
        ),
    ]
