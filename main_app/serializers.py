from rest_framework import serializers
from .models import Country
from .models import Holidays
from .models import Rivers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, vaidated_data):
        user = User.objects.create_user(
            username=vaidated_data['username'],
            email=vaidated_data['email'],
            password=vaidated_data['password']
        )
        return user 

class RiversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rivers
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    celebrate_for_today = serializers.SerializerMethodField()
    Rivers = RiversSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)



    class Meta:
        model = Country
        fields = '__all__'

    def get_celebrate_for_today(self, obj):
        return obj.celebrate_for_today()

class HolidaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holidays
        fields = '__all__'
        read_only_fiels = ('country',)


