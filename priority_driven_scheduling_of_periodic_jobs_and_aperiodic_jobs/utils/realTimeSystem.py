from utils.task import PeriodicTask
from utils.job import PeriodicJob, AperiodicJob
from utils.readyQueue.AperiodicServer import AperiodicServer
from utils.readyQueue.periodicReadyQueue import PeriodicReadyQueue

FILE = 'simple'
FILE_STATUS = 'test'

class RealTimeSystem:

	def __init__(self, periodic_file, aperiodic_file, server_size, server): #'periodic' 'aperiodic'
		""" Initialize """

		self.server = server
		self.output_file = periodic_file
		self.periodic_ready_queue = PeriodicReadyQueue()
		self.aperiodic_ready_queue = AperiodicServer(server_size, server)
		self.text = ""

		self.periodic_tasks  = self.read_periodic_file(periodic_file)
		self.aperiodic_jobs  = self.read_aperiodic_file(aperiodic_file)
		self.maxSimTime = 1000



	def read_periodic_file(self, file_name):
		""" Read file and save all periodic tasks """

		with open(f'./data/{FILE_STATUS}/test/{file_name}.txt') as f:
			lines = f.read().splitlines()
			f.close()

		all_tasks = []
		for idx, line in enumerate(lines):
			numbers = [ int(x) for x in line.split(',',2) ]
			new_task = PeriodicTask(f"T{idx+1}", idx, *numbers)
			all_tasks.append(new_task)

		return all_tasks
	


	def read_aperiodic_file(self, file_name):
		""" Read file and store all aperiodic tasks """

		with open(f'./data/{FILE_STATUS}/test/{file_name}.txt') as f:
			lines = f.read().splitlines()
			f.close()

		all_jobs = []
		for idx, line in enumerate(lines):
			numbers = [ int(x) for x in line.split(',',2) ]
			new_job = AperiodicJob(f"A{idx+1}", *numbers)
			all_jobs.append(new_job)

		return all_jobs
	


	def write_file(self):
		""" Write file  """
		with open(f"./data/test/ans/{self.server}/{self.output_file}.txt", "w") as f:
			f.write(self.text)
			f.close()



	def print_rts(self, clock):
		""" Print RTS execution"""

		pj:PeriodicJob = self.periodic_ready_queue.get_first_priority_job()
		aj:AperiodicJob = self.aperiodic_ready_queue.get_first_priority_job()
						
		print("CLOCK: ", clock)
		if pj != -1:
			pj.print_job()
		else:
			print("No Periodic Job\n")
		
		if aj != -1:
			print(self.aperiodic_ready_queue.resource)
			print(self.aperiodic_ready_queue.server_deadline)
			aj.print_job()
		else:
			print("No Aperiodic Job\n")

		print("-------------------------------")



	def excute_high_priority_job(self, clock):
		""" Excute high priority from periodic ready queue and aperiodic ready queue in server """

		pj:PeriodicJob = self.periodic_ready_queue.get_first_priority_job()
		aj:AperiodicJob = self.aperiodic_ready_queue.get_first_priority_job()

		if aj!=-1 and pj!= -1 and self.aperiodic_ready_queue.hasResource() and pj.absolute_deadline >= self.aperiodic_ready_queue.server_deadline:
			return self.aperiodic_ready_queue.excute_job(clock)
		
		elif aj!=-1 and pj== -1 and self.aperiodic_ready_queue.hasResource():
			return self.aperiodic_ready_queue.excute_job(clock)
			
		elif pj!= -1 :
			return self.periodic_ready_queue.excute_job(clock)

		else:
			return ''



	def run(self):
		""" Run on the real time system """

		for clock in range(0, self.maxSimTime+1):

			missing_str = ""

			# 1. check periodic jobs and aperiodic jobs finish before deadline
			missing_str += self.periodic_ready_queue.check_whether_jobs_wont_miss_deadline(clock)
			missing_str += self.aperiodic_ready_queue.check_whether_jobs_wont_miss_deadline(clock)

			# 2. check whether it's time to insert periodic task to periodic ready queue
			task:PeriodicTask
			for task in self.periodic_tasks:
				if(clock % task.period == 0):
					job:PeriodicJob = PeriodicJob(clock, task)
					self.periodic_ready_queue.insert(job)


			# 3. check whether it's time to insert aperiodic job to aperiodic ready queue
			for job in self.aperiodic_jobs:
				if(clock == job.arrive_time):
					# insert to aperodic queue
					self.aperiodic_ready_queue.insert(clock, job)


			# 4. check aperiodic_ready_queue's deadline equal clock
			self.aperiodic_ready_queue.check_deadline_equal_clock(clock)
					

			# 5. excute job from ready queue
			name = self.excute_high_priority_job(clock)


			self.text += f"{clock} {'{:<2}'.format(name)} {missing_str}\n"


		self.text += f"\nPERIODIC JOBS:\n"
		self.text += f"Miss deadline job number: {self.periodic_ready_queue.miss_deadline_job_num}\n"
		self.text += f"Total job number: {self.periodic_ready_queue.total_job_num}\n"
		self.text += f"Miss rate: {self.periodic_ready_queue.miss_deadline_job_num / self.periodic_ready_queue.total_job_num}\n"
		
		self.text += f"\nAPERIODIC JOBS:\n"
		self.text += f"Aperiodic jobs total response time: {self.aperiodic_ready_queue.total_response_time}\n"
		self.text += f"Finish a job number: {self.aperiodic_ready_queue.finished_a_job_number}\n"
		self.text += f"Average aperiodic job response time: {self.aperiodic_ready_queue.total_response_time / self.aperiodic_ready_queue.finished_a_job_number}\n"
		
		self.write_file()



