# learning-django
Various projects and apps used to learn the fantastic Django...

## official_tutorial
This directory contains the official tutorial source code starting from https://docs.djangoproject.com/en/4.2/intro/tutorial01/ based on Django version 4.2.
You can follow commits one by one to better identify each part of the tutorial.

Installation of Django
```bash
# Go to your favorite directory (here "official_tutorial", and
# create a Python virtual env (only the first time)
python3.11 -m venv venv # note you may use a different Python version
# Activate it
source venv/bin/activate
# Update pip and install the latest Django version
pip install --upgrade pip
python -m pip install Django
# Check the installed django version
python -m django --version

# Now your Python env is ready for playing with Django :-)
```

## my1stcms
This directory contains a test of the wagtail Django content management system (CMS).

The first commit simply follow the default installation instructions (read https://github.com/wagtail/wagtail for details):
```bash
pip install wagtail
wagtail start mysite
cd mysite
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
