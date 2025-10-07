# Q-1 By default are django signals executed synchronously or asynchronously?

Django Signals are Synchronous - means that the process runs in a single thread, block the main code untill the signal has been executed

```bash  
Signals.py 
@receiver(post_save, sender=Question)
def slow_signal(sender,instance,**kwargs):
    print("[Signal] Started slow signal...")
    time.sleep(5)  
    #A time delay for the signal
    print("[Signal] Finished slow signal!")

```
A signal only executed when A question is created 
if it was Asynchronous while that time sleep 

it should have printed 
``` bash 
    print("[View] Question created — returning response now!")
```
but instead it waited and executed it after that function was executed 