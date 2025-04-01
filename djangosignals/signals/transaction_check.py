from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def transaction_signal_handler(sender, instance, **kwargs):
    # Create another model that would fail if the transaction was already committed
    try:
        # Try to create a user with the same username, which would violate uniqueness
        User.objects.create_user(username=instance.username, password='password123')
        print("Created duplicate user - this shouldn't happen!")
    except Exception as e:
        print(f"Expected error in signal handler: {e}")
        # If we're in the same transaction, this will roll back the original user creation too
        raise

# In a view or elsewhere
def test_transaction():
    try:
        with transaction.atomic():
            print("Starting atomic transaction")
            user = User.objects.create_user(username='transactiontest', password='password123')
            print("User created, signal handler will now run")
            # If the signal handler raises an exception inside this transaction,
            # this whole transaction gets rolled back
    except Exception as e:
        print(f"Transaction rolled back: {e}")
        
    # Check if user was created
    user_exists = User.objects.filter(username='transactiontest').exists()
    print(f"User exists after transaction: {user_exists}")