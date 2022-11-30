# Generated by Django 4.1 on 2022-11-30 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chihu",
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
                ("user_id", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("comment_content", models.TextField(default="", verbose_name="评论内容")),
                ("publish_time", models.DateField(auto_now=True, verbose_name="发表时间")),
                ("reply_count", models.IntegerField(default=0, verbose_name="回帖数量")),
                ("like_count", models.IntegerField(default=0, verbose_name="点赞数量")),
                ("shop_score", models.IntegerField(default=0, verbose_name="评论给店铺的分数")),
            ],
            options={
                "verbose_name": "评论表",
                "verbose_name_plural": "评论表",
                "db_table": "db_comment",
            },
        ),
        migrations.CreateModel(
            name="Shop",
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
                ("shop_name", models.CharField(max_length=20, verbose_name="店铺名称")),
                (
                    "shop_profile_photo",
                    models.ImageField(null=True, upload_to="photos", verbose_name="图片"),
                ),
                ("shop_score", models.IntegerField(default=0, verbose_name="店铺评分")),
                ("comment_count", models.IntegerField(default=0, verbose_name="评论量")),
                (
                    "shop_isChiHu",
                    models.BooleanField(default=False, verbose_name="是否吃乎认证"),
                ),
                ("is_delete", models.BooleanField(default=False, verbose_name="逻辑删除")),
            ],
            options={
                "verbose_name": "店铺",
                "verbose_name_plural": "店铺",
                "db_table": "db_shop",
            },
        ),
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
                ("sid", models.IntegerField(default=0, null=True)),
                ("user_name", models.CharField(max_length=20)),
                ("password", models.IntegerField(default=0, null=True)),
                ("image", models.ImageField(null=True, upload_to="")),
                ("is_ch", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "用户",
                "verbose_name_plural": "用户",
                "db_table": "tb_user",
            },
        ),
        migrations.CreateModel(
            name="Photos",
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
                ("image", models.ImageField(upload_to="photos/", verbose_name="评论的图片")),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="db.comment"
                    ),
                ),
            ],
            options={
                "verbose_name": "图片表",
                "verbose_name_plural": "图片表",
                "db_table": "Photos",
            },
        ),
        migrations.CreateModel(
            name="Huitie",
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
                    "comment",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db.comment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db.user",
                    ),
                ),
            ],
            options={
                "verbose_name": "评论回帖",
                "verbose_name_plural": "评论回帖",
                "db_table": "tb_huitie",
            },
        ),
        migrations.AddField(
            model_name="comment",
            name="shop",
            field=models.ForeignKey(
                default=None, on_delete=django.db.models.deletion.CASCADE, to="db.shop"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                default=None, on_delete=django.db.models.deletion.CASCADE, to="db.user"
            ),
        ),
        migrations.CreateModel(
            name="Collect",
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
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "shop",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db.shop",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db.user",
                    ),
                ),
            ],
            options={
                "verbose_name": "收藏",
                "verbose_name_plural": "收藏",
                "db_table": "tb_collect",
            },
        ),
    ]
