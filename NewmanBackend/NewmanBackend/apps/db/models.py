from django.db import models


class User(models.Model):
    sid = models.IntegerField(default=0, null=True)  # 学号
    user_name = models.CharField(max_length=20)  # 用户名
    password = models.IntegerField(default=0, null=True)  # 密码
    image = models.ImageField(null=True)  # 头像
    is_ch = models.BooleanField(default=False)  # 是否为吃乎作者

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sid


class Shop(models.Model):
    shop_name = models.CharField(max_length=20, verbose_name='店铺名称')
    # upload_to 指定的路径待定
    shop_profile_photo = models.ImageField(upload_to='photos', verbose_name='图片', null=True)
    shop_score = models.IntegerField(default=0, verbose_name='店铺评分')
    comment_count = models.IntegerField(default=0, verbose_name='评论量')
    shop_isChiHu = models.BooleanField(default=False, verbose_name='是否吃乎认证')
    # 注销该店铺
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        # 指定表名
        db_table = 'db_shop'
        verbose_name = '店铺'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.shop_name


class Comment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE,default=None)  # 关联的
    shop = models.ForeignKey("Shop", on_delete=models.CASCADE,default=None)  # 关联的店铺id
    comment_content = models.TextField(default="", verbose_name="评论内容")
    publish_time = models.DateField(auto_now=True, verbose_name="发表时间")
    reply_count = models.IntegerField(default=0,verbose_name="回帖数量")
    like_count = models.IntegerField(default=0,verbose_name="点赞数量")
    shop_score = models.IntegerField(default=0,verbose_name="评论给店铺的分数")

    class Meta:
        db_table = "db_comment"
        verbose_name = "评论表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Photos(models.Model):
    """用于存放评论图片表"""
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos/", verbose_name="评论的图片")

    class Meta:
        db_table = "Photos"
        verbose_name = "图片表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Huitie(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True, default=None)  # 外键 用户 id
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, default=None)  # 外键 评论 id
    content = models.TextField  # 回帖内容
    date = models.DateTimeField  # 发表时间

    class Meta:
        db_table = 'tb_huitie'
        verbose_name = '评论回帖'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Collect(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True, default=None)  # 外键 用户 id
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True, blank=True, default=None)  # 外键 店铺 id
    time = models.DateTimeField(auto_now_add=True)  # 收藏时间

    class Meta:
        db_table = 'tb_collect'
        verbose_name = '收藏'
        verbose_name_plural = verbose_name


class Chihu(models.Model):
    user_id = models.IntegerField(default=0)  # 吃乎用户账号