import unittest
import pytest



@pytest.mark.usefixtures("setup")
class Base(unittest.TestCase):
    pass

