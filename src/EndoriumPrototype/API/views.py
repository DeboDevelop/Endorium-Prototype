from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse("Index of the API")

class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminMapAPIView(APIView):

    def get(self, request):
        admin_map = AdminMap.objects.all()
        serializer = AdminMapSerializer(admin_map, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminMapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminMapDetail(APIView):

    def get_object(self, pk):
        try:
            return AdminMap.objects.get(pk=pk)
        except AdminMap.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        admin_map = self.get_object(pk)
        serializer = AdminMapSerializer(admin_map)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        admin_map = self.get_object(pk)
        serializer = AdminMapSerializer(admin_map, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        admin_map = self.get_object(pk)
        admin_map.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MessageAPIView(APIView):

    def get(self, request):
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageDetail(APIView):

    def get_object(self, pk):
        try:
            return Message.objects.get(pk=pk)
        except Message.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        message = self.get_object(pk)
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        message = self.get_object(pk)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        message = self.get_object(pk)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpvoteAPIView(APIView):

    def get(self, request):
        upvotes = Upvote.objects.all()
        serializer = UpvoteSerializer(upvotes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UpvoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpvoteDetail(APIView):

    def get_object(self, pk):
        try:
            return Upvote.objects.get(pk=pk)
        except Upvote.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        upvotes = self.get_object(pk)
        serializer = UpvoteSerializer(upvotes)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        upvotes = self.get_object(pk)
        serializer = UpvoteSerializer(upvotes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        upvotes = self.get_object(pk)
        upvotes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)