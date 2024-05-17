from django.urls import path
from .views import Home
from .views import Home, CountryList, CountryDetail, HolidaysListCreate, HolidayDetail, RiversList, RiversDetail, CreateUserView, LoginView, VerifyUserView, AddToyRiver

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('countries/', CountryList.as_view(), name='country-list'),
  path('countries/<int:id>/', CountryDetail.as_view(), name='country-detail'),
  path('countries/<int:country_id>/holidays/', HolidaysListCreate.as_view(),        name='holidays-list-create'),
  path('countries/<int:country_id>/holiday/<int:id>/', HolidayDetail.as_view(), name='holidays-detail'),
  path('rivers/', RiversList.as_view(), name='river-list'),
  path('rivers/<int:id>/', RiversDetail.as_view(), name='river-detail'),
  path('rivers/<int:river>/add_river/<int:river_id>/', AddToyRiver.as_view(), name='add-toy-to-cat'),
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path ('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
  

]
