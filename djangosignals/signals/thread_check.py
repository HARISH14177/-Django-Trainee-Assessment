from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def thread_info_signal_handler(sender, instance, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal handler running in thread: {current_thread.name} (ID: {current_thread.ident})")

# In a view or elsewhere
def create_user_thread_test():
    current_thread = threading.current_thread()
    print(f"Creating user in thread: {current_thread.name} (ID: {current_thread.ident})")
    user = User.objects.create_user(username='threadtest', password='password123')
    return user