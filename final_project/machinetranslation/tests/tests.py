import unittest
from translator import english_to_french as e_f, french_to_english as f_e

class testE2F(unittest.TestCase):
    def tst(self):
        self.assertIsNone(e_f(None))
        self.assertEqual(e_f("Hello"),"Bonjour")
        self.assertNotEqual(e_f("Bonjour"),"Hello")

class testF2E(unittest.TestCase):
    def tst(self):
        self.assertIsNone(f_e(None))
        self.assertEqual(f_e("Bonjour"),"Hello")
        self.assertNotEqual(f_e("Hello"),"Bonjour")

unittest.main()