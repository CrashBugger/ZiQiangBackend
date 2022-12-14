"""
Django settings for NewmanBackend project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from django.core.cache.backends.redis import RedisCache

"""
settings in developing environment
开发阶段即未上线时项目文件
"""
from ..apps import *
from pathlib import Path
import os, sys

# print(sys.path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Highway,追加导包路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6t8tdr4$g_xgzshs3i+%=x-hodg-f&*uab0py117#*%og6utk2"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'rest_framework',  # DRF
    # 'test_lhw.apps.TestLhwConfig',
    # 'test_lhw.apps.TestLhwConfig',
    'shop.apps.ShopConfig',
    'square.apps.SquareConfig',
    "user.apps.UserConfig",
    "collect.apps.CollectConfig",
    "db.apps.DbConfig",
    "signin.apps.SigninConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "NewmanBackend.urls"
# 存放数据库图片的文件夹
MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'media').replace('\\', '/')  # 设置静态文件路径为主目录下的media文件夹
MEDIA_URL = '/media/'
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(Path(__file__).resolve().parent.parent.parent, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "NewmanBackend.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': '192.168.23.129',  # 数据库主机,要修改成自己的
#         'PORT': 3306,  # 数据库端口
#         'USER': 'root',  # 数据库用户名
#         'PASSWORD': '66666666',  # 数据库用户密码
#         'NAME': 'ZiQiangBack'  # 数据库名字
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': '192.168.159.131',  # 数据库主机,要修改成自己的
#         'PORT': 3306,  # 数据库端口
#         'USER': 'zqnewman',  # 数据库用户名
#         'PASSWORD': '123456',  # 数据库用户密码
#         'NAME': 'ZqNewmanDb_3'  # 数据库名字
#     }
# }
# 远程数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '47.96.30.120',  # 数据库主机,要修改成自己的
        'PORT': 3306,  # 数据库端口
        'USER': 'godfood_user',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库用户密码
        'NAME': 'goodfood_1'  # 数据库名字
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 以下为redis相关配置
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:3306/0",  # 换成自己的
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:3306/1",  # 换成自己的
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"
# 以上为redis相关配置

# 以下为日志输出配置，还没配置好
# 参考：https://www.bilibili.com/video/BV1ya411A7C8/?p=12&spm_id_from=pageDriver&vd_source=763af5f146c65b47f793e885944c3b1b
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
#     'formatters': {  # 日志信息显示的格式
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
#         },
#     },
#     'filters': {  # 对日志进行过滤
#         'require_debug_true': {  # django在debug模式下才输出日志
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {  # 日志处理方法
#         'console': {  # 向终端中输出日志
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {  # 向文件中输出日志
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/mylog.log"),  # 日志文件的位置
#             'maxBytes': 300 * 1024 * 1024,
#             'backupCount': 10,
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {  # 日志器
#         'django': {  # 定义了一个名为django的日志器
#             'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
#             'propagate': True,  # 是否继续传递日志信息
#             'level': 'INFO',  # 日志器接收的最低日志级别
#         },
#     }
# }
# 以上为日志输出配置
