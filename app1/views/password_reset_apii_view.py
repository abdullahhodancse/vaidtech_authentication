from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app1.models.custome_user import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse
from app1.serializer.reset_api import PasswordResetRequestSerializer

class PasswordResetRequestAPIView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_url = request.build_absolute_uri(
                reverse('password_reset_confirm_api', kwargs={'uidb64': uid, 'token': token})
            )

            
            send_mail(
                subject="Password Reset",
                message=f"Click the link to reset your password: {reset_url}",
                from_email="your_email@example.com",
                recipient_list=[user.email],
                fail_silently=False,
            )

            return Response({"message": "Password reset email pathano hoise."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
