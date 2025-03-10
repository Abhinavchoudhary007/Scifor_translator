from django.db import models

class TranslationHistory(models.Model):
    original_text = models.TextField()
    translated_text = models.TextField()
    language = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_text} -> {self.translated_text} ({self.language})"