from django.db import models
from django.contrib.auth.models import User


ROLE_CHOICES = [
    ("Batsman", "Batsman"),
    ("Bowler", "Bowler"),
    ("All-Rounder", "All-Rounder"),
    ("Wicket Keeper", "Wicket Keeper"),
]
class Player(models.Model):

    name = models.CharField(max_length=100)

    country = models.CharField(max_length=50)

    role = models.CharField(
                max_length=50,
                choices=ROLE_CHOICES
            )

    batting_style = models.CharField(max_length=100)

    bowling_style = models.CharField(max_length=100)

    matches = models.PositiveIntegerField()

    runs = models.PositiveIntegerField()

    wickets = models.PositiveIntegerField()

    biography = models.TextField()

    image = models.ImageField(upload_to="players/")

    def __str__(self):
        return self.name
    
    featured = models.BooleanField(
        default=False
    )
    
    featured_order = models.PositiveIntegerField(default=0)
    
class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )

    class Meta:

        unique_together = ("user", "player")

    def __str__(self):

        return f"{self.user.username} - {self.player.name}"
    
class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name