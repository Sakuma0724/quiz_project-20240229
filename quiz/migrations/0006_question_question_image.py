# Generated by Django 5.0.1 on 2024-02-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_choice_explanation_question_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='question_images/'),
        ),
    ]
