# Contact book

In this directory, we will build a contact book GUI application with `Python, SQLite, and PyQt`.

## Project architecture

- The root directory is contact_book. It’ll contain the following files:
    - `requirements.txt` provides the project’s requirements list.
    - `README.md` provides general information about the project.
    - `runapp.py` provides the entry-point script to run the application.
- `contact/` is a subdirectory that provides the application’s main package. It provides the following modules:
    - `__init__.py`: it tells that `contact` is a package. When you import the package, this code will run. You don’t need to put any code in an __init__.py file to initialize the package. An empty __init__.py file will do the job. However, in this case, you define a module-level constant called __version__ to hold the version number of your application.
    - `views.py` : application main Window
    - `database.py`
    - `main.py`
    - `model.py`

