# Generated by Django 5.0 on 2024-01-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on', 'author']},
        ),
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(default='empty'),
        ),
    ]
