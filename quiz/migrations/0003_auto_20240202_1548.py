# Generated by Django 3.0.4 on 2024-02-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20240201_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='question_images/'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
