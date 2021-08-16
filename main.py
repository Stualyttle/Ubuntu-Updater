import os
import time
import logging

start_time = time.time()
seconds = 5

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > seconds:
        # Update computer
        print("Updating...")
        logging.info("Updating...")
        os.system("sudo apt update")
        print("Updated, now upgrading...")
        logging.info("Updated, now upgrading...")
        os.system("sudo apt upgrade -y")
        print("Upgraded.")
        logging.info("Upgraded.")

        # Reset counter and set next update to every 12 hours:
        elapsed_time = 0
        start_time = time.time()
        seconds = 43200
