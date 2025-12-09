# test.py
import logging
import time

logger = logging.getLogger("demo")
logging.basicConfig(level=logging.INFO)

def do_something(name: str) -> str:
    msg = f"Hello, {name}!"
    logger.info(msg)
    return msg

if __name__ == "__main__":
    while True:
        do_something("world")
        time.sleep(3)
