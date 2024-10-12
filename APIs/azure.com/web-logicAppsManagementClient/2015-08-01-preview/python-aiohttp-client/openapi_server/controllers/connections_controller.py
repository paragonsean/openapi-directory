from typing import List, Dict
from aiohttp import web

from openapi_server.models.confirm_consent_code_input import ConfirmConsentCodeInput
from openapi_server.models.connection import Connection
from openapi_server.models.connection_collection import ConnectionCollection
from openapi_server.models.connection_secrets import ConnectionSecrets
from openapi_server.models.consent_link_input import ConsentLinkInput
from openapi_server.models.consent_link_payload import ConsentLinkPayload
from openapi_server.models.list_connection_keys_input import ListConnectionKeysInput
from openapi_server import util


async def connections_confirm_consent_code(request: web.Request, subscription_id, resource_group_name, connection_name, api_version, content) -> web.Response:
    """connections_confirm_consent_code

    Confirms consent code of a connection.

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str
    :param content: The content.
    :type content: dict | bytes

    """
    content = ConfirmConsentCodeInput.from_dict(content)
    return web.Response(status=200)


async def connections_create_or_update(request: web.Request, subscription_id, resource_group_name, connection_name, api_version, connection) -> web.Response:
    """connections_create_or_update

    Creates or updates a connection.

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str
    :param connection: The connection.
    :type connection: dict | bytes

    """
    connection = Connection.from_dict(connection)
    return web.Response(status=200)


async def connections_delete(request: web.Request, subscription_id, resource_group_name, connection_name, api_version) -> web.Response:
    """connections_delete

    Deletes a connection.

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connections_get(request: web.Request, subscription_id, resource_group_name, connection_name, api_version) -> web.Response:
    """connections_get

    Gets a connection.

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connections_list(request: web.Request, resource_group_name, subscription_id, api_version, top=None, filter=None) -> web.Response:
    """Get Connections

    Gets a list of connections.

    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def connections_list_connection_keys(request: web.Request, subscription_id, resource_group_name, connection_name, api_version, content) -> web.Response:
    """connections_list_connection_keys

    Lists connection keys.

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str
    :param content: The content.
    :type content: dict | bytes

    """
    content = ListConnectionKeysInput.from_dict(content)
    return web.Response(status=200)


async def connections_list_consent_links(request: web.Request, subscription_id, resource_group_name, connection_name, api_version, content) -> web.Response:
    """connections_list_consent_links

    Lists consent links of a connection.

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param api_version: API Version
    :type api_version: str
    :param content: The content.
    :type content: dict | bytes

    """
    content = ConsentLinkInput.from_dict(content)
    return web.Response(status=200)
