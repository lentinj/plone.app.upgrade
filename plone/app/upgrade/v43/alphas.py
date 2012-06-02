import logging
from plone.app.upgrade.utils import loadMigrationProfile
from Products.PlonePAS.Extensions.Install import setupPasswordPolicyPlugin
from Products.CMFCore.utils import getToolByName

logger = logging.getLogger('plone.app.upgrade')


def to43alpha1(context):
    """4.2 -> 4.3alpha1
    """
    loadMigrationProfile(context, 'profile-plone.app.upgrade.v43:to43alpha1')


def to43alpha1_password_validation(context):
    """Add the default password validation plugin to acl_users
    """

    p = 'Portlets: View dashboard'
    portal = getToolByName(context, 'portal_url').getPortalObject()
    setupPasswordPolicyPlugin(portal)
