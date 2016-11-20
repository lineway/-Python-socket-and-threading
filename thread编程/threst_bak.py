import threading, time

def dmn():
	print('dmn start ...')
	time.sleep(2)
	print('dmn stop ...')

def ndmn():
	print('ndmn start ...')
	time.sleep(1)
	print('ndmn stop.')

d = threading.Thread(target=dmn)
d.daemon = True # 设置为后台线程
n = threading.Thread(target=ndmn)
print('start...')

d.start()
n.start()
print('end.')