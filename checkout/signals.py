from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total on lineitem update/create
        sender: sender of the signal (in this case - OrderLineItem)
        instance: instance of the model that sent it
        created: boolean informing whether this is a new instance or one being updated
        **kwargs: keyword arguments
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """ Update order total on lineitem delete
    """
    instance.order.update_total()
