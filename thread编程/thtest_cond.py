import threading, time

share = 0
share_cond = threading.Condition()				# 建立条件变量

class ProThread(threading.Thread):				# 定义生产者线程
	def __init__(self):
		super().__init__()
		self.name = 'Produce'

	def run(self):
		global share
		if share_cond.acquire():				# 获取共享资源	
			while True:
				if not share:
					share += 1
					print(self.name, share)
					share_cond.notify()			# 唤醒等待的线程
				share_cond.wait()
				time.sleep(1)


class CustomThread(threading.Thread):			# 定义消费者线程
	def __init__(self):
		super().__init__()
		self.name = 'Custom'

	def run(self):
		global share
		if share_cond.acquire():
			while True:
				if share:
					share -= 1
					print(self.name, share)
					share_cond.notify()
				share_cond.wait()
				time.sleep(1)


if __name__ == '__main__':
	t = ProThread()
	tt = CustomThread()
	t.start()
	tt.start()