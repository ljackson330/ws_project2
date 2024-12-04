Required:
``pip install django django-allauth django-allauth[socialaccount]``
``python manage.py migrate``

Go to the Google Cloud console and get the ``client_id`` and ``secret`` from your OAuth application and put them in ws_project2/settings.py in the ``SOCIALACCOUNT_PROVIDERS=`` block
Put the correct authorized origin and redirect URLs in now too.

``python manage.py runserver``

Log in to the web app with your Google account. This will create a user record in the user database. 

Create local admin account
``python manage.py createsuperuser``

Go to https://foo.com/admin in a private browser window and log in with that admin account. Grant your SSO account the staff privilege (it's a tick box on the user page)

Now you can create and edit project information.

