# Django Messaging Web App

This is a reusable Django project that can handle private messages between Users implemented with `Django Rest Framework` and `PostgreSQL`.

## Features

1. User `Registration`.
2. User `Login` and `Logout`.
3. A User is allowed to have different Conversations with another User
4. A User can `Archive` a Conversation.
4. A User can `Delete` a Conversation.
5. User can see `sorted Conversation list` where his last Conversation shows up with `timestamp`.
6. User can see `message list` with `timestamp` related to a particular `Conversation` sorted by `timestamp`.
7. User can send `messages` and `Photos` to another User and maintaina a `Conversation thread`.

## Installation

1. `git clone https://github.com/ahsanhabib91/django-messaging-web-app.git`
2. `cd django-messaging-web-app`.
3. `virtualenv .`.
4. `source bin/activate`.
5. `pip install -r requirements.txt`.
6. `cd src`
7. Update the `django_messaging_service/setting.py file`. Put the front-end Ip address and port number in `CORS_ORIGIN_WHITELIST` and Update the Database information. Please use `Postfresql` as `Database`.
8. `python manage.py makemigrations`.
9. `python manage.py migrate`.
10. `python manage.py runserver`.