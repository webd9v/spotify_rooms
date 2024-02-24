import random
import string
from django.contrib.auth.models import AbstractUser
from django.db import models

def get_unique_code(length: int=8, retry=10) -> str:
        while retry:
            code = "".join(random.choices(string.ascii_letters, k=length))
            if not Room.objects.filter(code=code).count():
                return code
            retry -= 1
        raise Exception("Can't find a unique code")

# Create your models here.
class User(AbstractUser):
    pass

class Room(models.Model):
    code = models.CharField(max_length=10, default=get_unique_code, unique=True, verbose_name="Room Code")
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Rooms", null=False, blank=False, verbose_name="Host")
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __repr__(self) -> str:
        return f"Room #{self.code}, Host: {self.host.username}"