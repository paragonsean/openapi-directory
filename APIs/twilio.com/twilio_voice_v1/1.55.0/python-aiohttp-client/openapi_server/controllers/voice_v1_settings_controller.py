from typing import List, Dict
from aiohttp import web

from openapi_server.models.voice_v1_dialing_permissions_dialing_permissions_settings import VoiceV1DialingPermissionsDialingPermissionsSettings
from openapi_server import util


async def fetch_dialing_permissions_settings(request: web.Request, ) -> web.Response:
    """fetch_dialing_permissions_settings

    Retrieve voice dialing permissions inheritance for the sub-account


    """
    return web.Response(status=200)


async def update_dialing_permissions_settings(request: web.Request, dialing_permissions_inheritance=None) -> web.Response:
    """update_dialing_permissions_settings

    Update voice dialing permissions inheritance for the sub-account

    :param dialing_permissions_inheritance: &#x60;true&#x60; for the sub-account to inherit voice dialing permissions from the Master Project; otherwise &#x60;false&#x60;.
    :type dialing_permissions_inheritance: bool

    """
    return web.Response(status=200)
