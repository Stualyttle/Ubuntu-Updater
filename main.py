import os
from time import sleep
import logging

while True:
    # Update computer
    print("Updating...")
    logging.info("Updating...")
    os.system("sudo apt update")
    print("Updated, now upgrading...")
    logging.info("Updated, now upgrading...")
    os.system("sudo apt upgrade -y")
    print("Upgraded.")
    logging.info("Upgraded.")
    sleep(43200)
