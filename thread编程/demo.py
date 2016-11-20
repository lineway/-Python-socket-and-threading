import threading,time

share = 0

share_cond = threading.Condition()

class ProThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = 'Produce'

    def run(self):
        global share
        if share_cond.acquire():
            while True:
                if not share:
                    share += 1
                    print(self.name,share)
                    share_cond.notify()
                share_cond.wait()
                time.sleep(1)

class CustomThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = 'Custom'

    def run(self):
        global share
        if share_cond.acquire():
            while True:
                if share:
                    share -= 1
                    print(self.name,share)
                    share_cond.notify()
                share_cond.wait()
                time.sleep(1)

if __name__ == '__main__':
    t  = ProThread()
    tt = CustomThread()
    t.start()
    tt.start()