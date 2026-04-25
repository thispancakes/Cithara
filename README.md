# Cithara
Exercise 1: https://docs.google.com/document/d/1aih2pXZoWlwIC8qZXn3BHMQrw_FYupJAbrDeyMKP-g0/edit?usp=sharing  
Exercise 2: https://docs.google.com/document/d/1i0DAdeH7V0wZpY8sN6MNFgOaq2n5ADCWox5FyQtKJVU/edit?usp=sharing  
## CRUD Funtionality
CRUD Functionaly is implemented using Django Admin.
![CREATE](https://github.com/thispancakes/Cithara/blob/main/images/Screenshot%202026-03-23%20190216.png)
![READ/DELETE](https://github.com/thispancakes/Cithara/blob/main/images/Screenshot%202026-03-23%20190325.png)
![UPDATE](https://github.com/thispancakes/Cithara/blob/main/images/Screenshot%202026-03-23%20190413.png)
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
Create a config.py file in the cithara directory from the example config_example.py (not the root directory)  
```
GENERATION_STRATEGY = 'mock' # 'mock' or 'suno'
SUNO_API_KEY = '' # Your Suno API key here
```
Where GENERATION_STRATEGY is either 'mock' or 'suno' depending on what strategy you want to use. SUNO_API_KEY is required if you are using the suno strategy.  
You can aquire an API key from going to https://sunoapi.org/api-key (You will need to make an account if you do not already have one) and then pressing the 'Copy' button.

### Step 2
Run the following:
```
py manage.py migrate
```
Create a Django admin user. Instructions can be found on the "Creating an admin user" Section here:   
https://docs.djangoproject.com/en/6.0/intro/tutorial02/#creating-an-admin-user.
## Running
Run the following:
```
py manage.py runserver
```

Then follow the link to http://127.0.0.1:8000/.

Additionally, go to http://127.0.0.1:8000/admin/ for access to the admin page (Login with the credentials you provided).

## Song Generation
Go to the admin page to create a user http://127.0.0.1:8000/admin/.  
  
![](https://github.com/thispancakes/Cithara/blob/main/images/Screenshot%202026-04-25%20225845.png)  
Then go to http://127.0.0.1:8000/ to the songs page, and click the generate song button and fill out the details (use the created users id, which should be 1). Using the suno strategy will cause the generation page to load for a little while.  
Mock output example:  
![](https://github.com/thispancakes/Cithara/blob/main/images/Screenshot%202026-04-25%20225731.png)  
  
finished Suno output example:  
![](https://github.com/thispancakes/Cithara/blob/main/images/Screenshot%202026-04-25%20225655.png)  
  
You can periodically see the suno song status in the terminal output:  
![](https://github.com/thispancakes/Cithara/blob/main/images/Screenshot%202026-04-25%20225815.png)  
![](https://github.com/thispancakes/Cithara/blob/main/images/Screenshot%202026-04-25%20232912.png)  
  
You could also check the Suno website to see if its working.
