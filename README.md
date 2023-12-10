# LAB: Class 26

## Project: Intro to Django

## Author: Jacob Bassett

## Resources:

[Assignment](https://canvas.instructure.com/courses/7689176/assignments/40391850)

[Flowbite](https://flowbite.com/docs/getting-started/django/)


## Installation

Run the following in the terminal while in project's root directory. For macOS.

```bash
git clone "...url"
cd django-snacks
python3.? -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open browser and proceed to "http://127.0.0.1:8000/home" or "http://127.0.0.1:8000/about".

## Requirements.txt
asgiref==3.7.2

Django==5.0

django-appconf==1.0.6

django-compressor==4.4

rcssmin==1.1.1

rjsmin==1.2.1

sqlparse==0.4.4

## Tests

Run the following in the terminal while in project's root directory and the virtual environment is active. For macOS.

```bash
python manage.py test

# expected
Found 10 test(s).
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.012s

OK
```