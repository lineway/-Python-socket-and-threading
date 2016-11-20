import threading, time, random


share = 4

class MyThread(threading.Thread):
	def __init__(self, i):
		super().__init__()
		self.i = i

	def run(self):
		global share
		for d in range(3):
			lock.acquire()
			print(share)
			share += self.i
			time.sleep(random.random())
			print('+', self.i, '=',share)
			lock.relase()

lock = threading.Lock()

if __name__ == '__main__':
	t = MyThread(2)
	tt = MyThread(6)
	t.start()
	tt.start()