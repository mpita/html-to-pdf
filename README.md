# HTML to PDF with Django 2.1 and Python 3.6.3

> The code was made of this post https://codeburst.io/django-render-html-to-pdf-41a2b9c41d16

## Step to run the example project

#### - Step 1
Create the virtual environment
```sh
$ python3 -m venv .env
$ source .env/bin/activate
```
#### - Step 2
Install the requirements packages
```sh
(.env) $ pip install -r requirements.txt
```
#### - Step 3
Migrate the models to the database
```sh
(.env) $ python manage.py makemigrations product
(.env) $ python manage.py migrate
```
#### - Step 4
We create a superuser
```sh
(.env) $ python manage.py createsuperuser
```
#### - Step 5
Now create two users, in the django admin with your first and last name as well as the superuser. for this we have to run the project first.
```sh
(.env) $ python manage.py runserver
```
go to http://localhost:8000/admin
#### - Step 6
Create products with the Seeder class from the seeds.py file of the product application
```sh
(.env) $ python manage.py shell
Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from product.seeds import Seeder
>>> Seeder().seed()
```
leave the shell with ctrl + D
#### - Step 7
```sh
(.env) $ python manage.py runserver
```
go to http://localhost:8000/render/pdf/
