import unittest
import doctest

import ladder


def load_tests(loader, tests, ignore):
    """ Run all doctests. """
    tests.addTests(doctest.DocTestSuite(ladder))
    return tests


class TestLadder(unittest.TestCase):
    def test_foobar(self):
        self.assertEqual(ladder.min_ladder('foo', 'bar'), ['foo', 'for', 'far', 'bar'])

    def test_not_in_dict(self):
        self.assertEqual(ladder.min_ladder('foo', '---'), None)

    def test_mismatch(self):
        self.assertRaises(Exception, ladder.min_ladder, ('a', 'bar'))

