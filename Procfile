web: gunicorn --name=playground --config gunicorn_config.py project.wsgi
release: python manage.py migrate
worker: python manage.py rqworker
rqscheduler: python manage.py rqscheduler