from rest_framework.serializers import ModelSerializer
from .models import Users

class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'password')

    def create(self, validated_data):
        print("running")
        user = Users(
            email=validated_data["email"],
            password=validated_data["password"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user