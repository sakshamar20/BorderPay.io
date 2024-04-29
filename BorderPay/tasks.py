from datetime import datetime
import time

def run():
    print("Executing run() at:", datetime.now())

start = time.time()

while True:
    if (time.time() - start >= 30):
        run()
        start = time.time()





