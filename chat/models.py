from django.db import models

# Create your models here.
from django.db import models

class QueryLog(models.Model):
    user_question = models.TextField()
    llm_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query at {self.created_at}"