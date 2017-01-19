--Python Web Application for Handling Appointments--

>>Framework : Django
>>Database: Sql Lite
>>Backend: Python

Other Technologies Used:
>>JSON
>>SQL Lite
>>HTML
>>Bootstrap

******************************************
Requirements: 
******************************************

(1) The Appointment will be put under the sql lite database with no less than single table. One of the table contains 3 columns atleast.

(2) Used python scripting as a backend which observe the requests from the client server.

(3) The Frontend is a single web page which displays a "NEW" button, an empty text field with a "SEARCH" button and the bottom of the page will be an (intially empty) area for displaying the appointments in a table.

(4) If user enters the value in the text box and press the SEARCH button, the appointments area is cleared and getAppointments() is called with text value  from the search box. If the search text box is empty when the SEARCH button is click 
then all of the appoitments will appear. It refreshes the table DOM dynamically instead of refreshing the page which loaded already.

(5) User enters the data into the form and hits the "ADD" button, the filled form is submitted into the backend server. Hitting the form with values might reloads the web page entirely.

******************************************
Technical Steps: 
******************************************

* Install Django default Python 3.5 version is installed or install Python3.5 version

* After installing Django create a Repository and  name it as appointments:
    $ django-admin startproject appointments
    $ python manage.py runserver
    $ python manage.py runserver 8000
* In appointments/urls.py
   create views.py in appointment folder
* $ python manage.py migrate
* Create models.py in appointment folder
   from django.db import models
   class user_appointments(models.Model):
   date = models.DateField(null=True)
   description = models.CharField(max_length=200, null=True)
   time = models.CharField(max_length=10, null=True)
* Activate models by changing the INSTALLED_APPS in appointments/settings.py 
* $ python manage.py makemigrations appointment
* $ python manage.py migrate
* $ python manage.py runserver
 

-----
End of document


