from .task import PeriodicTask

class Job():
	def __init__(self, name, excution_time):
		""" Initialize job """
		
		self.name = name
		self.excution_time =  excution_time

	def __del__(self):
		""" Delete job """



class PeriodicJob(PeriodicTask, Job):
	def __init__(self, clock, task:PeriodicTask):
		""" Initialize job """

		super().__init__(task.name, task.id, task.period, task.excution_time)
		self.arrive_time = clock
		self.absolute_deadline = self.period + clock

	def __del__(self):
		""" Delete job """

	def print_job(self):
		""" Print job data """

		print("name ", self.name)
		print("arrive_time ", self.arrive_time)
		print("period ", self.period)
		print("excution_time ", self.excution_time)
		print("absolute_deadline ", self.absolute_deadline)
		print()



class AperiodicJob(Job):
	def __init__(self, name, arrive_time, excution_time):
		""" Initialize job """

		super().__init__(name, excution_time)
		self.arrive_time = arrive_time

	def __del__(self):
		""" Delete job """

	def print_job(self):
		""" Print job data """

		print("name ", self.name)
		print("arrive_time ", self.arrive_time)
		print("excution_time ", self.excution_time)
		print()
