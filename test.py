import math
import copy

class Node:
	
	def __init__(self, name, order, phase_time, period, relative_deadline, excution_time):
		self.name = name
		self.order = order
		self.phase_time = phase_time
		self.period = period
		self.relative_deadline = relative_deadline
		self.excution_time = excution_time
		self.absolute_deadline = 0
		self.slack = 0

	def print_node(self):
		print(self.name, self.phase_time, self.period, self.relative_deadline, self.excution_time)


class ReadyQueue:

	def check_whether_jobs_can_finish(self, clock):
		""" Check whether all jobs in the ready queue can finish in time by ad - c - e"""

		job:Node
		for job in self.ready_queue:
			if(job.absolute_deadline - clock - job.excution_time < 0):
					self.miss_deadline_job_num += 1
					self.ready_queue.remove(job)	
					# print(f"{job.name} miss schedule!")
					return f"{job.name} miss schedule!\n"
		return ""


	
	def schedulabilityTest(self, schedule_type):
		
		n = len(self.ready_queue)
		if schedule_type == 'EDF':
			evaluation = 1
		elif schedule_type == 'RM':
			evaluation = n * (math.pow(2, 1/n) - 1)


		schedulability = 0

		job:Node
		for job in self.ready_queue:
			schedulability += job.excution_time/min(job.period, job.relative_deadline)

		if schedulability <= evaluation:
			return f"it works in {schedule_type}!"
		else:
			return f"it can't work in {schedule_type}!"
	
	def __init__(self):
		self.total_job_num = 0
		self.miss_deadline_job_num = 0
		self.ready_queue = []


	def insert(self, schedule_type, new_job:Node):
		self.total_job_num += 1

		if(schedule_type == 'RM'):
			attr = 'period'
			
		elif(schedule_type == 'EDF'):
			attr = 'absolute_deadline'

		elif(schedule_type == 'LST'):
			attr = 'slack'


		new_job_val = getattr(new_job, attr)
		

		job:Node
		for idx, job in  enumerate(self.ready_queue):
			job_val = getattr(job, attr)

			if(new_job_val < job_val):
				self.ready_queue.insert(idx, new_job)
				return
			
			elif(new_job_val == job_val and new_job.order < job.order):
				self.ready_queue.insert(idx, new_job)
				return
		
		self.ready_queue.append(new_job)
	

	
	def get_first_priority_job(self):
		
		if len(self.ready_queue) == 0:
			return ''
		
		job:Node = self.ready_queue[0]
		name = job.name
		job.excution_time -= 1
		# print(job.excution_time)
		if(job.excution_time == 0):
			self.ready_queue.remove(job)

		return name
		
	
	def printLL(self):
		print("Ready queue")		
		s = ''
		job:Node
		for job in self.ready_queue:
			s = f"{s} {job.name}:{job.slack} "
		print(s)
	

def at_least_run_times(jobs):

	period_arr = []
	max_phase_time = 0

	job:Node
	for job in jobs:

		period_arr.append(job.period)
		if(job.phase_time > max_phase_time):
			max_phase_time = job.phase_time

	return math.lcm(*period_arr)+max_phase_time
	

FILE = 'test1.txt'
SCHEDULE_TYPE = ['RM','EDF','LST'] # strict LST


# read file to get all jobs

def read_file(file):
	all_tasks = []

	with open(f'test/test{file}.txt') as file:
		lines = file.read().splitlines()

	for idx, line in enumerate(lines):
		numbers = [ int(x) for x in line.split(', ',4) ]
		new_job = Node(f"T{idx+1}", idx, *numbers)
		all_tasks.append(new_job)

	""" Print all nodes """
	# task:Node
	# for task in all_tasks:
	# 	task.print_node()

	return all_tasks

def write_file(file, text):
	with open(f"ans/{schedule_type}/test{file}.txt", "w") as f:
		f.write(text)
		f.close()



def run(schedule_type, all_tasks):

	ready_queue = ReadyQueue()
	# print(ready_queue.schedulabilityTest(schedule_type))

	end_clock = at_least_run_times(all_tasks)+1

	text = ""
	for clock in range(1, end_clock):

		# print("clock ", clock)

		# check each job can finish before deadline
		text += ready_queue.check_whether_jobs_can_finish(clock)

		# check whether it's time to insert job to ready queue
		task:Node
		for task in all_tasks:
			if((clock - task.phase_time) % task.period == 0):
				job = copy.copy(task)
				job.absolute_deadline = clock + job.relative_deadline
				job.slack = job.absolute_deadline - job.excution_time
				ready_queue.insert(schedule_type, job)

		# ready_queue.printLL()

		# excute job from ready queue
		name = ready_queue.get_first_priority_job()
		text += f"{clock} {name}\n"
		# print(f"{'{:<2}'.format(clock)} {name}")
		# print("---\n")

	return text

""" Test """
# file = 1
# schedule_type = SCHEDULE_TYPE[2]
# all_tasks = read_file(file)
# text = run(schedule_type, all_tasks)
# write_file(file, text)



""" Run all data """
for file in range(1, 7):

	for schedule_type in SCHEDULE_TYPE:

		all_tasks = read_file(file)
		text = run(schedule_type, all_tasks)
		write_file(file, text)




	








