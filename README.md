## Advanced Web Technologies

Installation steps:

- Install Python 3.x.y: https://www.python.org/downloads/ 
- Download PostgreSQL (user: postgres, password: 1234) and pgAdmin4. https://www.postgresql.org/download/  https://www.pgadmin.org/download/
- Create database with name 'movie_portal' in pgAdmin4.
- Create a virtual environment. https://docs.python.org/3/library/venv.html
- Install pip. https://pip.pypa.io/en/stable/
- Install Django: python -m pip install Django
- Install psycopg2: pip install psycopg2-binary
- The version of Django should be Django 3.2 or later, which supports Python 3.6 and later.
- Git clone project: git clone https://github.com/serxinho/Movie-Portal.git
- Inside the project:
  - Make the migrations: python manage.py makemigrations
  - Migrate: python manage.py migrate
  - Create a superuser: 
    - python manage.py createsuperuser
    - Username: admin
    - Email address: admin@example.com
    - Password: admin 
  - Run server: python manage.py runserver
- Open http://127.0.0.1:8000/admin/  in a web browser and create new movies (Images are inside the project in: /media/pics)
- Open http://127.0.0.1:8000/ and play.



Created by:
- Sergio Herrando Cuenca
- Bernat Puig Font
