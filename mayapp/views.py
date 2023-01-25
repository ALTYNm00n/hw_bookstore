from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from mayapp.serializers import(
    BookCategorySerializer,
    AuthorSerializer,
    BookSerializer,
    RegistrationSerializer,
    AuthorizarionSerializer,
)
from mayapp.models import (BookCategory,Book,Author)


from mayapp.send_gmail import send_msg
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework import permissions
from rest_framework.decorators import action

class CategoryView(ModelViewSet):
    queryset= BookCategory.objects.all()
    serializer_class=BookCategorySerializer

    @action(methods=['post,'],detail=True,serializer_class=BookSerializer,permission_classes =(permissions.IsAuthenticatedOrReadOnly,))
    def add_book(self,request,*args,**kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user= request.user
        book=Book.objects.create(
            book=self.get_object(),
            name = serializer.validated_data.get
            ('name'),
            author=user,
            date_of_issue=serializer.validated_data.get('date_of_issue'),
            chapter_amount=serializer.validated_data.get('chapter_amount'),
            preview=serializer.validated_data.get('preview'),
            price=serializer.validated_data.get('price'),
            discount=serializer.validated_data.get('discount')
            
            
            )
        return Response(BookSerializer(book).data)


class BookView(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends=(
        DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,
    )
    filterset_fields=(
        'date_of_issue',
    )
    search_fields=(
        'name','id','book_category__name',
    )
    ordering_fields=(
        'price','id'
    )

class AuthorView(ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,
    )


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(username = username). exists():
            return Response({"message": 'User with such username is already  exists'})

        user = User.objects.create_user(
            username=username,
            email= email,
            password=password
        )

        send_msg(email=email, username=username)

        token = Token.objects.create(user=user)
        return Response({"token: token.key"})
    

class AuthorizarionView(APIView):
     def post(self, request):
        serializer =AuthorizarionSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = data.get('username')
        password = data.get('password')

        user  = User.objects.filter(username=username).first()

        if user is not None:
            if check_password(password, user.password):
                token, _ =Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            return Response ({"error": 'Password is not valid'}, status=400)
        return Response({'error':'this username is not resigtreted'}, status=400)









