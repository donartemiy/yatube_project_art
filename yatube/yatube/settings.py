"""
Django settings for yatube project.

Generated by 'django-admin startproject' using Django 2.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x1lv!gfxe&4js%sv0lvcvnn%no2@36naj-@9-l23l!b2ms-ccg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Указываем откуда погружать статические файлы
# static - имя каталога в головной территории проекта
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# Переопределяем стандартные значения
# На этот адрес перенаправит пользователей для авторизации
# на страницу users:var_login. Полезно при @login_required
LOGIN_URL = 'users:var_login'
# Перенаправление после успешной авторизации
LOGIN_REDIRECT_URL = 'posts:index'


# Подключаем модуль отправки писем с движком filebased.EmailBackend
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# Дирректория для писем
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    # Встроенное приложение для регистрации
    # и авторизации пользователей
    'django.contrib.auth',
    'users.apps.UsersConfig',    # Регистрируем приложение users
    'core',
    'about'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yatube.urls'


TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# За настройки шаблонов HTMP в Django отвечает переменная TEMPLATES
TEMPLATES = [
    {
        # BACKEND - тут указывается язык шаблонов
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],    # Здесь django будет искать шаблоны
        'APP_DIRS': True,   # Нужно ли искать шаблоны на уровне приложений
        'OPTIONS': {
            # Перед обработкой шаблона, вызываются функции из списка
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Добавляем контекст-процессор,функция get_year лежит
                # в файле 'core / context_processors / year.'
                # Теперь можно прямо в DTL обращаться к get_year
                'core.context_processors.year.get_year',
            ],
        },
    },
]

WSGI_APPLICATION = 'yatube.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # файл с базой будет создан в головной директории проекта
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
