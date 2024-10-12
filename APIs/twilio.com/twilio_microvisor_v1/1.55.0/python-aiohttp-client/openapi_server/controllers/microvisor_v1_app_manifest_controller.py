from typing import List, Dict
from aiohttp import web

from openapi_server.models.microvisor_v1_app_app_manifest import MicrovisorV1AppAppManifest
from openapi_server import util


async def fetch_app_manifest(request: web.Request, app_sid) -> web.Response:
    """fetch_app_manifest

    Retrieve the Manifest for an App.

    :param app_sid: A 34-character string that uniquely identifies this App.
    :type app_sid: str

    """
    return web.Response(status=200)
