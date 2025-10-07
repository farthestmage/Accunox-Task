# Topic Django Signals
## Q-1 By default are django signals executed synchronously or asynchronously?

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
## Do django signals run in the same thread as the caller?
As they run Synchronously we can tell even by calling the signals we se it runs in a single thread by checking the thread_id
This is also a great proof for  does django signals run synchronously 


## Do django signals run in the same database transaction as the caller?
A signal is executed when sender sends a signal to recievers that the a function has been performed and if that function is performed it needs to be executed so with that signal is executed.
So in this case we when the database transaction is executed it gives a signal that that data is being added to the table so executes the signal
for eg: we see the instance id of the question which is being created to show as a proof that it's running in the same database- Transaction.
```bash
print(f"[Signal] Fired for Question_id:{instance.id}")

```
we raise an exception to rollback the trigger 