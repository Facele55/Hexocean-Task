# HexOcean Recruitment Task

## How to run

* Python Virtual Environment. 
Check out the [for more information](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
  - Create a virtual environment:
    + `python -m venv venv` for Windows;
    + `python3 -m venv venv` for *nix(Ubuntu, Linux, macOS)
  - Activate it:
    + `venv\Scripts\activate` for Windows
    + `. venv/bin/activate` for *nix(Ubuntu, Linux, macOS)
  - Install requirements:
    + `pip install -r requirements.txt` Windows
    + `pip3 install -r requirements.txt` *nix(Ubuntu, Linux, macOS)
  - Run server:
    + `python manage.py runserver` for Windows
    + `python3 manage.py runserver` for *nix(Ubuntu, Linux, macOS)
  - Open in browser:
    + [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Docker
  - Navigate to project folder:
    + provide command: `docker-compose up`
  - Open in browser:
    + [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
### Task Finishing
Sadly, I was not able to accomplish all the requirements.

    - "generate expiring links" was not completed.


### Performance
As per my research, the Django Rest Framework is not the best option for APIs, but 
built-in classes and functions will take care of that.

### Tests
Testing is my weakness. I'm working on it. 
For this project, I made a few simple tests.
To run tests from the command line, you must first activate 
the virtual environment and enter a command.
`python manage.py test` for Windows or
`python3 manage.py test` for *nix systems (Linux, Ubuntu, macOS).

### The time it took you to perform the task
Generally speaking, to perform this task takes around 2 days.
Most of the time was used to find the best dynamic and flexible solution.
In my code, I'm following the principles of DRY and KISS.

