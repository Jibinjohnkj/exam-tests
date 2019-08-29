# exam-tests-example
A generic exam app using Django

Installation
------------
pip install pipenv

git clone https://github.com/Jibinjohnkj/examtests.git

cd exam-tests-example

pipenv install --ignore-pipfile

pipenv shell

python manage.py migrate

python manage.py runserver


Introduction
------------

The root URL('/') should take you to a login page.
If you are new student please register. If you are a teacher, please login with the given username and password.

After registering, if you are a student you should be able to take the test and see the results. 
If you are a teacher you can either create a test (via Django admin) or view the all the results.

