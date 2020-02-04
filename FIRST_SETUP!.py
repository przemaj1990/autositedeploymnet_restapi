

# 1, (venv) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ virtualenv -p python3 env
# 2. (venv) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ source env/bin/activate
# ^C(venv) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/autositedeployment$ source venv/bin/activate
# 3. (env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ pip install django
# 4. (env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ django-admin startproject networkportal .
# 5. (env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ python manage.py runserver
# 6. (env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ python manage.py makemigrations
# 7. (env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ python manage.py migrate
# 8. (env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ python manage.py startapp janmierczijoke
# 9.  adding 'janmierczijoke' to settings.py INSTALLED_APPS
# 10. database setup [optional]:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql', '<tu wstaw nazwę bazy danych>'
#         'NAME': 'python_module_5',                 '<tu wstaw nazwę sterownika>'
#         'USER': 'coders_user',                     '<tu wstaw nazwę użytkownika bazy danych>'
#         'PASSWORD': 'password',                    '<tu wstaw hasło bazy danych>'
#         'HOST': '127.0.0.1',                       '< tu wstaw adres hosta >'
#         'PORT': '5432',
#     }
# }
# 11.Model setup[according to project]
# 12.(env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ python manage.py createsuperuser
#       Username (leave blank to use 'pm1990'): pm1990
#       Email address: przemaj1990@gmail.com
#       Password: Mugin1234
#       Password (again):
#       Superuser created successfully.
# 13. Add static and templates directories in project files & setting changed:
#         STATICFILES_DIRS = ['static']
#         'DIRS': ['templates'],
# 14. ^C(env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ pip install --upgrade django-crispy-forms
# 15. (env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$   pip install django-markdown-deux
# 16. (env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/NetworkPortalDemo$ pip install django-pagedown
# 17. add admin.site.register(JanQuestions) to admin.py
# 18. Adding str&unicode to Model:
#                               def __str__(self):
#                                      return self.cebula
#                               def __unicode__(self):
#                                      return self.cebula
# 19. Mapping URLs to app [INCLUDE]: path('janmierczijoke/', include(('janmierczijoke.urls', 'janmierczijoke'), namespace='janmierczijoke')),
# 20. Admin view in url path('admin/', admin.site.urls),
# 21. Add to model:
#       def get_absolute_url(self):
#           (return "/model_name/{}/".format(self.id)_
#           return reverse("detail", kwargs={"id": self.id})
# 21a. Add namespace="post" to general urls
# 21b.      return reverse("post:detail", kwargs={"id": self.id})
#          - and in html there will be: {% url "post:detail" id=obj.id %}
# 22. Adding a filesdirectory to save files from project: /media/
# 22a. Add to settings.py:
#       'django.template.context_processors.media',
#       MEDIA_URL = '/media/'
#       MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "autositedeployment/media")
# 22b. add to main urls.py:
#       from django.conf import settings
#       from django.conf.urls.static import static
#       ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 23. Setup email setting in settings.py:
#        EMAIL_HOSTS = 'smtp.gmail.com'
#        EMAIL_HOSTS_USER = 'gcxbcb0@gmail.com'
#        EMAIL_PASSWORD = 'Pcxvbcxv'
#        EMAIL_PORT = 587
#        EMAIL_USE_TLS = True
#
#
# Advancing the Blog: 3
#       {obj.element|safe} - render code from object into html
#       - so if ther is <h1>coś<h1> it will not print but render it into html.
#
# 24 install crispy-form: pip install django-crispy-forms
# 24a add to settings.py: CRISPY_TEMPLATE_PACK = 'bootstrap3'
# Steps for Generic Foergin Keys:
# (venv) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/autositedeployment$ python manage.py startapp nocportal
# 25. Create in teplate directory registration
# 26. Create login & logout html
# 27. add LOGIN_REDIRECT_URL = '/lbe_portal' to settings.py - tp redirect after login to correct page.
# 27b. add LOGOUT_REDIRECT_URL = '/lbe_portal' to settping.py
# 28. When you would like to ue your own User app:
#           a. create app User
#           b. add for for creation new users
#           c. add view for register, logn, logout
# 29. if login requred on class/def in view, add also: LOGIN_URL = '/login/' in settings py - it will
#     redirect you to login view.
#

