from django.db import models

class Student(models.Model):
    app_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    marks = models.IntegerField()

    def __str__(self):
        return self.name