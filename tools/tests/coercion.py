#!/usr/bin/python

import testify
from testify.assertions import assert_equal

from tools.tests.test_case import EZIOTestCase

class MyStringable(object):
    def __str__(self):
        return 'ohai'

display = {
        'first': 1,
        'second': 2.0,
        'third': 'asdf',
        'fourth': MyStringable(),
}

class SimpleTestCase(EZIOTestCase):

    target_template = 'coercion'

    def get_display(self):
        return display

    def get_refcountables(self):
        return display.values()

    def test(self):
        super(SimpleTestCase, self).test()
        assert_equal(
            self.result.split(),
            ['first', '1', 'second', '2.0', 'third', 'asdf', 'fourth', 'ohai']
        )

if __name__ == '__main__':
    testify.run()
