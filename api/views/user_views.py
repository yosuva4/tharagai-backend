from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from twilio.rest import Client
import random
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


from api.serializers.user_Serializers import UserSeralizers,UserSeralizersWithToken,UserAddressSerialaizer
from api.model.user_model import UserAddress


class AllProfiles(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def get(self, request):
        return Response(UserSeralizers(User.objects.all(),many=True).data)
    
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,pk):
        try:
            return Response(UserSeralizers(User.objects.get(id=pk)).data)
        except Exception as e:
            return Response(status=404,data= {'error':"User not found"})
    
class GetUser(APIView):
    def get(self, request):
        try:
            user = request.user
            serializer = UserSeralizers(user, many=False)  
            return Response(serializer.data)
        except Exception as e:
            return Response(status=404, data={"error": "User not found"})
    
class UserRegistration(APIView):
    def post(self,request):
        data = request.data
        try:
            user = User.objects.create(
                username = data['username'],
                email = data['email'],
                password = make_password(data['password'])
            )
            serializer = UserSeralizersWithToken(user,many=False)
            return Response(serializer.data)
        
        except Exception as e:
            print("the error is : ",e)
            return Response(status=404,data={"error":"Did not registre"})
             
class AddressViews(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        try:
            user = request.user
            serailzer = UserAddressSerialaizer(UserAddress.objects.filter(user = user),many=True)
            return Response(status=200,data=serailzer.data)
        except Exception as e:
            return Response(status=400,data={"message" : "User not found"})
        
    
      

             
# def generate_otp():
#     otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
#     return otp


# class Send_otp(APIView):
#     def post(self,request):
        
#         try:
#             phone_number = request.data['phone_number']
            
#             if phone_number:
#                 user,created  = CustomUser.objects.get_or_create(phone_number=phone_number)
                                
#                 otp = generate_otp()
                    
#                 user.otp = otp
#                 user.save()
                
#                 # client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
#                 # client.messages.create(body=f'your otp is:{otp}',
#                 #                            from_=f"{settings.TWILIO_PHONE_NUMBER}",
#                 #                            to=f'{settings.COUNTRY_CODE}{phone_number}') 
#                 content = {
#                     'message':"OTP sent successfully.",
#                     "status" : True
#                 }
                
#                 return Response(content)
#             else:
#                 content = {
#                     'message':"Please enter valid Email ID/Mobile number",
#                     "status" : False
#                 }
                
#                 return Response(content)
            
        
#         except Exception as e:
#             print("the error is :",e)
#             content = {
#                 'error':"Please enter valid Email ID/Mobile number"
#             }
#             return Response(content,status=400)


# class Verify_otp(APIView):
    
#     def post(self,request):
#         print(request.user)
#         try:
#             phone_number = request.data['phone_number']
#             otp = request.data['otp']
            
#             if phone_number:
#                 if CustomUser.objects.filter(phone_number=phone_number).exists():
#                     if CustomUser.objects.filter(phone_number=phone_number,otp=otp).exists():  
                        
#                         user = CustomUser.objects.get(phone_number=phone_number)
#                         login(request,user)
#                         user1 = authenticate(request, phone_number=phone_number)
#                         print("the user is : ",user1)     
#                         content = {
#                             "user" : user,                            
#                             'message':"OTP verification successful."
#                         }
#                         return Response(content,status=200)
#                     else:
#                         content = {
#                             'error':"OTP does not match."
#                         }
#                         return Response(content,status=400)
#                 else:
#                     content = {
#                         'error':"Mobile Number does not exist."
#                     }
#                     return Response(content,status=400)
                    
#             else:
#                 content = {
#                     'error':"Mobile Number does not exist."
#                 }
#                 return Response(content,status=400)
                
        
#         except Exception as e:
#             print("The error is ",e)
#             content = {
#                 'error':str(e)
#             }
#             return Response(content,status=400)
        

