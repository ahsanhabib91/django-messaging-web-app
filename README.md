# Django Messaging Web App

This is a reusable Django project that can handle private messages between Users implemented with `Django Rest Framework` and `PostgreSQL`. The front-end of this project is implement with `Angular 4`, `Material UI` and `Bootstrap` which can be found in this [repository](https://github.com/ahsanhabib91/angular-messaging-web-app).

## Features

*  	User `Registration`.
*  	User `Login` and `Logout`.
*  	A User is allowed to have different Conversations with another User
*  	A User can `Archive` a Conversation.
*  	A User can `Delete` a Conversation.
*  	User can see `sorted Conversation list` where his last Conversation shows up with `timestamp`.
*  	User can see `message list` with `timestamp` related to a particular `Conversation` sorted by `timestamp`.
*	User can send `messages` and `photos` to another User and maintaina a seperate `Conversation thread`.

## Installation

*	`git clone https://github.com/ahsanhabib91/django-messaging-web-app.git`
*	`cd django-messaging-web-app`.
*	`virtualenv .`.
*	`source bin/activate`.
*	`pip install -r requirements.txt`.
*	`cd src`
*	Update the `django_messaging_service/setting.py file`. Put the front-end `Ip address` and `port number` in `CORS_ORIGIN_WHITELIST` and Update the `Database` information. Please use `Postfresql` as `Database`.
*	`python manage.py makemigrations`.
*	`python manage.py migrate`.
*	`python manage.py runserver`.