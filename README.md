# django-todo-backend

This project is to showcase how to build a simple rest api backend server using django framework

## Step to init the project
1. Make sure that you have [python](https://www.python.org/downloads/) installed on your machine
2. Install [django](https://docs.djangoproject.com/en/4.0/topics/install/#installing-official-release) and [django-rest-framework](https://www.django-rest-framework.org/#installation) on your machine
```bash
pip install django django-rest-framework
```
3. Init the django project
```bash
django-admin startproject todo_backend
```
4. Put `rest_framework` in `INSTALLED_APPS` array inside `settings.py` file
5. Make sure that you have [pgsql](https://www.postgresql.org/download/) installed on your machine and you can access it on your terminal
6. Install psycopg2
```bash
pip install psycopg2
```
or
```bash
pip install psycopg2-binary
```
7. Change database configuration in your `settings.py` file
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo_app', 
        'USER': 'postgres', 
        'PASSWORD': 'yourpasswords',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```
8. Migrate the database
```bash
py manage.py makemigrations
py manage.py migrate
```
9. Now you're all set, you can run your app
```bash
py manage.py runserver
```
or create a feature first
```bash
py manage.py startapp myapp
```
