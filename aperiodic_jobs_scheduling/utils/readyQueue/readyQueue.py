from ..job import Job

class ReadyQueue:

	def __init__(self):
		""" Initialize ready queue """
		
		self.ready_queue = []
		self.total_job_num = 0
		self.miss_deadline_job_num = 0
		self.total_response_time = 0
		self.finished_a_job_number = 0
	
	
	def check_whether_jobs_wont_miss_deadline(self, clock):
		""" Check whether all jobs in the ready queue can finish in time """


	
	def insert(self, new_job:Job):
		""" Insert job to ready queue """
	

	
	def get_first_priority_job(self):
		""" Get the first priority of ready queue """

		if(len(self.ready_queue) == 0):
			return -1
		
		return self.ready_queue[0]
	

	
	def excute_job(self):
		""" Excute Job """
		
		job:Job = self.ready_queue[0]
		name = job.name
		job.excution_time -= 1
		
        # Check job is over and remove it
		if(job.excution_time == 0):
			self.ready_queue.remove(job)

		return name

	

	def print_rq(self):
		""" Get the first priority out of ready queue """
		

