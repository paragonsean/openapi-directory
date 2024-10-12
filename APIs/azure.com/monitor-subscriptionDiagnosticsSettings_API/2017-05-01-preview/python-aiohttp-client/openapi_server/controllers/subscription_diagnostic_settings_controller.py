from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.subscription_diagnostic_settings_resource import SubscriptionDiagnosticSettingsResource
from openapi_server.models.subscription_diagnostic_settings_resource_collection import SubscriptionDiagnosticSettingsResourceCollection
from openapi_server import util


async def subscription_diagnostic_settings_create_or_update(request: web.Request, subscription_id, api_version, name, parameters) -> web.Response:
    """subscription_diagnostic_settings_create_or_update

    Creates or updates subscription diagnostic settings for the specified resource.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param name: The name of the diagnostic setting.
    :type name: str
    :param parameters: Parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = SubscriptionDiagnosticSettingsResource.from_dict(parameters)
    return web.Response(status=200)


async def subscription_diagnostic_settings_delete(request: web.Request, subscription_id, api_version, name) -> web.Response:
    """subscription_diagnostic_settings_delete

    Deletes existing subscription diagnostic settings for the specified resource.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param name: The name of the diagnostic setting.
    :type name: str

    """
    return web.Response(status=200)


async def subscription_diagnostic_settings_get(request: web.Request, subscription_id, api_version, name) -> web.Response:
    """subscription_diagnostic_settings_get

    Gets the active subscription diagnostic settings for the specified resource.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param name: The name of the diagnostic setting.
    :type name: str

    """
    return web.Response(status=200)


async def subscription_diagnostic_settings_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """subscription_diagnostic_settings_list

    Gets the active subscription diagnostic settings list for the specified subscriptionId.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
