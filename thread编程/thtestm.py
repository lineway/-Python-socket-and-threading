import threading
import time

def thfun():
	s = 0
	for i in range(30):
		s += i
		time.sleep(0.1)
	print(s)


class MyThread(threading.Thread):

	def run(self):
		s = 0
		for i in range(30):
			s += i
			time.sleep(0.1)
		print(s)		

if __name__ == '__main__':
	# ths = [threading.Thread(target=thfun) for i in range(2)]
	# for th in ths:
	# 	th.start()
	# thfun()
	# thfun()

	ths = [MyThread() for i in range(2)]
	for th in ths:
		th.start()