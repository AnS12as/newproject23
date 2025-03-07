from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    preview = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview = models.URLField(blank=True, null=True)
    video_url = models.URLField()

    def __str__(self):
        return self.title


