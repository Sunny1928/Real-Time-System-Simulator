from utils.realTimeSystem import RealTimeSystem


SCHEDULE_TYPE = ['RM','EDF','LST'] # strict LST



if __name__ == "__main__":
	
	""" Test """
	# file = 6
	# schedule_type = SCHEDULE_TYPE[1]
	# system = RealTimeSystem(file, schedule_type)
	# text = system.run()


	""" Run all data """
	for file in range(1, 7):

		for schedule_type in SCHEDULE_TYPE:
			system = RealTimeSystem(file, schedule_type)
			text = system.run()