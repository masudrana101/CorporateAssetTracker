from django.shortcuts import render
from rest_framework import permissions, status, viewsets, filters
from rest_framework.response import Response
from .models import UserAccount as User
from .serializers import UserSerializer, LogSerializer, UserUpdateSerializer, PasswordUpdateSerializer, UserTokenSerializer
from django.db.models import Q
from utils.response_wrapper import ResponseWrapper
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserFilter

# Create your views here.
# Using filter() instead of get() where needed because get() will throw an exception if no object is found
class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filterset_class = UserFilter
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id', 'username', 'email', 'first_name', 'last_name')

    # this method needed custom permission classes for each action
    def get_permissions(self):
        if self.action == 'register':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'login':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'user_list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    # this method needed custom serializer classes for each action
    def get_serializer_class(self):

        if self.action == 'login':
            return LogSerializer

        elif self.action == 'update':
            return UserUpdateSerializer

        elif self.action == 'password_update':
            return PasswordUpdateSerializer

        elif self.action == 'register':
            return UserTokenSerializer

        else:
            return UserSerializer


    # this method is for all users list
    def user_list(self, request):
        try:
            qs = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(qs, many=True)
            return ResponseWrapper(
                data=serializer.data,
                message='User list',
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # this method is for user registration
    def register(self, request):
        try:
            email = request.data.get('email')
            phone = request.data.get('phone')
            password = request.data.get('password')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')

            if email:
                username = email
            elif phone:
                username = phone

            if User.objects.filter(email=email).exists():
                return ResponseWrapper(
                    message='User already exists with same email!',
                    error_code=status.HTTP_400_BAD_REQUEST
                )
            elif User.objects.filter(phone=phone).exists():
                return ResponseWrapper(
                    message='User already exists with same phone number!',
                    error_code=status.HTTP_400_BAD_REQUEST
                )
            else:
                user = User.objects.create_user(username=username, email=email, phone=phone, password=password, first_name=first_name, last_name=last_name)
                user.save()
                serializer = self.get_serializer(user)
                return ResponseWrapper(
                    data=serializer.data,
                    message='User created successfully!',
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # this method is for user login
    def login(self, request):
        try:
            phone_or_email = request.data.get('phone_or_email')
            password = request.data.get('password')

            if phone_or_email:
                user = User.objects.filter(Q(email=phone_or_email) | Q(phone=phone_or_email)).first()
                if user:
                    if user.check_password(password):
                        serializer = UserTokenSerializer(user)
                        return ResponseWrapper(
                            data=serializer.data,
                            status=status.HTTP_200_OK,
                            message='Login successful!'
                        )
                    else:
                        return ResponseWrapper(
                            message='Password is incorrect!',
                            error_code=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return ResponseWrapper(
                        message='User does not exists!',
                        error_code=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return ResponseWrapper(
                    message='Phone or email is required!',
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # this method is for user update
    def update(self, request, *args, **kwargs):
        try:
            user = User.objects.filter(id=request.user.id).first()
            serializer = self.get_serializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='User updated successfully!',
                    status=status.HTTP_200_OK
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # this method is for user user detail
    def user_detail(self, request, *args, **kwargs):
        try:
            user = User.objects.filter(id=request.user.id).first()
            if user:
                serializer = UserSerializer(user)
                return ResponseWrapper(
                    data=serializer.data,
                    message='User detail',
                    status=status.HTTP_200_OK
                )
            else:
                return ResponseWrapper(
                    message='User does not exists!',
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # this method is for user password update
    def password_update(self, request):
        try:
            user = User.objects.filter(id=request.user.id).first()
            old_password = request.data.get('old_password')
            new_password = request.data.get('new_password')
            if user:
                if user.check_password(old_password):
                    user.set_password(new_password)
                    user.save()
                    serializer = UserSerializer(user)
                    return ResponseWrapper(
                        data=serializer.data,
                        message='Password updated successfully!',
                        status=status.HTTP_200_OK
                    )
                else:
                    return ResponseWrapper(
                        message='Old password is incorrect!',
                        error_code=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return ResponseWrapper(
                    message='User does not exists!',
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )
            




        