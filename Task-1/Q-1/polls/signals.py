import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
from .models import Question


@receiver(post_save, sender=Question)
def slow_signal(sender,instance,**kwargs):
    print(f"[Signal] Started slow signal... thread_id: {threading.get_ident()}")
    print(f"[Signal] Fired for Question_id:{instance.id}")
    time.sleep(5)  
    #A time delay for the signal
    print("[Signal] Finished slow signal!")

