from .task import Task

class Job(Task):
	def __init__(self, task:Task, clock):
		""" Initialize job """
		super().__init__(task.name, task.id, task.phase_time, task.period, task.relative_deadline, task.excution_time)
		self.absolute_deadline = clock + task.relative_deadline
		self.slack =  self.absolute_deadline - task.excution_time

	def __del__(self):
		""" Delete job """
		# print('Delete Job')

	def print_job(self):
		""" Print job data """
		print(self.name, self.phase_time, self.period, self.relative_deadline, self.excution_time)