from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Stores a follower relationship between users.

    'owner' - the user following another user.
    'followed' - the user being followed.
    'unique_together' - ensures a user can't 'double follow' the same user.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
