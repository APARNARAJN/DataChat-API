from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QueryLog
from .serializers import QueryLogSerializer
import ollama

class QueryView(APIView):
    def post(self, request):
        user_question = request.data.get('question')
        
        if not user_question:
            return Response(
                {'error': 'No question provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Real LLM call
        response = ollama.chat(
            model='llama3.2',
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a helpful data analyst assistant. Answer questions about data clearly and concisely.'
                },
                {
                    'role': 'user',
                    'content': user_question
                }
            ]
        )
        
        llm_response = response['message']['content']
        
        log = QueryLog.objects.create(
            user_question=user_question,
            llm_response=llm_response
        )
        
        serializer = QueryLogSerializer(log)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HistoryView(APIView):
    def get(self, request):
        logs = QueryLog.objects.all().order_by('-created_at')
        serializer = QueryLogSerializer(logs, many=True)
        return Response(serializer.data)

class QueryDetailView(APIView):
    def delete(self, request, pk):
        try:
            log = QueryLog.objects.get(pk=pk)
            log.delete()
            return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except QueryLog.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)