from mockito import mock, verify
import unittest

from TourismDataAnalysis import helloworld,val_2,val_3,val_4

class HelloWorldTest(unittest.TestCase):
    def test_1(self):
        out = mock()

        helloworld(out)

        verify(out).write('0.0')
        
    def test_2(self):
        out = mock()
        val_2(out)
        
        verify(out).write('1633890.9090909064')
        
    def test_3(self):
        out = mock()
        val_3(out)
        
        verify(out).write('2008000.0')
        
    def test_4(self):
        out = mock()
        val_4(out)
        
        verify(out).write('102763.63636363624')
        
        
        