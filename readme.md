# NG Books

## A mini book inventory for all your books

## To get started

1) Clone the repository and create a virtualenv for yourself using 
```
mkvirtualenv <name of virtualenv here>
```

2) Install the requirements
```
pip install -r requirements.txt
```

3) Create your database and update the settings found in settings.py under `DATABASES` configuration

4) Run migrations to sync the models with your db using
```
python manage.py migrate
```

5) Create a super user for yourself. This would allow you log into django admin `localhost:8000/admin/`
```
python mange.py createsuperuser
```

6) Start your server (default to port 8000)
```
python mange.py runserver
``

7) Navigate to the admin site and update your db with information `localhost:8000/admin/`

8) Test the app by searching for the information you just updated your db with

9) Run unit tests with 
```
python manage.py test
```
or if you prefer to see the coverage, run
```
coverage run manage.py test
coverage report
```