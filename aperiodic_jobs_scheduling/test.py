from utils.realTimeSystem import RealTimeSystem

SERVER_TYPE = ['CUS', 'TBS']


if __name__ == "__main__":
	
    # periodic_file = 'simple/periodic'
    # aperiodic_file = 'simple/aperiodic_2'

    # periodic_file = 'complicated/0.8'
    # aperiodic_file = 'complicated/aperiodic'

    # periodic_file = 'complicated/0.9'
    # aperiodic_file = 'complicated/aperiodic'
    server_size = 0.2

    # """ Test """
    # server = SERVER_TYPE[0]
    # system = RealTimeSystem(periodic_file, aperiodic_file, server_size, server)
    # text = system.run()


    # """ Run all data """

    for server in SERVER_TYPE:

        periodic_file = 'simple/periodic'
        aperiodic_file = 'simple/aperiodic_2'

        periodic_file = 'complicated/0.8'
        aperiodic_file = 'complicated/aperiodic'

        periodic_file = 'complicated/0.9'
        aperiodic_file = 'complicated/aperiodic'

        system = RealTimeSystem(periodic_file, aperiodic_file, server_size, server)
        text = system.run()