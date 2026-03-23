# Cithara
## CRUD Funtionality
CRUD Functionaly is implemented using Django Admin. Views are currently not fully complete.
## Installation
### Prerequisites
Have Python 3.12 or later installed: https://www.python.org/downloads/.  
Have Django 6.0.3 installed: https://www.djangoproject.com/download/.
### Step 1  
Navigate to your desired directory to put the project in on your command line interface. Then clone the repository and navigate into the folder.  
```
git clone https://github.com/thispancakes/Cithara.git
```
```
cd cithara
```
### Step 2
Run the following:
```
py manage.py migrate
```
Create a Django admin user. Instructions can be found on the "Creating an admin user" Section here:   
https://docs.djangoproject.com/en/6.0/intro/tutorial02/#creating-an-admin-user.
### Step 3
(This is the only step you need to repeat if you have done the installation before.)  

Run the following:
```
py manage.py runserver
```

Then follow the link to http://127.0.0.1:8000/.

Additionally, go to http://127.0.0.1:8000/admin/ for access to the admin page (Login with the credentials you provided).
