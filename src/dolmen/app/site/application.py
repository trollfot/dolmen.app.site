# -*- coding: utf-8 -*-

import grok
import dolmen.content as content
from dolmen.app.site import IDolmen
from dolmen.app.authentication import initialize_auth
from dolmen.relations import ICatalog, RelationCatalog
from zope.app.security.interfaces import IAuthentication
from zope.app.authentication import PluggableAuthentication


class Dolmen(grok.Application, content.Container):
    """A Dolmen Site Manager with a local registry.
    """
    grok.implements(IDolmen)
    content.nofactory()
    title = u"My Dolmen Site"

    grok.local_utility(RelationCatalog, ICatalog)
    grok.local_utility(PluggableAuthentication, IAuthentication,
                       setup=initialize_auth)
