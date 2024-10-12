from typing import List, Dict
from aiohttp import web

from openapi_server.models.serverless_v1_service_build_build_status import ServerlessV1ServiceBuildBuildStatus
from openapi_server import util


async def fetch_build_status(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_build_status

    Retrieve a specific Build resource.

    :param service_sid: The SID of the Service to fetch the Build resource from.
    :type service_sid: str
    :param sid: The SID of the Build resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)
