from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from app1.serializer.confirm_reset_api import PasswordResetConfirmSerializer
from rest_framework.views import APIView
from app1.models.custome_user import User
from rest_framework.response import Response
from rest_framework import status

class PasswordResetConfirmAPIView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except:
            return Response({"error": "Invalid UID"}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({"error": "Invalid বা expired token"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PasswordResetConfirmSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password successfully reset."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
