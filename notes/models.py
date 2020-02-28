from django.db import models
from uuid import uuid4
# model that corresponds to user records
from django.contrib.auth.models import User
# Create your models here.


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4,
                          editable=False)  # uuid4 generates random id
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    # automatically adds itself when first added
    created_at = models.DateTimeField(auto_now_add=True)
    # adds itself when added or modified
    last_modified = models.DateTimeField(auto_now=True)


# Note that has information about the currently logged in user

class PersonalNote(Note):  # inherit from Note model
    # cascade - related records in other tables get deleted automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)
