# Generated by Django 4.1.3 on 2022-11-28 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0003_chihu_user_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"verbose_name": "评论表", "verbose_name_plural": "评论表"},
        ),
        migrations.AddField(
            model_name="comment",
            name="comment_content",
            field=models.TextField(default="", verbose_name="评论内容"),
        ),
        migrations.AddField(
            model_name="comment",
            name="like_count",
            field=models.IntegerField(default=0, verbose_name="点赞数量"),
        ),
        migrations.AddField(
            model_name="comment",
            name="publish_time",
            field=models.DateField(auto_now=True, verbose_name="发表时间"),
        ),
        migrations.AddField(
            model_name="comment",
            name="reply_count",
            field=models.IntegerField(default=0, verbose_name="回帖数量"),
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
            name="shop_score",
            field=models.IntegerField(default=0, verbose_name="评论给店铺的分数"),
        ),
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                default=None, on_delete=django.db.models.deletion.CASCADE, to="db.user"
            ),
        ),
        migrations.AlterModelTable(
            name="comment",
            table="Comments",
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
    ]