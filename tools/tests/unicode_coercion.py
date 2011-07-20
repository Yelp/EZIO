#!/usr/bin/python

import testify
from testify.assertions import assert_equal

from tools.tests.test_case import EZIOTestCase

class MyStringable(object):
    def __str__(self):
        return 'ohai'

    def __unicode__(self):
        return u'ohaiunicode'

display = {
        'first': 1,
        'second': 2.0,
        'third': u'asdf',
        'fourth': MyStringable(),
}

class SimpleTestCase(EZIOTestCase):

    target_template = 'coercion'

    # $third is a unicode (u'asdf'), which forces coercion of everything to unicode
    expected_result_type = unicode

    def get_display(self):
        return display

    def get_refcountables(self):
        return display.values()

    def test(self):
        super(SimpleTestCase, self).test()
        assert_equal(
            self.result.split(),
            ['first', '1', 'second', '2.0', 'third', 'asdf', 'fourth', 'ohaiunicode']
        )

if __name__ == '__main__':
    testify.run()
