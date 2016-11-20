import threading, time

event = threading.Event()

class MyThreadWait(threading.Thread):
	def run(self):
		self.name = 'Wait thread'
		print(self.name, 'Wait...')
		event.wait()
		print(self.name, 'Start...')
		event.clear()
		time.sleep(3)


class MythreadMain(threading.Thread):
	def run(self):
		time.sleep(3)
		print('Maint thread set event flag!')
		event.set()

if __name__ == '__main__':
	thw = MyThreadWait()
	thm = MythreadMain()
	thw.start()
	thm.start()

