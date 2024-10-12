from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.integration_account_session import IntegrationAccountSession
from openapi_server.models.integration_account_session_list_result import IntegrationAccountSessionListResult
from openapi_server import util


async def sessions_create_or_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, session_name, api_version, session) -> web.Response:
    """sessions_create_or_update

    Creates or updates an integration account session.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param session_name: The integration account session name.
    :type session_name: str
    :param api_version: The API version.
    :type api_version: str
    :param session: The integration account session.
    :type session: dict | bytes

    """
    session = IntegrationAccountSession.from_dict(session)
    return web.Response(status=200)


async def sessions_delete(request: web.Request, subscription_id, resource_group_name, integration_account_name, session_name, api_version) -> web.Response:
    """sessions_delete

    Deletes an integration account session.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param session_name: The integration account session name.
    :type session_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def sessions_get(request: web.Request, subscription_id, resource_group_name, integration_account_name, session_name, api_version) -> web.Response:
    """sessions_get

    Gets an integration account session.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param session_name: The integration account session name.
    :type session_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def sessions_list_by_integration_accounts(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, top=None, filter=None) -> web.Response:
    """sessions_list_by_integration_accounts

    Gets a list of integration account sessions.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation. Options for filters include: ChangedTime.
    :type filter: str

    """
    return web.Response(status=200)
