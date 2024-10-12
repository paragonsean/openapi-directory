from typing import List, Dict
from aiohttp import web

from openapi_server.models.ldap_service_info import LdapServiceInfo
from openapi_server.models.ldap_service_info_update import LdapServiceInfoUpdate
from openapi_server.models.ldap_service_summary import LdapServiceSummary
from openapi_server.models.ldap_service_summary_list_response import LdapServiceSummaryListResponse
from openapi_server import util


async def create_ldap_service(request: web.Request, body) -> web.Response:
    """Add a new authentication domain

    Add a new authentication domain.

    :param body: Information for joining an authentication domain.
    :type body: dict | bytes

    """
    body = LdapServiceInfo.from_dict(body)
    return web.Response(status=200)


async def delete_ldap_service(request: web.Request, id) -> web.Response:
    """Delete an authentication domain for the given ID

    Delete an authentication domain for the given ID.

    :param id: ID of the authentication domain to be deleted.
    :type id: str

    """
    return web.Response(status=200)


async def get_ldap_service(request: web.Request, id) -> web.Response:
    """Get a LDAP service for the given ID

    Get a LDAP service for the given ID.

    :param id: ID of the authentication domain to be retrieved.
    :type id: str

    """
    return web.Response(status=200)


async def patch_ldap_service(request: web.Request, id, body) -> web.Response:
    """Update an existing authentication domain

    Modify the values of a specified authentication domain object.

    :param id: ID of the authentication domain to be updated.
    :type id: str
    :param body: Information for updating an authentication domain.
    :type body: dict | bytes

    """
    body = LdapServiceInfoUpdate.from_dict(body)
    return web.Response(status=200)


async def put_ldap_service(request: web.Request, id, body) -> web.Response:
    """Replace the values of an authentication domain

    Replace the values of a specified authentication domain object.

    :param id: ID of the authentication domain to be updated.
    :type id: str
    :param body: Information for updating an authentication domain.
    :type body: dict | bytes

    """
    body = LdapServiceInfoUpdate.from_dict(body)
    return web.Response(status=200)


async def query_ldap_service(request: web.Request, ) -> web.Response:
    """Get a list of LDAP services

    Get a list of LDAP services.


    """
    return web.Response(status=200)
