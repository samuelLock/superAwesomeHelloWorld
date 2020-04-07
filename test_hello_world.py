import hello_world
import unittest

class TestHelloWorld(unittest.TestCase):

    def testMessage(self):
        message = 'Hello, World!'
        self.assertEqual(hello_world.message(), message)

if __name__ == '__main__':
    unittest.main()
