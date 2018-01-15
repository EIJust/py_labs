import time
from threading import Thread
from queue import Queue
from lab_3 import get_washingtonpost_news


class WashingtonpostNewsMonitor(Thread):
    def __init__(self, news_queue):
        super(WashingtonpostNewsMonitor, self).__init__()
        self.news_queue = news_queue
        self.old_news = set()

    def run(self):
        while True:
            news = set(get_washingtonpost_news())
            new_news = news - self.old_news
            self.old_news = self.old_news | new_news
            for n in list(new_news):
                self.news_queue.put(n)
        time.sleep(1)


if __name__ == '__main__':
    queue = Queue()
    monitor = WashingtonpostNewsMonitor(queue)
    monitor.setDaemon(True)
    monitor.start()

    while True:
        print(queue.get())
