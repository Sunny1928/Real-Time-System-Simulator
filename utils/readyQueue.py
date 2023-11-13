from .job import Job

class ReadyQueue:

	def __init__(self):
		""" Initialize ready queue """
		self.total_job_num = 0
		self.miss_deadline_job_num = 0
		self.ready_queue = []


	def insert(self, schedule_type, new_job:Job):
		""" Initialize ready queue """
		self.total_job_num += 1

        # Set attribute to get according to scheduler
		if(schedule_type == 'RM'):
			attr = 'period'
		elif(schedule_type == 'EDF'):
			attr = 'absolute_deadline'
		elif(schedule_type == 'LST'):
			attr = 'slack'

		new_job_val = getattr(new_job, attr)
		job:Job
		for idx, job in  enumerate(self.ready_queue):
			job_val = getattr(job, attr)

            # Predencnce of new job is smaller
			if(new_job_val < job_val):
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
		job:Job
		for job in self.ready_queue:
			if(job.absolute_deadline - clock - job.excution_time < 0):
					self.miss_deadline_job_num += 1
					self.ready_queue.remove(job)	
					text += f"{job.name} "
		
		if(text == ""): return ""
		else: return f"({text}miss deadline)"

	

	
	def get_first_priority_job(self):
		""" Get the first priority out of ready queue """
		
        # There is no job in ready queue
		if len(self.ready_queue) == 0:
			return ''
		
		job:Job = self.ready_queue[0]
		name = job.name
		job.excution_time -= 1
		
        # Check job is over and remove it
		if(job.excution_time == 0):
			self.ready_queue.remove(job)

		return name
		
	
	def printRQ(self):
		""" Get the first priority out of ready queue """
		print("Ready queue")		
		text = ''
		job:Job
		for job in self.ready_queue:
			text = f"{text} {job.name}:{job.slack} "
		print(text)

