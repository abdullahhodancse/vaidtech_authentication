from rest_framework import serializers
from app1.models.custome_user import User

from app1.models.patient_models import patient

class RgisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    age = serializers.IntegerField(write_only=True)   # patient field
    disease = serializers.CharField(write_only=True, required=False)  # patient field

    class Meta:
        model = User
        fields = ['email', 'password', 'age', 'disease']  
    def create(self, validated_data):
        # User part
        age = validated_data.pop('age')
        disease = validated_data.pop('disease', "")
        user = User.objects.create_user(
           
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Patient part
        patient.objects.create(
            user=user,
            age=age,
            disease=disease
        )

        return user
