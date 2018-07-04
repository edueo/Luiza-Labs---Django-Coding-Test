# Employee Manager



## Requirements

- Python 3

- Pipenv



## Project stack

- Django 2

- SQLite 3

- Django REST Framework



## Setup local environment



1. Clone the project

2. Install dependencies. Execute in your root project directory

   ```sh
   pipenv install
   ```

3. Active the virtual environment

4. ```sh
   pipenv shell
   ```

   5. Run django development server 

```sh
cd vagaped && python manage.py runserver
```

  6. Open http://localhost:8000/ in your browser



## Employee manager Admin

1. Open http://localhost:8000/admin/ in your browser

2. Credentials

   ```sh
   Username: magalu
   Password: m4g4lu@2018
   ```



## Employee manager REST API



### List

```sh
curl localhost:8000/employee/
```

### Add

```sh
curl -XPOST -H "Content-Type: application/json" http://localhost:8000/employee/ -d'{"name": "Fulano","email": "fulano@email.com","department": {"title": "CS"}}'
```










