# How to install this thing anywhere #

* (install python - usually comes with pip out of the box, if not, install pip separately, you also may want to use virtualenv)
* (install and set up a local postgres database or connect to a remote database later - connecting to a remote is recommended if you're not using Linux, actually it doesn't even have to be postgres, just the app has been tested and known to work on postgres)
* (install git)
* git clone https://USERNAME@bitbucket.org/lauriy/webothlike.git PROJECT_FOLDER
* cd /PROJECT_FOLDER
* pip install -r requirements.txt
* change the DATABASES entry in PROJECT_FOLDER/WeBothLike/settings.py to match your database
* python manage.py migrate
* python manage.py runserver
* fix the errors or warnings Django gives you (like adding a social app at localhost:8000/admin)
* otherwise, everything should be up and running at localhost:8000 by default