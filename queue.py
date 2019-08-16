from pythonds.basic import Queue
def hotline(namelist,num):
    squeue=Queue()
    for name in namelist:
        squeue.enqueue(name)
    while squeue.size()>1:
        for i in range(num):
            squeue.enqueue(squeue.dequeue())
        squeue.dequeue()
    return squeue.dequeue()
print(hotline(["banu","devi","subha","kane","able","alfred"],5))
