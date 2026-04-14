"""
WSGI config for youtube project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube.settings')

application = get_wsgi_application()

# my Added


# Add your project directory to the sys.path
path = '/home/admin/E:/yut/youtube'  
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'youtube.settings'  # Replace 'your_project' with your actual project name

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()