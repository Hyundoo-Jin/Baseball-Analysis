import os, sys

from django.core.wsgi import get_wsgi_application

#sys.path.append('/home/jin-lab/anaconda3/envs/chatbot/lib/python3.6/site-packages/django')
#sys.path.append('/home/jin-lab/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot.settings")

application = get_wsgi_application()
