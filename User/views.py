from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from .models import Users
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET", "POST"])
def user_create(request):
    if request.method == "POST":
        #the password should be strong and length mixed up chage such as "bangalore@01"
        serializer = UserSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            user=serializer.save()
            return Response({ "email": user.email}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"invalid data"}, status=status
                            .HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        data = request.data
        user = authenticate(request, email=data['email'], password=data['password'])
        user_data = {}
        if user is not None:
            login(request, user)
            user=Users.objects.get(email=data['email'])
            #user_data = Token.objects.filter(user=user).values()
            return Response("logged in successfully")
        else:
            user_data['message'] = "login failed"
            return Response(user_data, status=status.HTTP_401_UNAUTHORIZED)