# -*- coding: utf-8 -*-

from zope.interface import implements

from plone.dexterity.content import Container

from .interfaces import ILaboratory


class Laboratory(Container):
    """SENAITE Laboratory
    """
    implements(ILaboratory)
