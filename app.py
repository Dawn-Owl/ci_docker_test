"""CI 연습용 간단한 데모 모듈입니다."""

import logging
import time

logger = logging.getLogger("demo")
logging.basicConfig(level=logging.INFO)

def do_something(name: str) -> str:
    """이름을 받아서 인사 메시지를 만들고 로그로 남긴다."""
    msg = f"Hello, {name}!"
    logger.info(msg)
    return msg

if __name__ == "__main__":
    while True:
        do_something("world")
        time.sleep(3)
