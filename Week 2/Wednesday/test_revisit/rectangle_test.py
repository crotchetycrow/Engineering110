from rectangle import *


def test_get_width():
    r = Rectangle(width=10,height=5)
    assert r.width == 10

def test_get_height():
    r = Rectangle(width=10,height=5)
    assert r.height == 5
