# HostelManagement

## Requirements :
* Python 3.8.5
* Django 2.2.12
* MySQL Client Library

## Installation:
Create a folder where you wish to save the project

**1)Install Python**
```
$pip install python
```

**2)Install Django**
```
$pip install django
```

**3)Install MySQL Client Library**
```
$install mysql-connector-python
```

**3)Clone the repository**
```
$git clone https://github.com/deeptadevkota/HostelManagement.git
```

**4)Enter the project**
```
$cd HostelManagement
```

**5)Setup Database in MySQL command line**
```
$create database hostel_management_system;
```
```
$create user 'hostel_management_system'@'localhost' identified by 'password';
```
```
$grant all privileges on *.* to 'hostel_management_system';
```

**6)Makemigrations to database**\
```
$python manage.py makemigrations
```
```
$python manage.py migrate
```

**7)Create a superuser**\
```
$python manage.py createsuperuser
```

**8)Run Server**\
```
$python manage.py runserver
```


