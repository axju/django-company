=======
Company
=======

Quick start
-----------

1. Add "company" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'company',
    ]

2. Include the company URLconf in your project urls.py like this::

    path('company/', include('company.urls')),

3. Run `python manage.py migrate` to create the company models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to configurat the company (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/company/ to participate in the company.