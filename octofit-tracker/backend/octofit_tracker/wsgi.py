"""
WSGI config for octofit_tracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import django

from django.core.wsgi import get_wsgi_application

# Ensure Django is properly initialized
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
django.setup()

application = get_wsgi_application()
