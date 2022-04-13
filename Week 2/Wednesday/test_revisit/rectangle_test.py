from rectangle import *


def test_get_width():
    r = Rectangle(width=10)
    assert r.width == 10
