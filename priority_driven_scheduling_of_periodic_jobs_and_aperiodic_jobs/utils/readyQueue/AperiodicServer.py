from ..job import AperiodicJob, Job
from .readyQueue import ReadyQueue

class AperiodicServer(ReadyQueue):

	def __init__(self, server_size, server_type):
		""" Initialize ready queue """
		
		super().__init__()
		self.server_deadline = 0
		self.resource = 0 # es
		self.server_size = server_size
		self.server_type = server_type
		



	def hasResource(self):
		""" Check whether server has resources """

		return self.resource 
	


	def hasJobs(self):
		""" Check whether ready queue has jobs """

		return len(self.ready_queue) 



	def check_whether_jobs_wont_miss_deadline(self, clock):
		""" Check whether the first job in the ready queue can finish in time """
		
		text = ""

		if self.hasJobs() and self.hasResource() and self.server_deadline < clock:
			
			job:AperiodicJob = self.get_first_priority_job()
			text += f"{job.name} "
			self.ready_queue.remove(job)

		if(text == ""): return ""
		else: return f"({text}miss deadline)"



	def insert(self, clock, new_job:AperiodicJob):
		""" Insert a job to ready queue """

		# Check R2 and update server deadline and resources
		if(len(self.ready_queue) == 0):

			if self.server_type == 'CUS':
				if clock >= self.server_deadline:
					self.server_deadline = clock + new_job.excution_time/self.server_size
					self.resource = new_job.excution_time

				else:
					"""Do nothing"""
					
			elif self.server_type == 'TBS':
				self.server_deadline = max(clock, self.server_deadline) + new_job.excution_time/self.server_size
				self.resource = new_job.excution_time
		
		self.ready_queue.append(new_job)




	def check_deadline_equal_clock(self, clock):
		""" For CUS, check R3 and update server deadline and resources"""

		if(self.server_type == 'CUS'):
			if  self.server_deadline == clock:
				if self.get_first_priority_job() != -1:
					self.server_deadline = self.server_deadline + self.get_first_priority_job().excution_time/self.server_size
					self.resource = self.get_first_priority_job().excution_time
		


	def excute_job(self, clock):
		""" Excute Job """
		
		job:Job = self.ready_queue[0]
		name = job.name
		job.excution_time -= 1
		self.resource -= 1
		
        # Check job is over and remove it
		if(job.excution_time == 0):

			self.finished_a_job_number += 1
			self.total_response_time += clock - job.arrive_time + 1
			self.ready_queue.remove(job)

			# For TBS, check R3 and update server deadline and resources
			if(self.server_type == 'TBS'):
				if self.get_first_priority_job() != -1:
					self.server_deadline = self.server_deadline + self.get_first_priority_job().excution_time/self.server_size
					self.resource = self.get_first_priority_job().excution_time
				else:
					"""Do nothing"""

		return name
		

	
	def print_rq(self):
		""" Print ready queue """

		print("Ready queue")		
		text = ''
		job:AperiodicJob
		for job in self.ready_queue:
			text = f"{text} {job.arrive_time} "
		print(text)

