class Queue(object):
    def __init__(self):
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def enqueue(self, item):
        self.queue.append(item)
        print("%s enqueue success" %(item))
    def is_empty(self):
        return self.queue == []
    def dequeue(self):
        if not self.is_empty():
            item = self.queue[0]
            self.queue.remove(item)
            print("%s dequeue success" % (item))
        else:
            raise Exception("queue is null")
    def first(self):
        if not self.is_empty():
            item = self.queue[0]
            print("first item is %s" % (item))
        else:
            raise Exception("queue is null")

q = Queue()
for item in range(10):
    q.enqueue(item)
for item in range(3):
    q.dequeue()
print("queue len is ", len(q))