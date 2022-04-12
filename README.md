# Introduction
TODO app built with Django

![todoimage](https://github.com/nazikashyrova/todo-project/blob/master/todo.jpg?raw=true "Title")

### Main features
You will need django to be installed in you computer to run this app.
Head over to https://www.djangoproject.com/download/ for the download guide
Once you have downloaded django, go to the cloned repo directory and run the following command
      
### virtualenv
ulanyan pacageleri bir yerde goymak ucun venv doretmeli doretman hem işledip bilyas...

# install virtual environment

$  unix/macOS:  python3 -m venv env

$  windows : py -m venv env


# Activate virtual environment

unix/macOS:$  source env/bin/activate

windows : $ .\env\Scripts\activate


If you want to switch projects or otherwise leave your virtual environment, simply run:
 
 deactivate
 
# Installing packages
Now that you’re in your virtual environment you can install packages. Let’s install the Requests library from the Python Package Index (PyPI):


Unix/macOS: python3 -m pip install -r requirements.txt

Windows: py -m pip install -r requirements.txt  
  
Then simply apply the migrations:
    $ python manage.py makemigrations

    $ python manage.py migrate
    
We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user

$ python manage.py createsuperuser

We just need to start the server now and then we can start using our TODO App. Start the server by following command

$ python manage.py runserver
Once the server is hosted, head over to http://127.0.0.1:8000 for the App.
