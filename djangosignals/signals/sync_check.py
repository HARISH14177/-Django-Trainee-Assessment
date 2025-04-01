from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler started for user: {instance.username}")
    time.sleep(5)  
    print(f"Signal handler completed for user: {instance.username}")

def create_user():
    print("About to create user")
    start_time = time.time()
    user = User.objects.create_user(username='testuser', password='password123')
    end_time = time.time()
    print(f"User creation completed in {end_time - start_time:.2f} seconds")
    return user