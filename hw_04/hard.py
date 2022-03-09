import time
import codecs
from datetime import datetime
from multiprocessing import Queue
from multiprocessing import Process


def process_a(main_to_a, a_to_b):
    while True:
        a_to_b.put(main_to_a.get().lower())
        time.sleep(5)


def process_b(a_to_b, b_to_main):
    while True:
        b_to_main.put(codecs.encode(a_to_b.get(), "rot_13"))


if __name__ == '__main__':
    main_to_a = Queue()
    a_to_b = Queue()
    b_to_main = Queue()
    Process(target=process_a, args=(main_to_a, a_to_b), daemon=True).start()
    Process(target=process_b, args=(a_to_b, b_to_main), daemon=True).start()
    dialogue = []
    while True:
        message = input(">>> ")
        dialogue.append("Time is " + datetime.now().strftime("%H:%M:%S") + "   " + message + '\n')
        if message == "exit":
            dialogue.append("\nSession was stopped")
            break
        while not b_to_main.empty():
            out_str = "\nTime is " + datetime.now().strftime("%H:%M:%S") + \
                      " encoded message is : " + b_to_main.get() + '\n'
            print(out_str)
            dialogue.append(out_str)
        main_to_a.put(message)
    with open("artifacts/hard.txt", "w") as file:
        for d in dialogue:
            file.write(d)
