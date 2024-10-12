from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_available_locales200_response import GetAvailableLocales200Response
from openapi_server.models.get_common_settings200_response import GetCommonSettings200Response
from openapi_server.models.get_global_alerts200_response import GetGlobalAlerts200Response
from openapi_server.models.get_user_system_overrides200_response import GetUserSystemOverrides200Response
from openapi_server import util


async def get_available_locales(request: web.Request, ) -> web.Response:
    """get_available_locales

    List of available localization cultures


    """
    return web.Response(status=200)


async def get_common_settings(request: web.Request, ) -> web.Response:
    """get_common_settings

    Get the common settings used by the Bungie.Net environment.


    """
    return web.Response(status=200)


async def get_global_alerts(request: web.Request, includestreaming=None) -> web.Response:
    """get_global_alerts

    Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

    :param includestreaming: Determines whether Streaming Alerts are included in results
    :type includestreaming: bool

    """
    return web.Response(status=200)


async def get_user_system_overrides(request: web.Request, ) -> web.Response:
    """get_user_system_overrides

    Get the user-specific system overrides that should be respected alongside common systems.


    """
    return web.Response(status=200)
