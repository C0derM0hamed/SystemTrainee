from rest_framework import serializers

from trainee.models import Trainee


class TraineeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, trim_whitespace=True)

    class Meta:
        model = Trainee
        fields = ["id", "name"]

    def validate_name(self, value):
        # Reject empty/whitespace-only names while keeping validation simple.
        cleaned = value.strip()
        if not cleaned:
            raise serializers.ValidationError("Name cannot be empty.")
        return cleaned
