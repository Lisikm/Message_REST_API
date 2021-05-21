from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Message, User
from .serializers import MessageSerializer, MessageViewSerializer, RegistrationSerializer


class MessageView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageViewSerializer

    def get_object(self):
        obj = super().get_object()
        obj.display_count += 1
        obj.save()
        return obj


class MessageCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        instance.display_count = 0
        instance.save()
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class MessageDestroyView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class ObtainTokenView(views.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        send_mail(
            'Secret token',
            f'{token.key}',
            'imjustsendingemails@gmail.com',
            [user.email],
            fail_silently=False,
        )
        return Response({'token': 'Token has been send to your email.'})