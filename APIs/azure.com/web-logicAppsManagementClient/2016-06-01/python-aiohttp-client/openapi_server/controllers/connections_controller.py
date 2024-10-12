from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_connection_definition import ApiConnectionDefinition
from openapi_server.models.api_connection_definition_collection import ApiConnectionDefinitionCollection
from openapi_server.models.confirm_consent_code_definition import ConfirmConsentCodeDefinition
from openapi_server.models.consent_link_collection import ConsentLinkCollection
from openapi_server.models.list_consent_links_definition import ListConsentLinksDefinition
from openapi_server import util


async def connections_confirm_consent_code(request: web.Request, subscription_id, resource_group_name, connection_name, api_version, confirm_consent_code) -> web.Response:
    """Confirms the consent code for a connection

    Confirms consent code of a connection

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_name: Connection name
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str
    :param confirm_consent_code: The consent code confirmation
    :type confirm_consent_code: dict | bytes

    """
    confirm_consent_code = ConfirmConsentCodeDefinition.from_dict(confirm_consent_code)
    return web.Response(status=200)


async def connections_create_or_update(request: web.Request, subscription_id, resource_group_name, connection_name, api_version, connection) -> web.Response:
    """Replace an existing connection

    Creates or updates a connection

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_name: Connection name
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str
    :param connection: The connection
    :type connection: dict | bytes

    """
    connection = ApiConnectionDefinition.from_dict(connection)
    return web.Response(status=200)


async def connections_delete(request: web.Request, subscription_id, resource_group_name, connection_name, api_version) -> web.Response:
    """Delete an existing connection

    Deletes a connection

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_name: Connection name
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connections_get(request: web.Request, subscription_id, resource_group_name, connection_name, api_version) -> web.Response:
    """Get a connection

    Get a specific connection

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_name: Connection name
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connections_list(request: web.Request, subscription_id, resource_group_name, api_version, top=None, filter=None) -> web.Response:
    """Get all connections

    Gets a list of connections

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param api_version: API Version
    :type api_version: str
    :param top: The number of items to be included in the result
    :type top: int
    :param filter: The filter to apply on the operation
    :type filter: str

    """
    return web.Response(status=200)


async def connections_list_consent_links(request: web.Request, subscription_id, resource_group_name, connection_name, api_version, list_consent_link) -> web.Response:
    """Lists consent links for a connection

    Lists the consent links of a connection

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_name: Connection name
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str
    :param list_consent_link: The consent links
    :type list_consent_link: dict | bytes

    """
    list_consent_link = ListConsentLinksDefinition.from_dict(list_consent_link)
    return web.Response(status=200)


async def connections_update(request: web.Request, subscription_id, resource_group_name, connection_name, api_version, connection) -> web.Response:
    """Update an existing connection

    Updates a connection&#39;s tags

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_name: Connection name
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str
    :param connection: The connection
    :type connection: dict | bytes

    """
    connection = ApiConnectionDefinition.from_dict(connection)
    return web.Response(status=200)
