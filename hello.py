import sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

def index(request):
    """Return a http response"""
    return HttpResponse('Hello World')

urlpatterns = (
    path('', index),
)

if __name__ == "__main__":
    """main function"""
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
