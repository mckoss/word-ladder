import unittest
import doctest

import ladder


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(ladder))
    return tests
