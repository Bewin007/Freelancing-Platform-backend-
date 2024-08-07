from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from .serializers import *
from .models import User
from .filters import UserFilter

class Hello(APIView):
    def get(self, request):
        return Response("Hello")

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class User_Create(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized_users = [UsersSerializer(user).data for user in users]
        return Response(serialized_users)
    
    def post(self, request):
        serializer = Users_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = User_Bank_Update_Serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        

class Bank_Detail_api(APIView):
    def get(self,request):
        data = Bank_Details.objects.all()
        serializer = Bank_Details_Serializer(data)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Bank_Details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ExpertListView(generics.ListAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer

class Expert_api(APIView):
    def get(self, request):
        users = Expert.objects.all()
        serialized_users = [ExpertSerializer(user).data for user in users]
        return Response(serialized_users)
    
    def post(self, request):
        serializer = Expert_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, user_id):
        try:
            user = Expert.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class Catogery_api(APIView):
    def get(self,request):
        data = Category.objects.all()
        serializer = CategorySerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Gig_api(APIView):
    def get(self,request):
        data = Gig.objects.all()
        serializer = GigSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Gig_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Review_api(APIView):
    def get(self,request):
        data = Review.objects.all()
        serializer = ReviewSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Review_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FAQ_api(APIView):
    def get(self,request):
        data = FAQ.objects.all()
        serializer = FAQSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FAQ_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Replay_api(APIView):
    def get(self,request):
        data = Replay.objects.all()
        serializer = ReplaySerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Replay_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Gig_package_api(APIView):
    def get(self,request):
        data = Gig_package.objects.all()
        serializer = Gig_packageSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Gig_package_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Order_api(APIView):
    def get(self,request):
        data = Order.objects.all()
        serializer = OrderSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Order_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Expert_Catogery_api(APIView):
    def get(self,request):
        data = Expert_Catogery.objects.all()
        serializer = Expert_CatogerySerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Expert_Catogery_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Wishlist_api(APIView):
    def get(self,request):
        data = Wishlist.objects.all()
        serializer = WishlistSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Wishlist_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Call_Details_api(APIView):
    def get(self,request):
        data = Call_Details.objects.all()
        serializer = Call_DetailsSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Call_Details_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Notification_api(APIView):
    def get(self,request):
        data = Notification.objects.all()
        serializer = NotificationSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Notification_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class User_id_search(APIView):
    def get(self, request, pk):
        users = User.objects.filter(id = pk)
        serialized_users = [UsersSerializer(user).data for user in users]
        return Response(serialized_users)
    
class User_email_search(APIView):
    def get(self, request, pk):
        users = User.objects.filter(email = pk)
        serialized_users = [UsersSerializer(user).data for user in users]
        return Response(serialized_users)
    

class User_paging(APIView):
    def get(self, request):
        page = int(request.GET.get('page', 1))
        page_size = 10
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        queryset = User.objects.all()[start_index:end_index]
        serializer = UsersSerializer(queryset, many=True)
        data = User.objects.count()
        next_page = False
        if (data/page_size >= page):
            next_page = True
        response_data = {
            'count': data,  # Total number of items
            'page': page,  # Current page number
            'page_size': page_size,  # Items per page
            'results': serializer.data,  # Serialized data
            'next_page': next_page
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
    def post(self, request):
        page = int(request.data.get('page'))
        page_size = int(request.data.get('page_size'))
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        queryset = User.objects.all()[start_index:end_index]
        serializer = UsersSerializer(queryset, many=True)
        next_page = False
        data = User.objects.count()
        if (data/page_size >= page):
            next_page = True
        response_data = {
            'count': data,  # Total number of items
            'page': page,  # Current page number
            'page_size': page_size,  # Items per page
            'results': serializer.data,  # Serialized data
            'next_page': next_page
        }

        return Response(response_data, status=status.HTTP_200_OK)