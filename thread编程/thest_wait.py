import threading, time

class MyThread(threading.Thread):
	def run(self):
		for i in range(30):
			print('threading: ', i)
			time.sleep(0.1)


if __name__ == '__main__':
	t = MyThread()
	t.start()
	t.join(1)
	for i in range(1,10):
		print('Main:', i)
		time.sleep(0.1)