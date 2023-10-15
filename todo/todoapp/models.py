from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.




# default_user = User.objects.get(username='nidhish')


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    task_description = RichTextField()
    task_status = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)



    def __str__(self):
        return self.title



class Priority(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    PRIORITY_CHOICES = (
        (5, "⭐"),
        (4, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (2, "⭐⭐⭐⭐"),
        (1, "⭐⭐⭐⭐⭐"),
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        null=True,
        blank=False,
    )

    def __str__(self):
        return str(self.priority)

