# Estimated time
# 30 min
#
# Level of difficulty
# Low
#
# Objectives
# improving the student's skills in creating logs;
# improving the student's skills in creating their own handler and formatter.

# Scenario
# It's likely that the temperature of your phone battery can get
# pretty high. Check if that’s true. Write a program that will
# simulate the recording of battery temperatures with an interval
# of one minute. The simulation should contain 60 logs (the last hour).
#
# To simulate temperatures, use one of the available random functions
# in Python. Temperatures should be drawn in the range of 20–40 degrees
# Celsius, and then saved in the following format:
#
# LEVEL_NAME – TEMPERATURE_IN_CELSIUS UNIT => DEBUG – 20 C
#
# The drawn temperatures should be assigned to the appropriate level
# depending on their value:
#
# DEBUG = TEMPERATURE_IN_CELSIUS < 20
# WARNING = TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35
# CRITICAL = TEMPERATURE_IN_CELSIUS > 35
#
# Put all logs in the battery_temperature.log file. The task will be
# completed when you implement your own handler and formatter.

import logging
import random

FORMAT = '%(levelname)s - %(message)s'


class BatterySimulation:
    def __init__(self, logger):
        self.logger = logger

    def simulate_last_hour(self):
        for minute in range(1, 60 + 1):
            temperature = random.randint(20, 40)

            if temperature < 30:
                self.logger.debug('{} C'.format(temperature))
            elif 30 <= temperature <= 35:
                self.logger.warning('{} C'.format(temperature))
            elif temperature > 35:
                self.logger.critical('{} C'.format(temperature))
            else:
                raise Exception('Temperature out of range.')


logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('battery_temperature.log', mode='w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

battery_simulation = BatterySimulation(logger)
battery_simulation.simulate_last_hour()
