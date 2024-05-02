# Signals raised after save and delete events
from django.db.models.signals import post_save, post_delete
# receiver needed to listen for and respond to signals
from django.dispatch import receiver

# Signals to be raised when changes made to Order line items, so need to import that too
from .models import OrderLineItem


# receiver decorator used to execute function anytime the post_save signal is sent
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total on lineitem update/create
        sender: sender of the signal (in this case - OrderLineItem)
        instance: instance of the model that sent it
        created: boolean informing whether this is a new instance or one being updated
        **kwargs: keyword arguments
    """
    # when signal raised, just call the update_total method we've written in models.py
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ Update order total on lineitem delete
    """
    print('delete signal received')
    instance.order.update_total()
