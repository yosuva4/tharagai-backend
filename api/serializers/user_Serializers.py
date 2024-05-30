from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from api.model.user_model import UserAddress


class UserSeralizers(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','isAdmin']
        
    def get_isAdmin(self,obj):
        return obj.is_staff
    
    
class UserSeralizersWithToken(UserSeralizers):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','isAdmin','token'] 
        
    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token)
    
    
class UserAddressSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'