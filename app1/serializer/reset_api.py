from rest_framework import serializers
from app1.models.custome_user import User


class PasswordResetRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()


    class Meta:
        model = User
        fields = ['email']

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError
        return value