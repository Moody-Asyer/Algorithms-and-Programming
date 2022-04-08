import threading
import time
import sys


class Philosopher(threading.Thread):
    running = True

    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            time.sleep(20)
            print ('Philosopher %s is hungry.' % self.index)
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
        while self.running:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print ('Philosopher %s starts eating. '% self.index)
        time.sleep(25)
        print ('Philosopher %s finishes eating and leaves to think.' % self.index)

def main():
    forks = [threading.Semaphore() for n in range(filsuf)]
    philosophers= [Philosopher(i, forks[i%filsuf], forks[(i+1)%filsuf])
            for i in range(filsuf)]

    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(85)
    Philosopher.running = False
    time.sleep(100)
    print ("Now we're finishing.")


if __name__ == "__main__":
    n = len(sys.argv)
    global filsuf
    global makan
    if n == 5:
        if sys.argv[1] == "--filsuf" and sys.argv[3] == "--makan":
            filsuf = int(sys.argv[2])
            makan = int(sys.argv[4])
            main()
    else:
        print("wrong format!")
        print("format : python dining_philosopher.py --filsuf n --makan n")