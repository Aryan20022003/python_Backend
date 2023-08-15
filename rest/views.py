import jwt
from . import serilizers
from . import models
from . import tokenManager
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET", "POST"])
def company_list(request):
    if request.method == "POST":
        print(request.data)
        serializer = serilizers.companySerializer(data=request.data["data"])
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data={"status": 201, "data": serializer.data},
            )
            # create object
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
                data={"status": 400, "data": []},
            )
    elif request.method == "GET":
        companyData = models.Company.objects.all()
        serializer = serilizers.companySerializer(
            companyData, context={"request": request}, many=True
        )
        return Response(data={"status": 200, "data": serializer.data})


@api_view(["POST"])
def signup(request):
    serializer = serilizers.userSerializer(data=request.data["data"])

    if serializer.is_valid():
        userId = serializer.validated_data["userId"]
        if not models.userData.objects.filter(userId=userId).exists():
            serializer.save()
            user = models.userData.objects.get(userId=serializer.data["userId"])
            user.set_password(serializer.data["password"])##set_password is define in model
            # user.save()
            responseData = serializer.data
            responseData["password"] = "password is hidden"
            token = tokenManager.tokenIssuer(serializer.data["userId"])
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "status": 201,
                    "data": responseData,
                    "token": token,
                },  # does not what to send password
            )
        else:
            print("already exists")
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"status": 409, "data": []}
            )
    else:
        print("not valid data")
        return Response(
            status=status.HTTP_400_BAD_REQUEST, data={"status": 400, "data": []}
        )
    # create object


@api_view(["POST"])
def Login(request):
    try:
        user = models.userData.objects.get(userId=request.data["data"]["userId"])
        if user.check_password(request.data["data"]["password"]):##check_password is define in model
            token = tokenManager.tokenIssuer(request.data["data"]["password"])
            return Response(
                status=status.HTTP_200_OK,
                data={"status": 200, "data": [], "token": token},
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"status": 400, "data": []}
            )
    except models.userData.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND, data={"status": 404, "data": []}
        )


@api_view(["GET"])
def sessionTester(request):
    try:
        token: str = request.headers["Authorization"].split(" ")[1]
        if tokenManager.tokenVerifier(token):
            return Response(
                status=status.HTTP_200_OK,
                data={"status": 200, "data": [], "token": token},
            )
        else:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={"status": 401, "data": [], "message": "token is not valid"},
            )
    except:
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                "status": 400,
                "data": [],
                "message": "Authentication header not in correct format or missing",
            },
        )
