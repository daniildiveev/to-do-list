from django.db import models


class Task(models.Model):
    title = models.CharField("name", max_length=100, related_name="tasks")
    creator = models.CharField("creator", max_length=100)
    description = models.CharField("description", max_length=1000)
    status = models.CharField("status", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField("date due")

    def __str__(self):
        return f"""
            Title: {self.title},
            Creator: {self.creator},
            Status: {self.status}
        """
