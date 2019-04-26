import os, webbrowser, time, subprocess
subprocess.run('pipenv sync')
subprocess.Popen('pipenv run python manage.py runserver')
time.sleep(5)
webbrowser.open('http://127.0.0.1:8000', new=1, autoraise=True)
