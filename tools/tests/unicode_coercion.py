#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        # this is a true unicode object that happens to also contain a non-ASCII character:
        'fifth': u"hommage à jack",
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
        # note that 'asdf' == u'asdf', so we don't need to explicitly prefix the
        # literals here with u:
        assert_equal(
            self.result.strip().split('\n'),
            ['first', '1', 'second', '2.0', 'third', 'asdf', 'fourth', 'ohaiunicode',
             'fifth', u'hommage \xe0 jack'
            ]
        )

if __name__ == '__main__':
    testify.run()
