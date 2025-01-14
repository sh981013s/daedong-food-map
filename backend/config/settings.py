"""# config settings"""
import logging
import os
from datetime import timedelta
from pathlib import Path

import dj_database_url
import django_heroku
from django.contrib.messages import constants as messages

SITE_ID = 1
# django basic settings
PROJECT_NAME = os.getenv("PROJECT_NAME")

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "TRUE"
USE_DOCKER = os.getenv("USE_DOCKER") == "TRUE"
USE_HEROKU = os.getenv("USE_HEROKU") == "TRUE"
PORT = os.getenv("PORT")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Deploy settings
DEPLOY_URL = os.getenv("DEPLOY_URL")
ALLOWED_HOSTS = ["*", "127.0.0.1", DEPLOY_URL]

# user model settings
AUTH_USER_MODEL = "users.User"

ROOT_URLCONF = "config.urls"

CUSTOM_APPS = [
    "users",
    "action_trackings",
    "inquiries",
    "places",
    "reports",
    "reviews",
    "file_managers",
    "bookmarks",
]

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "sass_processor",
    "extra_views",
    "django_unicorn",
    "django_extensions",
    "corsheaders",
    "silk",
    "nplusone.ext.django",
    # django-taggit
    "taggit",
    "taggit_serializer",
    # django-rest-framework
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "django_filters",
    # django-allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # documentation
    "drf_yasg",
] + CUSTOM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "silk.middleware.SilkyMiddleware",
    "nplusone.ext.django.NPlusOneMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = (
    {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_NAME"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": "db",
            "PORT": os.getenv("POSTGRES_PORT"),
        }
    }
    if USE_DOCKER
    else {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
)

if USE_HEROKU:
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES["default"].update(db_from_env)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = []

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_HOST_USER = EMAIL_ADDRESS
MAIL_USERNAME = EMAIL_ADDRESS
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SERVER_EMAIL = EMAIL_ADDRESS
DEFAULT_FORM_MAIL = os.getenv("DEFAULT_FORM_MAIL")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# sass settings

SASS_PROCESSOR_ENABLED = True
SASS_OUTPUT_STYLE = "compact"
SASS_PRECISION = 8
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, "assets")


# 메세지 프레임워크 클래스 설정

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# debug tool settings
INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# SQL explorer
INSTALLED_APPS += ["explorer"]
EXPLORER_CONNECTIONS = {"Default": "default"}
EXPLORER_DEFAULT_CONNECTION = "default"

EXPLORER_SQL_BLACKLIST = (
    "ALTER",
    "CREATE TABLE",
    "DELETE",
    "DROP",
    "GRANT",
    "INSERT INTO",
    "OWNER TO" "RENAME ",
    "REPLACE",
    "SCHEMA",
    "TRUNCATE",
    "UPDATE",
)

EXPLORER_DEFAULT_ROWS = 1000

EXPLORER_SCHEMA_EXCLUDE_TABLE_PREFIXES = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
)

EXPLORER_SCHEMA_INCLUDE_VIEWS = True

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://daedong-food-map.netlify.app",
]
CORS_ALLOW_CREDENTIALS = True

# N+1 Query auto detector
NPLUSONE_LOGGER = logging.getLogger("nplusone")
NPLUSONE_LOG_LEVEL = logging.WARN

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "nplusone": {
            "handlers": ["console"],
            "level": "WARN",
        },
    },
}

# REST_FRAMEWORK settings
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "config.pagination.StandardResultsSetPagination",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',
}


ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "none"
REST_USE_JWT = True
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=14),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=31),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}

django_heroku.settings(locals())
