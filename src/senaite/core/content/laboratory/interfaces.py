# -*- coding: utf-8 -*-

from zope import schema

from plone.supermodel import model
from plone.app.textfield import RichText

from senaite.core import senaiteMessageFactory as _


class ILaboratory(model.Schema):
    """SENAITE Laboratory
    """
