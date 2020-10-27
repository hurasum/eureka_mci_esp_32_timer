"""
Thread typing class
"""


class Thread:
    """"""
    def start_new_thread(self, th_name, th_func, args , kwargs):
        """
        Start a new thread and return its identifier.
        The returned thread ID is used with most methods to access the created thread.
        Argument 	Description
        th_name 	string, used to describe the thread
        th_func 	MicroPython object of type function (defined with def) or bound_method (defined as class method).
        This is the main thread function which usualy runs in infinite loop. See the thread function template for more details.
        args 	the thread positional arguments given as tuple of objects.
        If the thread function requires no arguments, an empty tuple must be given - ()
        kwargs 	optional; if used, must be given as dictionary of keyword arguments

        npth =_thread.start_new_thread("Neopixel", thrainbow, ())
        bmeth =_thread.start_new_thread("BME280", bmerun, (60,))
        testth = _thread.start_new_thread("Test", thread_entry, (10, 20), {'a2': 0, 'a3': 1})


        """
        pass

    def stack_size(self, size):
        """
        If executed without arguments returns the thread stack size (in bytes) used when creating new threads.
        The optional size argument specifies the stack size to be used for subsequently created threads.

        The maximum stack size used by the thread can be checked with _thread.list()

        """
        pass

    def stack_size(self):
        """
        testth = _thread.start_new_thread("Test",thread_entry, (10, 20), {'a2': 0, 'a3': 1})
        """
        pass

    def allowsuspend(self):
        """
        The default behavior of the thread after it is created is to not allow to be suspended.
        This method can be used to explicitly allow the thread suspension.
        The method must be called from the thread function.
        """
        pass

    def suspend(self, th_id):
        """
        Suspend the execution of the thread th_id function on FreeRTOS level.
        """
        pass

    def resume(self, th_id):
        """
        Resume the execution of the thread th_id function previously suspended with _thread.suspend() on FreeRTOS level.
        """
        pass

    def stop(self, th_id):
        """
        Terminate the thread th_id, free all allocated memory.

            The thread function must handle _thread.EXIT notification
            See the thread function template.


        """
        pass

    def getThreadName(self, th_id):
        """
        Get the name of the thread with ID th_id.

        """
        pass

    def getSelfName(self):
        """
        Get the name of the thread executing this method.
        The method must be called from the thread function.

        """
        pass

    def getReplID(self):
        """
        Get the thread ID of the main (REPL) thread.
        Can be used to send notifications/messages to the main thread.
        """
        pass

    def getMainID(self):
        """
        Same as _thread.getReplID()

        """
        pass

    def wait(self, timeout):
        """
        Suspend the execution of the thread function until some notification is received or timeout expires.
        If the optional argument timeout is not given, the function will wait indefinitely.
        Returns integer >0 (the notification value) if the notification was received while waiting or 0 on timeout.
        The method must be called from the thread function.

        """
        pass

    def getnotification(self):
        """
        Check if any notification was sent to the thread executing this method.
        Returns integer >0 (the notification value) if there was pending notification or 0 if not.
        The method must be called from the thread function.

        """
        pass

    def getmsg(self):
        """
        Check if any message was sent to the thread executing this method.
        Returns 3-items tuple: (message_type, sender_ID, message)
        message_type = 0 -> message = None
        message_type = 1 -> message type is integer
        message_type = 2 -> message type is string

        The method must be called from the thread function.

        """
        pass

    def notify(self, th_id, value):
        """
        Send notification to the thread with id th_id.
        Value range: 0 < value < 65536 .
        Constants _thread.PAUSE, _thread.SUSPEND, _thread.RESUME, _thread.STOP, _thread.EXIT can be used for system notifications.

        """
        pass

    def sendmsg(self, th_id, msg):
        """
        Send message to the thread with id th_id.

        msg argument can be integer or string.

        """
        pass

    def lock(self):
        """
        Lock the thread execution to the calling thread.
        Must always be executed in combination with _thread.unlock().

        During the execution of code between _thread.lock() and _thread.unlock(), all other threads will not execute.
        That way, the maximum performance can be achieved for some limited time.
        Running the code between _thread.lock() and _thread.unlock() can also be used when accessing some shared resources, e.g. the global variables.

        """
        pass

    def unlock(self):
        """
        UnLock the thread after _thread.lock() and allow other threads to execute.
        """
        pass

    def lock(self):
        """
        Lock the thread execution to the calling thread.
        Must always be executed in combination with _thread.unlock().

        During the execution of code between _thread.lock() and _thread.unlock(), all other threads will not execute.
        That way, the maximum performance can be achieved for some limited time.
        Running the code between _thread.lock() and _thread.unlock() can also be used when accessing some shared resources, e.g. the global variables.
        """
        pass

    def unlock(self):
        """
        UnLock the thread after _thread.lock() and allow other threads to execute.
        _thread.lock() and _thread.unlock() must always be used in pairs.
        """
        pass

    def replAcceptMsg(self, flag):
        """
        Returns True if the main thread (REPL) is allowed to accept messages.
        If executed from the main thread, optional flag argument (True | False) can be given to allow/dissallow accepting messages in the main thread.

        """
        pass

    def status(self, th_id):
        """
        Returns the thread status code:
        Running: _thread.RUNNING (0)
        Suspended: _thread.SUSPENDED (1)
        Waiting: _thread.WAITING (2)
        Terminated: _thread.TERMINATED (-1)

        """
        pass

    def list(self, print):
        """
        Print the status of all created threads.
        If the optional print argument is set to False, returns the tuple with created threads information:
        (th_id, type, name, state, stack_size, max_stack_used)

        # >>> _thread.list()
        ID=1073586276, Name: THRD#2, State: waiting, Stack=4096, MaxUsed=948, Type: PYTHON
        ID=1073581228, Name: THRD#1, State: waiting, Stack=4096, MaxUsed=956, Type: PYTHON
        ID=1073447944, Name: MainThread, State: running, Stack=20480, MaxUsed=2616, Type: MAIN
        # >>> _thread.list(False)
        ((1073586276, 2, 'THRD#2', 2, 4096, 948), (1073581228, 2, 'THRD#1', 2, 4096, 956), (1073447944, 1, 'MainThread', 0, 20480, 2616))
        # >>>



        Constants
        For use in thread notification functions:

        """
        pass
