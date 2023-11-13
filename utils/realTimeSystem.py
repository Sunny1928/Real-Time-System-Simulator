import math
import copy
from utils.task import Task
from utils.job import Job
from utils.readyQueue import ReadyQueue

class RealTimeSystem:

	def __init__(self, file, schedule_type):
		""""""
		self.file = file
		self.task_arr  = self.read_file()
		self.schedule_type = schedule_type
		self.ready_queue = ReadyQueue()
		self.text = ""
		# Print all tasks 
		# task:Task
		# for task in self.all_tasks:
		# 	task.print_task()

	def read_file(self):
		""" Read file and store all tasks """
		with open(f'data/test/test{self.file}.txt') as f:
			lines = f.read().splitlines()
			f.close()

		all_tasks = []
		for idx, line in enumerate(lines):
			numbers = [ int(x) for x in line.split(', ',4) ]
			new_task = Task(f"T{idx+1}", idx, *numbers)
			all_tasks.append(new_task)

		return all_tasks
	
	def write_file(self):
		""" Write file  """
		with open(f"data/ans/{self.schedule_type}/test{self.file}.txt", "w") as f:
			f.write(self.text)
			f.close()

	def schedulability_test(self):
		""" Return whether it can work by schedulability test  """
		n = len(self.task_arr)
		if self.schedule_type == 'RM':
			evaluation = n * (pow(2, 1/n) - 1)
		elif self.schedule_type == 'EDF':
			evaluation = 1
		elif self.schedule_type == 'LST':
			return 1
		
		schedulability = 0
		task:Task
		for task in self.task_arr:
			schedulability += task.excution_time/min(task.period, task.relative_deadline)
		
		# print(schedulability, evaluation)
		# Check whether it can work by comparing schedulability and evaluation
		if schedulability <= evaluation:
			return 1
		else:
			return 0

	def minimum_run_times(self):
		""" Return the minimum clocks for all tasks """
		period_arr = []
		max_phase_time = 0

		task:Task
		for task in self.task_arr:

			period_arr.append(task.period)
			if(task.phase_time > max_phase_time):
				max_phase_time = task.phase_time

		return math.lcm(*period_arr)+max_phase_time

	def run(self):
		""" Run on the real time system """
		
		# check whether tasks work by schedulability test
		if(self.schedulability_test() != 1):
			self.text = f"Jobs might miss deadline by {self.schedule_type}\n"
			# self.write_file()
			# return

		end_clock = self.minimum_run_times()

		for clock in range(0, end_clock):

			# check each job can finish before deadline
			missing_str = self.ready_queue.check_whether_jobs_wont_miss_deadline(clock)

			# check whether it's time to insert job to ready queue
			task:Task
			for task in self.task_arr:
				left_time_to_start = clock - task.phase_time
				if(left_time_to_start >= 0 and left_time_to_start % task.period == 0):
					job:Job = Job(task, clock)
					self.ready_queue.insert(self.schedule_type, job)


			# excute job from ready queue
			name = '{:<2}'.format(self.ready_queue.get_first_priority_job())
			self.text += f"{clock} {name} {missing_str}\n"

			# self.ready_queue.printRQ()
			# print(f"{'{:<2}'.format(clock)} {name}")
			# print("---\n")
		
		self.text += f"Total job number: {self.ready_queue.total_job_num}\n"
		self.text += f"Miss deadline job number: {self.ready_queue.miss_deadline_job_num}\n"
		
		self.write_file()



