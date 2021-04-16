# Generated by Django 2.2 on 2021-04-13 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswers',
            name='paper_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Paper.Papers', verbose_name='Papers'),
        ),
        migrations.DeleteModel(
            name='Papers',
        ),
    ]
