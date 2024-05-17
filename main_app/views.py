from django.shortcuts import render


# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Country, Holidays, Rivers
from . serializers import CountrySerializer, HolidaysSerializer, RiversSerializer, UserSerializer
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

class LoginView(APIView):
    permission_classes= [permissions.AllowAny]

    def post(self, request):
      username= request.data.get('username')
      password= request.data.get('password')
      user = authenticate(username=username, password=password)
      if user: 
        refresh = RefreshToken.for_user(user)
        return Response ({
            
            'refresh': str(refresh),
            'access': str()
})
            
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the country-collector api home route!'}
    return Response(content)
class CountryList(generics.ListCreateAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer
  lookup_field = 'id'

class HolidaysListCreate (generics.ListCreateAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
      country_id = self.kwargs['country_id']
      return Holidays.objects.filter(country_id=country_id)
    
    def perform_create(self, serializer):
      coutry_id = self.kwargs['country_id']
      Country = Country.object.get(country=coutry_id)
      serializer.save(country=Country)

class HolidaysDetail (generics.RetrieveUpdateDestroyAPIView):
      serializer_class = HolidaysSerializer
      lookup_field = 'id'

      def get_queryset(self):
        country_id = self.kwargs['country_id']
        return Holidays.object.filters( country_id = country_id)
      

class RiversList (generics.ListCreateAPIView):
      queryset = Rivers.objects.all()
      serializer_class = RiversSerializer
      lookup_field = id

class RiversDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Rivers.objects.all()
  serializer_class = RiversSerializer
  lookup_field = 'id'

  # add (override) the retrieve method below
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    toys_not_associated = Rivers.objects.exclude(id__in=instance.toys.all())
    toys_serializer = RiversSerializer(toys_not_associated, many=True)

    return Response({
        'cat': serializer.data,
        'toys_not_associated': toys_serializer.data
    })
class AddToyRiver(APIView):
   def post(self, request, country, river_id):
      country = Country.object.get(id=country)
      river = Rivers.objects.get(id=river)
      country.rivers.add(Rivers)

      return Response({'message': f'Toy {river.name} added to Cat {river.name}'})


