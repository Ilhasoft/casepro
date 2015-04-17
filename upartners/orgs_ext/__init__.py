from __future__ import absolute_import, unicode_literals


from dash.orgs.models import Org


ORG_CONFIG_CONTACT_FIELDS = 'contact_fields'


def _org_get_contact_fields(org):
    return org.get_config(ORG_CONFIG_CONTACT_FIELDS)


def _org_set_contact_fields(org, fields):
    org.set_config(ORG_CONFIG_CONTACT_FIELDS, fields)


Org.get_contact_fields = _org_get_contact_fields
Org.set_contact_fields = _org_set_contact_fields
