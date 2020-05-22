from larpix import Controller
from larpix.io import ZMQ_IO

# controller = Controller()
# controller.io = ZMQ_IO(config_filepath = '/Users/jamesdeleon/larpix_v3/larpix-control/larpix/configs/io/daq-srv4.json', mosi_map = {2:1})
# controller.load('/Users/jamesdeleon/larpix_v3/larpix-control/larpix/configs/controller/pcb-5_chip_info.json')
# controller.io.ping()

# for key,chip in controller.chips.items():
# 	chip.config.load('/Users/jamesdeleon/larpix_v3/larpix-control/larpix/configs/chip/quiet.json')
# 	print(key, chip.config)
# 	controller.write_configuration(key)

# print(controller.run(1,'checking the data rate'))
# print(controller.reads[-1])

# print(controller.verify_configuration())


class Test:

	base_filepath = '/Users/jamesdeleon/larpix_v3/larpix-control/larpix/configs'

	def __init__(self):
		self.controller = Controller()
		self.controller.io = ZMQ_IO(config_filepath = Test.base_filepath + '/io/daq-srv4.json', miso_map = {2:1})
		self.controller.load(Test.base_filepath + '/controller/pcb-5_chip_info.json')

	def ping(self):
		return self.controller.io.ping()

	def quiet_state(self):
		for key, chip in self.controller.chips.items():
			chip.config.load(Test.base_filepath + '/chip/quiet.json')
			print(key, chip.config)
			self.controller.write_configuration(key)

		print(self.controller.run(5, 'checking the data rate'))
		print(self.controller.reads[-1])

		return ''

	def verify(self):
		return self.controller.verify_configuration()


if __name__ == '__main__':

	trial = Test()
	trial.ping()
	trial.quiet_state()
	trial.verify()


