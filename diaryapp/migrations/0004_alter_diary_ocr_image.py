# Generated by Django 3.2.3 on 2021-05-28 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0003_alter_diary_ocr_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='ocr_image',
            field=models.ImageField(blank=True, null=True, upload_to='diary/%Y/%m/%d'),
        ),
    ]