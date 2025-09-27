from rest_framework import serializers
from app1.models.custome_user import User



class PasswordResetConfirmSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords Does not match")
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])  # Hashing
        instance.save()
        return instance