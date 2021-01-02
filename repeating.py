import time, os, sys, sched

# POLLING_INTERVAL = 1

class Repeat(object):
    def __init__(self, wait, funcName):
        self.schedule = sched.scheduler(time.time, time.sleep)
        self._running = False
        self.wait = wait
        self.funcName = funcName
        self.interval = self.wait
        # self.interval = POLLING_INTERVAL

    def periodic(self, action, actionargs=()):
        if self._running:
            self.event = self.schedule.enter(self.interval, 1, self.periodic, (action, actionargs))
            action(*actionargs)

    def start(self):
        self._running = True
        self.periodic(self.funcName)
        self.schedule.run( )

    def stop(self):
        self._running = False
        if self.schedule and self.event:
            self.schedule.cancel(self.event)

#to use this function
#r = repeating.Repeat(1, function_name)
#r.start()
