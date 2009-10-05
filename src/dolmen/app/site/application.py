# -*- coding: utf-8 -*-

import grok
import dolmen.content as content
from dolmen.app.site import IDolmen


class Dolmen(grok.Application, content.Container):
    """A Dolmen Site Manager.
    """
    grok.implements(IDolmen)
    content.nofactory()
    title = u"My Dolmen Site"
