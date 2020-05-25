import threading


class AsynManager:
    def __init__(self):
        self.planners = None
        self.executors = []
        self.semaphore = threading.Semaphore(len(self.executors))
        self.threads = []

    def call(self, function_name, *args, **kwargs):
        func = getattr(self.planners, function_name)
        self.threads.append(threading.Thread(func, *args, **kwargs))
        self.threads[-1].run()
        self.threads[-1].join()


class Planner:
    pass


class Executor:
    pass



