from typing import List, Dict
from aiohttp import web

from openapi_server.models.time_tracking_configuration import TimeTrackingConfiguration
from openapi_server.models.time_tracking_provider import TimeTrackingProvider
from openapi_server import util


async def get_available_time_tracking_implementations(request: web.Request, ) -> web.Response:
    """Get all time tracking providers

    Returns all time tracking providers. By default, Jira only has one time tracking provider: *JIRA provided time tracking*. However, you can install other time tracking providers via apps from the Atlassian Marketplace. For more information on time tracking providers, see the documentation for the [ Time Tracking Provider](https://developer.atlassian.com/cloud/jira/platform/modules/time-tracking-provider/) module.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).


    """
    return web.Response(status=200)


async def get_selected_time_tracking_implementation(request: web.Request, ) -> web.Response:
    """Get selected time tracking provider

    Returns the time tracking provider that is currently selected. Note that if time tracking is disabled, then a successful but empty response is returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).


    """
    return web.Response(status=200)


async def get_shared_time_tracking_configuration(request: web.Request, ) -> web.Response:
    """Get time tracking settings

    Returns the time tracking settings. This includes settings such as the time format, default time unit, and others. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).


    """
    return web.Response(status=200)


async def select_time_tracking_implementation(request: web.Request, body) -> web.Response:
    """Select time tracking provider

    Selects a time tracking provider.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = TimeTrackingProvider.from_dict(body)
    return web.Response(status=200)


async def set_shared_time_tracking_configuration(request: web.Request, body) -> web.Response:
    """Set time tracking settings

    Sets the time tracking settings.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = TimeTrackingConfiguration.from_dict(body)
    return web.Response(status=200)
