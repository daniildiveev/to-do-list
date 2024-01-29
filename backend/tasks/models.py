from django.db import models


class Status(models.Model):
    name = models.CharField("name", max_length=15)
    color = models.CharField("color", max_length=10)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField("name", max_length=100)
    creator = models.CharField("creator", max_length=100)
    description = models.CharField("description", max_length=1000)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField("date due")

    def __str__(self):
        return f"""
            Title: {self.title},
            Creator: {self.creator},
            Status: {self.status}
        """
