from rest_framework import serializers
from.models import Vibe
class VibeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Vibe
        fields='__all__'