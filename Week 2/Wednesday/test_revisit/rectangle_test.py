from rectangle import *

r = Rectangle(width=10,height=5)

def test_get_width():
    assert r.width == 10

def test_get_height():
    assert r.height == 5

def test_get_area():
    assert r.get_area() == 50

def test_get_perimeter():
    assert r.get_perimeter() == 30

