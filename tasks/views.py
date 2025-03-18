from django.contrib.auth.models import User
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task
from .serializers import UserSerializer,TaskSerializer
from .permission import IsOwner
from django.utils.dateparse import parse_date
from .pagination import Pagination
from rest_framework.exceptions import ValidationError

class RegUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]  # Authenticated users only
    pagination_class=Pagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign task to the current user

    def get_queryset(self):
        
        user = self.request.user
        queryset = Task.objects.all() if user.is_staff else Task.objects.filter(user=user)

        # Query Parameters
        completed = self.request.query_params.get('completed')
        created_after = self.request.query_params.get('created_after')
        created_before = self.request.query_params.get('created_before')
        updated_after = self.request.query_params.get('updated_after')

        # Handle invalid 'completed' filter
        if completed is not None:
            if completed.lower() not in ["true", "false"]:
                raise ValidationError({"completed": "Invalid value. Use 'true' or 'false'."})
            queryset = queryset.filter(completed=completed.lower() == "true")

        # Handle invalid date formats
        try:
            if created_after:
                created_after_date = parse_date(created_after)
                if created_after_date is None:
                    raise ValueError
                queryset = queryset.filter(created_at__date__gte=created_after_date)

            if created_before:
                created_before_date = parse_date(created_before)
                if created_before_date is None:
                    raise ValueError
                queryset = queryset.filter(created_at__date__lte=created_before_date)

            if updated_after:
                updated_after_date = parse_date(updated_after)
                if updated_after_date is None:
                    raise ValueError
                queryset = queryset.filter(updated_at__date__gte=updated_after_date)
        
        except ValueError:
            raise ValidationError({"date": "Invalid date format. Use 'YYYY-MM-DD'."})

        return queryset


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner] # Authenticated user can use this class
    