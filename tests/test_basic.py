# tests/test_basic.py
from app import do_something

def test_do_something_returns_msg():
    msg = do_something("Jack")
    assert "Jack" in msg
