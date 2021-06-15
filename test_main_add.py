import pytest, os , sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


from myfunctions.mainadd import addk


def test_mainadd():
    outval = addk(5,2)
    assert outval == 7