"""
Django settings for coding_platform project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
import environ

# Initialize environ
env = environ.Env(
    # Set defaults for missing environment variables
    DEBUG=(bool, False)
)
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
GOOGLE_OAUTH2_CLIENT_ID = env('GOOGLE_OAUTH2_CLIENT_ID', default='')
GOOGLE_OAUTH2_CLIENT_SECRET = env('GOOGLE_OAUTH2_CLIENT_SECRET', default='')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-%1l2^d$2q8xuwtmv-z=_!&529loppvl)ikcs0&ef=safzcn=uw"

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
    "coding",
    "corsheaders",  # Add this line
    "staff",  # Add your app here
    'rest_framework',
    'django_extensions',
    'student',
    'mcq_platform',
]
CSRF_COOKIE_SECURE = False

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Add this line
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "backend.wsgi.application"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Add the origin of your frontend application
    "http://localhost:3001", 
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "assessment-portal-psi.vercel.app",
    "assessment-portal-git-main-kavin0047s-projects.vercel.app",
    "assessment-portal-o9e1gzej3-kavin0047s-projects.vercel.app",

# Add the origin of your frontend application
]   
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",  # Frontend origin
    "http://localhost:3001",
    "http://localhost:5173",  # Frontend origin
    "http://localhost:3001",
    "http://localhost:5173",  # Frontend origin
    "http://localhost:5174",
    'http://127.0.0.1:8000',
    'https://portal-8dvq2n0fs-krishneshwarans-projects.vercel.app/',
    'https://portal-sigma-lac.vercel.app/',
    "assessment-portal-psi.vercel.app",
    "assessment-portal-git-main-kavin0047s-projects.vercel.app",
    "assessment-portal-o9e1gzej3-kavin0047s-projects.vercel.app",
]

DATABASES = {
    
}
ALLOWED_HOSTS = ['*']


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # If using token-based auth
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'http://localhost:8000', 'https://portal-sigma-lac.vercel.app/', "http://localhost:5173", "http://localhost:5174"]
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'http://localhost:8000', 'https://portal-sigma-lac.vercel.app/', "http://localhost:5173", "http://localhost:5174"]
CORS_ALLOW_CREDENTIALS = True



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # For Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'testportalsns@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'xsqt gxtk prdj ptsx'  # Your email password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Default from email address
MONGODB_URI='mongodb+srv://krish:krish@assessment.ar5zh.mongodb.net/'
