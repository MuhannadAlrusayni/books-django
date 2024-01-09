# Pre-Requirement
You need the following to be able to run and test the application:
- [Poetry](https://python-poetry.org/): to manage dependencies
- Python 3.12

# Run The App
```sh
poetry env use python3.12 # this will create the .venv directory that will define our project environment. This is one time thing
poetry shell # this will let us activate the environment and opt-in
poetry install # this will install all the project dependencies we defined in `pyproject.toml` file
python manage.py migrate # this will create the database file and run the migration on it (this one time thing too, unless you have new migrations)
python manage.py runserver # this will run the app server, you can visit http://127.0.0.1:8000
```

# Run The test Suites
Assuming you have already created the environment directory and installed the project dependencies 
```sh
poetry shell # activate project environment
python manage.py test # this will run all tests in the project
```
