# Generated by Django 4.1.3 on 2022-11-29 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0005_alter_comment_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="publish_time",
            field=models.DateTimeField(auto_now=True, verbose_name="发表时间"),
        ),
    ]
