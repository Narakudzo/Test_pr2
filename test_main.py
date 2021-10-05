import unittest
from unittest import TestCase

import ap


class UnitTest(unittest.TestCase):
    def test1(self):
        a1 = ap.MyClass(1, 2, 3)
        self.assertEqual(a1.foo1(), 2)

    def test2(self):
        a1 = ap.MyClass(1, 2, 3)
        self.assertEqual(a1.foo2(), (2, 6, 2, 6))

    def test3(self):
        a1 = ap.MyClass(1, 2, 3)
        self.assertEqual(a1.foo3(), 6)

    def test4(self):
        a1 = ap.MyClass('a', 2, 3)
        self.assertEqual(a1.foo1(), 'aa')

    def test5(self):
        a1 = ap.MyClass(0.0000000000000000000000000000000000000000000000000001, 2, 3)
        self.assertEqual(a1.foo1(), 2e-52)


