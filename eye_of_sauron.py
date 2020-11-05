from observable import Observable


class EyeOfSauron(Observable):
    def __init__(self):
        Observable.__init__(self)

    def setEnemies(self, *args, **kwargs):
        if super().observable_last_state != args:
            self.notify_observers(args, kwargs)
            Observable.observable_last_state = args

