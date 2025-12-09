import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import do_something


def test_do_something_returns_msg():
    msg = do_something("Jack")
    assert "Jack" in msg
