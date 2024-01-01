from ..job import PeriodicJob
from .readyQueue import ReadyQueue

class PeriodicReadyQueue(ReadyQueue):

	def __init__(self):
		""" Initialize ready queue """

		super().__init__()
		self.total_job_num = 0
		self.miss_deadline_job_num = 0
		self.total_response_time = 0
		self.finished_a_job_number = 0



	def insert(self, new_job:PeriodicJob):
		""" Initialize ready queue """

		self.total_job_num += 1

		new_job_val = new_job.absolute_deadline
		job:PeriodicJob
		for idx, job in  enumerate(self.ready_queue):
			job_val = job.absolute_deadline

            # Predencnce of new job is smaller
			if(new_job_val < job.absolute_deadline):
				self.ready_queue.insert(idx, new_job)
				return
            
            # Predencnce of new job is same with the old one, so check with job id
			elif(new_job_val == job_val and new_job.id < job.id):
				self.ready_queue.insert(idx, new_job)
				return
		
		self.ready_queue.append(new_job)



	def check_whether_jobs_wont_miss_deadline(self, clock):
		""" Check whether all jobs in the ready queue can finish in time by absolute_deadline - clock - excution_time """

		text = ""
		delete_arr = []
		job:PeriodicJob
		for job in self.ready_queue:
			if(job.absolute_deadline - clock - job.excution_time < 0):
					self.miss_deadline_job_num += 1
					delete_arr.append(job)
					text += f"{job.name} "
		
		for job in delete_arr:
			self.ready_queue.remove(job)	

		if(text == ""): return ""
		else: return f"({text}miss deadline)"

	

	def excute_job(self, clock):
		""" Excute Job """
		
		job:PeriodicJob = self.ready_queue[0]
		name = job.name
		job.excution_time -= 1
		
        # Check job is over and remove it
		if(job.excution_time == 0):
			self.finished_a_job_number += 1
			self.total_response_time += clock - job.arrive_time + 1
			self.ready_queue.remove(job)

		return name
		
	

	def print_rq(self):
		""" Get the first priority out of ready queue """
		print("Ready queue")		
		text = ''
		job:PeriodicJob
		for job in self.ready_queue:
			text = f"{text} {job.name}:{job.absolute_deadline} "
		print(text)

