# Generated by Django 3.2.15 on 2022-09-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfdfdf', upload_to='galler'),
            preserve_default=False,
        ),
    ]
