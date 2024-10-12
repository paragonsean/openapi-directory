from typing import List, Dict
from aiohttp import web

from openapi_server.models.disable_serial_console_result import DisableSerialConsoleResult
from openapi_server.models.enable_serial_console_result import EnableSerialConsoleResult
from openapi_server.models.get_serial_console_subscription_not_found import GetSerialConsoleSubscriptionNotFound
from openapi_server.models.serial_console_operations import SerialConsoleOperations
from openapi_server.models.serial_console_status import SerialConsoleStatus
from openapi_server import util


async def disable_console(request: web.Request, api_version, subscription_id, default) -> web.Response:
    """Disable Serial Console for a subscription

    Disables the Serial Console service for all VMs and VM scale sets in the provided subscription

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it.
    :type subscription_id: str
    :param default: Default parameter. Leave the value as \&quot;default\&quot;.
    :type default: str

    """
    return web.Response(status=200)


async def enable_console(request: web.Request, api_version, subscription_id, default) -> web.Response:
    """Enable Serial Console for a subscription

    Enables the Serial Console service for all VMs and VM scale sets in the provided subscription

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it.
    :type subscription_id: str
    :param default: Default parameter. Leave the value as \&quot;default\&quot;.
    :type default: str

    """
    return web.Response(status=200)


async def get_console_status(request: web.Request, api_version, subscription_id, default) -> web.Response:
    """Get the disabled status for a subscription

    Gets whether or not Serial Console is disabled for a given subscription

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it.
    :type subscription_id: str
    :param default: Default parameter. Leave the value as \&quot;default\&quot;.
    :type default: str

    """
    return web.Response(status=200)


async def list_operations(request: web.Request, api_version) -> web.Response:
    """list_operations

    Gets a list of Serial Console API operations.

    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)
