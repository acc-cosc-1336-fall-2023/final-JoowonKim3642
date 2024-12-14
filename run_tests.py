#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here

import unittest

from tests.question_tests import question_a_tests

suite = unittest.TestLoader().loadTestsFromModule(question_a_tests)
unittest.TextTestRunner(verbosity=2).run(suite)
