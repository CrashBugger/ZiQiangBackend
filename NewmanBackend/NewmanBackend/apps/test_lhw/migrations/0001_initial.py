# Generated by Django 4.1 on 2022-11-23 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mobile",
                    models.CharField(max_length=11, unique=True, verbose_name="手机号"),
                ),
            ],
            options={
                "verbose_name": "用户",
                "verbose_name_plural": "用户",
                "db_table": "tb_users",
            },
        ),
    ]
