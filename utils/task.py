class Task:
	
    def __init__(self, name, id, phase_time, period, relative_deadline, excution_time):
        """ Initialize task """
        self.name = name
        self.id = id
        self.phase_time = phase_time
        self.period = period
        self.relative_deadline = relative_deadline
        self.excution_time = excution_time

    def __del__(self):
        """ Delete task """
        # print('Delete Task')

    def print_task(self):
        """ Print task data """
        print(self.name, self.phase_time, self.period, self.relative_deadline, self.excution_time)