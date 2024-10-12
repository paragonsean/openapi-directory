from typing import List, Dict
from aiohttp import web

from openapi_server.models.serverless_v1_service_function_function_version_function_version_content import ServerlessV1ServiceFunctionFunctionVersionFunctionVersionContent
from openapi_server import util


async def fetch_function_version_content(request: web.Request, service_sid, function_sid, sid) -> web.Response:
    """fetch_function_version_content

    Retrieve a the content of a specific Function Version resource.

    :param service_sid: The SID of the Service to fetch the Function Version content from.
    :type service_sid: str
    :param function_sid: The SID of the Function that is the parent of the Function Version content to fetch.
    :type function_sid: str
    :param sid: The SID of the Function Version content to fetch.
    :type sid: str

    """
    return web.Response(status=200)
