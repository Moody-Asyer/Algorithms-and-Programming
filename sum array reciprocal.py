import threading
import random
import time
import sys

my_array = []
sum = 0.0


class multithread(threading.Thread):
    def __init__(self, id, array, indexEnd, npath):
        threading.Thread.__init__(self)
        self.id = id
        self.array = array
        self.npath = npath
        self.indexEnd = indexEnd

    def run(self):
        reciprocal(self.array, self.indexEnd, self.npath)


def reciprocal(array, indexEnd, npath):
    global sum
    for i in range(int(indexEnd - npath), int(indexEnd)):
        sum = sum + (1 / my_array[i])


def make_array(numberArray):
    print("Menggenerate array " + str(numberArray) + " processing dan reciprocal.")
    for x in range(numberArray):
        my_array.append(float(random.randint(1, 99)))


def start_time():
    return time.time()


def end_time(start):
    end = time.time()
    return (end - start)

def main():

    npath = 0
    numberOfArray = 0
    multi_thread = []
    index_End = 0

    for i, arg in enumerate(sys.argv):
        if (arg == "--thread"):
            npath = int(sys.argv[i + 1])
        if (arg == "--array"):
            numberOfArray = int(sys.argv[i + 1])

    startMakeArray = start_time()
    make_array(numberOfArray)
    print("%s %0.2f %s" % ("Waktu pengerjaan  :", end_time(startMakeArray), "detik\n"))

    startReciprocal = start_time()
    print("Menghitung sum dari array reciprocal processing.")

    for x in range(npath):
        index_End = index_End + (numberOfArray / npath)
        multi_thread.append(multithread(x, my_array, index_End, numberOfArray / npath))

    for x in range(npath):
        multi_thread[x].start()

    for x in range(npath):
        multi_thread[x].join()
    print("%s %0.2f %s" % ("Waktu pengerjaan  :", end_time(startReciprocal), "detik\n"))

if __name__ == "__main__":
    main()

