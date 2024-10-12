from typing import List, Dict
from aiohttp import web

from openapi_server.models.security_contact import SecurityContact
from openapi_server.models.security_contact_list import SecurityContactList
from openapi_server.models.security_contacts_list_default_response import SecurityContactsListDefaultResponse
from openapi_server import util


async def security_contacts_create(request: web.Request, api_version, subscription_id, security_contact_name, security_contact) -> web.Response:
    """security_contacts_create

    Security contact configurations for the subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param security_contact_name: Name of the security contact object
    :type security_contact_name: str
    :param security_contact: Security contact object
    :type security_contact: dict | bytes

    """
    security_contact = SecurityContact.from_dict(security_contact)
    return web.Response(status=200)


async def security_contacts_delete(request: web.Request, api_version, subscription_id, security_contact_name) -> web.Response:
    """security_contacts_delete

    Security contact configurations for the subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param security_contact_name: Name of the security contact object
    :type security_contact_name: str

    """
    return web.Response(status=200)


async def security_contacts_get(request: web.Request, api_version, subscription_id, security_contact_name) -> web.Response:
    """security_contacts_get

    Security contact configurations for the subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param security_contact_name: Name of the security contact object
    :type security_contact_name: str

    """
    return web.Response(status=200)


async def security_contacts_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """security_contacts_list

    Security contact configurations for the subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)


async def security_contacts_update(request: web.Request, api_version, subscription_id, security_contact_name, security_contact) -> web.Response:
    """security_contacts_update

    Security contact configurations for the subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param security_contact_name: Name of the security contact object
    :type security_contact_name: str
    :param security_contact: Security contact object
    :type security_contact: dict | bytes

    """
    security_contact = SecurityContact.from_dict(security_contact)
    return web.Response(status=200)
