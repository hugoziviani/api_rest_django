# api_rest_django
simple api django with sqllite-3

To run this simple project you must to have installed python3 and jango with rest_framework

the address of the API are:
This is the home, where you can see the two others address witch can answere calls
http://127.0.0.1:8000/registry/

There are two routes avaliable to make request of [PULL, GET, PUT and DELETE]
This is for add companies, and register them
    http://127.0.0.1:8000/registry/company/

    OBS: the model of JSON that you must send is in this format
    JSON format:

    {
        "name": "Name example",
        "institutional_registry": "0001/11.19999example"
    }

This is other one is for add employees, and register them
    http://127.0.0.1:8000/registry/employee/

    OBS: you can add a object and asociate it on more than one companies, previously registred

    JSON format:
    {
        "first_name": "example_name",
        "last_name": "example_last_name",
        "email": "example_email",
        "username": "example_user_name",
        "work_for": [
            1,
            2,
            3,
            4
        ]
    }

    There are some verifications made by API to get better the insertions to database, email is unique,
    and the username is verified by a simple logic to allaw simple user names.