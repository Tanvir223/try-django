# Generated by Django 3.2.14 on 2022-08-05 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='nada'),
            preserve_default=False,
        ),
    ]
