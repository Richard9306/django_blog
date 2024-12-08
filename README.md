# django_blog
Small blog made with Django for educational purposes.

- [How to Set up](#how-to-set-up)






## How to Set up

Create specific folder (ex.django_blog):
```
mkdir django_blog
```
Navigate to django_blog folder by command:
```
cd django_blog
```
Clone repository:
```
git clone https://github.com/Richard9306/django_blog
```
You need to have installed Poetry package. If you don't have, please install using this command:
```
pip install poetry
```
Set poetry global option, to use project folder as place to hold virtual environment (recommended):
```
poetry config virtualenvs.in-project true
```
Install virtual environment, using current dependencies:
```
poetry install
```
Copy file env-template to .env file using command:
```
# linux/mac
cp env-template .env

# windows
copy env-template .env
```
Start poetry virtual environment
```
poetry shell
```

Update local .env file as needed

Create admin account to access admin site:

```
# linux/mac
# to apply db changes
./manage.py migrate 
./manage.py createsuperuser

# windows
# to apply db changes
python manage.py migrate
python manage.py createsuperuser
```


Run project:
```
# linux/mac
# to apply db changes
./manage.py migrate 
# to start project
./manage.py runserver

# windows
# to apply db changes
python manage.py migrate
# to start project
python manage.py runserver
```
