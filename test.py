from utils.realTimeSystem import RealTimeSystem


SCHEDULE_TYPE = ['RM','EDF','LST'] # strict LST



if __name__ == "__main__":
	
	""" Test """
	# file = 1
	# schedule_type = SCHEDULE_TYPE[0]
	# system = real_time_system(file, schedule_type)
	# text = system.run()


	""" Run all data """
	for file in range(1, 7):

		for schedule_type in SCHEDULE_TYPE:
			system = RealTimeSystem(file, schedule_type)
			text = system.run()