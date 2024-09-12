# different from /djangoproj/urls.py

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path to get list of cars (requires you to create a root user with Django admin to populate cars table for your Django app)
    # if you try to go to /get_cars without initializing root user to populate the cars table, you will get an error stating "no such table"
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    
    # path for registration
    path(route='register', view=views.registration, name='register'),

    # path for login
    path(route='login', view=views.login_user, name='login'),

    # path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    # path for dealer reviews view
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),

    # path for add a review view
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
    path(route='add_review', view=views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
