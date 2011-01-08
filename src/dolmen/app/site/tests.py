import unittest
import doctest

from zope.app.wsgi.testlayer import BrowserLayer

import dolmen.app.site

browser_layer = BrowserLayer(dolmen.app.site)

def test_suite():
    suite = unittest.TestSuite()

    app_test = doctest.DocFileSuite('README.txt',
        optionflags = (
            doctest.ELLIPSIS +
            doctest.NORMALIZE_WHITESPACE +
            doctest.REPORT_NDIFF),
        globs={'getRootFolder': browser_layer.getRootFolder})
    app_test.layer = browser_layer

    suite.addTest(app_test)
    return suite
