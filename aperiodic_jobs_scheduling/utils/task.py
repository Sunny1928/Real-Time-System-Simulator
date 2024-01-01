class PeriodicTask:
	
    def __init__(self, name, id, period, excution_time):
        """ Initialize task """

        self.name = name
        self.id = id
        self.period = period
        self.excution_time = excution_time

    def __del__(self):
        """ Delete task """

    def print_task(self):
        """ Print task data """
        
        print(self.name, self.period, self.excution_time)