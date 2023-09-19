from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from utils import get_token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
User = get_user_model()


# from rest_framework import get_user

# Create your views here.
@api_view(['GET', 'POST'])
def calc_carbon(request):
    if request.method == 'POST':
        diesel = int(request.data['diesel'])
        hydrogen = int(request.data['hydrogen'])
        annual = int(request.data['annual'])
        carbonsavings = int((diesel - hydrogen) * annual)
        result = carbonsavings
        data = {"carbonsavings": result}

        return Response(data)




@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        # print(request.POST)
        fname =  request.data['first_name']
        lname = request.data['last_name']
        email = request.data['email']
        pass1 = request.data['password']
        pass2 = request.data['confirm_password']
        username = request.data['username']

    if User.objects.filter(email=email):
        return Response('email is already used', status=status.HTTP_400_BAD_REQUEST)
    
    if pass1 != pass2:
        return Response('Input a uniform password', status=status.HTTP_400_BAD_REQUEST)
    
    
    user = User.objects.create_user(first_name=fname, last_name=lname,email=email, password=pass1, username=username)

    if user:
        token = get_token(user)
        response_data = {
            "user":{
                "first_name":user.first_name,
                "last_name":user.last_name,
                "email": user.email
            },
            "token":token.key
        }
        return Response(response_data, status=status.HTTP_202_ACCEPTED )
    return Response('You have successfully registered')



@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
    user = authenticate(email = email, password = password)
    if user:
        response_data = {
            "user":{
                "first_name":user.first_name,
                "last_name":user.last_name,
                "email": user.email
            },
            "token":get_token(user).key

        }
        return Response(response_data, status=status.HTTP_202_ACCEPTED )
    return Response('not logged in', status=status.HTTP_401_UNAUTHORIZED)


def logout(request):
    if request.method == 'POST':
        user = User.objects.get()
        user.delete()
        logout(user)

    
    


    
    