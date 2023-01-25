from django.urls import path 
from rest_framework.routers import DefaultRouter as DR


from mayapp.views import(
    BookView,
    AuthorView,
    CategoryView,
    RegistrationView,
    AuthorizarionView,
)

router = DR()

router.register('book_categories',CategoryView,basename='book_category')
router.register('book',BookView,basename='book')
router.register('author',AuthorView,basename='author')



urlpatterns =[
    path('reg/',RegistrationView.as_view()),
    path('login/',AuthorizarionView.as_view()),
]

urlpatterns += router.urls
