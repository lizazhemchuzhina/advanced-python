import time
import codecs
from datetime import datetime
from multiprocessing import Queue
from multiprocessing import Process
from multiprocessing import Pipe


def process_a(in_p, out_p):
    while True:
        out_p.send(in_p.get().lower())
        time.sleep(5)


def process_b(in_p, out_p):
    while True:
        out_p.send(codecs.encode(in_p.recv(), "rot_13"))


if __name__ == '__main__':
    main_to_a = Queue()
    a_to_b, b_to_a = Pipe()
    b_to_main, main_to_b = Pipe()
    Process(target=process_a, args=(main_to_a, a_to_b), daemon=True).start()
    Process(target=process_b, args=(b_to_a, b_to_main), daemon=True).start()
    dialogue = []
    while True:
        message = input(">>> ")
        dialogue.append("Time is " + datetime.now().strftime("%H:%M:%S") + "   " + message + '\n')
        if message == "exit":
            dialogue.append("\nSession was stopped")
            break
        main_to_a.put(message)
        message = main_to_b.recv()
        dialogue.append("Time is " + datetime.now().strftime("%H:%M:%S") + "   " + message + '\n')
        print(message)
    with open("artifacts/hard.txt", "w") as file:
        for d in dialogue:
            file.write(d)
