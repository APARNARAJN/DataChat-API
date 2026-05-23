from rest_framework import serializers
from .models import QueryLog

class QueryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryLog
        fields = ['id', 'user_question', 'llm_response', 'created_at']
        read_only_fields = ['llm_response', 'created_at']