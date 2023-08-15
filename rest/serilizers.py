# create serializer for model

from rest_framework import serializers
from .models import Company

from .models import userData


class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {
            "Company_id": {"read_only": True},
            "Company_name": {"required": True},
        }


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = "__all__"
        # extra_kwargs = {
        #     "userId": {"read_only": True, "required": True},
        #     "password": {"required": True},
        # }