# DOCKER FIRST SETUP:
# cd path/to/your/dev/folder
# touch Dockerfile
# docker build -t hello-world -f Dockerfile .
# ls
# docker run -it hello-world
# docker images / docker ps -a
# docker stop <your-container-id> / docker rm <your-container-id>







# ls
# cd env
# virtualenv -p python3 env
# (source activate)
# source env/bin/activate
# pip install django
# django-admin version
# (env) pm1990@pm1990-Lenovo-Z51-70:~/env/bin$ django-admin startproject coderslab .


# pdb.set_trace() - UZYWAĆ !!!
# source env/bin/activate

# pm1990@pm1990-Lenovo-Z51-70:~$ sudo -i
# [sudo] hasło użytkownika pm1990:
# root@pm1990-Lenovo-Z51-70:~#
# root@pm1990-Lenovo-Z51-70:~# su - postgres
# postgres@pm1990-Lenovo-Z51-70:~$
# postgres@pm1990-Lenovo-Z51-70:~$ psql
# psql (9.5.19)
# Type "help" for help.
#
# postgres=#
# postgres=#
# postgres=# CREATE DATABASE python_module_5;
# CREATE DATABASE
# postgres=# ^C
# postgres=# CREATE ROLE coders_user WITH ENCRYPTED PASSWORD 'password' LOGIN;
# CREATE ROLE
# postgres=#
# postgres=# GRANT ALL PRIVILEGES ON DATABASE python_module_5 to coders_user;
# GRANT

# ^C(env) pm1990@pm1990-Lenovo-Z51-70:~/PycharmProjects/WAR_PYT_W_09_Zaawansowane_Django/3_Django/coderslab$ python manage.py createsuperuser
# Username (leave blank to use 'pm1990'): pm1990
# Email address: przemaj1990@gmail.com
# Password:
# Password (again):
# Superuser created successfully.




# psql -h hostname -U username -W -d databasename
#
# psql -h localhost -U postgres -W

# psql -h localhost -d football -U postgres -f football.sql   - import z sql do db.

# Migracja baz danch do Django:
# https://docs.djangoproject.com/en/1.11/howto/legacy-databases/
# https://docs.djangoproject.com/en/1.11/ref/django-admin/#inspectdb


# Podstawowe Komendy:
# pip install django
# django-admin version
# python -m django --version
# django-admin startproject / runserver / startapp / makemigrations / migrate
# django-admin startproject <nazwa-projektu> <ścieżka-do-projektu>   or django-admin startproject coderslab .
#
#
# python manage.py runserver or python manage.py runserver <numer-portu>
# python manage.py runserver <ip>:<port>
# python manage.py startapp <nazwa-aplikacji>  --> python manage.py startapp edu
#
# python manage.py migrate / makemigrations

# class Product(models.Model):
# name = models.CharField(max_length=64)
# content = models.TextField()
# score = models.SmallIntegerField()
# price = models.DecimalField(max_digits=5, decimal_places=2)
# wants_spam = models.BooleanField()
# available_from = models.DateTimeField()
# visits = models.IntegerField()
#
# (null=True/False)  & (default=0) & max_length=64
# LIGHTSABERS = (
#     (1, "Red"),
#     (2, "Blue"),
#     (3, "Green"),
#     (4, "Purple")
# )
# saber = models.IntegerField(choices=LIGHTSABERS)
#
# (db_index=True) - to pole będzie indexem bazy danych
# primary_key=True - klucz główny
# python manage.py shell



