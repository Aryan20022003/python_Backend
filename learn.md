# how to start the static django server - startvirtualenv->hit active (make it executable before)

- django-admin startproject NameOfProject

# what is mange.py its a bridge b/w program and core module we ask manage.py to startapp , runserver

# when ever create an app include it in the setting.py so that masterFolder(same as project name) know about the project

    - Externalapp=["polls"]

# all the url/routes related stuff is in django.url ->(routes,include)

# to make an app standAlone (use the concept of route mounting)

    -polls
    ---routes
    -----urls.py(name of file should be this only)
            --- make urlpatterns=[path("url",callback funtion,name)](similar to me make in master folder's urls.py)

# makemigration poll will create a log file but doen't embrace it but migration will will embrace it

# python3 manage.py sqlmigrate nameofApp filename(eg.0001)

    - will show you sql query it will run if you embrace/migrate

# concept learned today

    - REST api in django how to make rest api
        -- important points are -> we need serializer to convert data into json and vice versa
        -- for checking provided data form client follows the conditions and constraints of module we use serializer
        -- when we make rest api we use django-rest-framework
        -- we need to make serializer.py file in app folder
        -- when we make call back or views in django for api handling we use api_view decorator
                eg @api_view(['GET','Post'])

            @api_view(['Get','Post'])
        -- def company_details(request):

            --- important point what ever the data being send via json from client side
            it will be in `request.data` and request.data is dict so suppose i want ot access
            authenticator so it will be like request.data['authenticator']

            -- and when we send response from the backend we use return Response(status="what ever the status ", data={"status":400,"data1":serializer.data})

            so what ever inside data will be send to client in form of json

        -- just see the rest app for rest and views.py of rest


# TOKEN AND JWT

    -- when we do request.data["data"] it will return the main segments where data is present
    ------- to eg acess word => request.data["data"]["word"]

    ---Fat model thin controller
        eg --- in model itself define functionality like set_password is defined in model of user itself so that when we do user.set_password("password") it will call the function define in model
        ----- similarly we define check password

    -- when we do model.userData.filter(username="username") it will return the instance of that data and we have password and other method of that instance that why define function in model itself and can be used there using self

    -- to encrypt password we use make_password("password") and to check password we use check_password("password") which are method of django hasher module

    --- for creating of jwt used external module pyjwt
