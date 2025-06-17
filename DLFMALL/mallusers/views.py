from rest_framework .views import APIView
from django.http import JsonResponse
from .Seriallizers import *
from .models import *

class userSignup(APIView):
    def post(self,request):
        serializerData=userDetailsSeriallizer(data=request.data)
        if serializerData.is_valid():
            userDetails.objects.create(**serializerData.data)
            message={"message": "User Signup Successfully"}
            return JsonResponse(message)
        return JsonResponse(serializerData.errors)
    
class usermembership(APIView):
        def get(self,request,email):
            result=list(membershipDetails.objects.filter(email=email).values())
            message = {"Membership Details":result}
            return JsonResponse(message)
