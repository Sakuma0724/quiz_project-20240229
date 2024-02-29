# Generated by Django 5.0.1 on 2024-02-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20240202_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_image',
        ),
        migrations.AddField(
            model_name='choice',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]