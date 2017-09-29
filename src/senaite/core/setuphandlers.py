# -*- coding: utf-8 -*-

from zope import component

from plone.portlets.interfaces import IPortletType

from senaite.core import logger


def setupHandler(context):
    """SENAITE CORE setup handler
    """

    if context.readDataFile('senaite.lcore.txt') is None:
        return

    logger.info("SENAITE CORE setup handler [BEGIN]")

    portal = context.getSite()  # noqa

    # Run Installers
    logger.info("SENAITE CORE setup handler [DONE]")
