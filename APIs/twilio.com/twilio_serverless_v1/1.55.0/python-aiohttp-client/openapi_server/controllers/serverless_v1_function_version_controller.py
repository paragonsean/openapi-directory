from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_function_version_response import ListFunctionVersionResponse
from openapi_server.models.serverless_v1_service_function_function_version import ServerlessV1ServiceFunctionFunctionVersion
from openapi_server import util


async def fetch_function_version(request: web.Request, service_sid, function_sid, sid) -> web.Response:
    """fetch_function_version

    Retrieve a specific Function Version resource.

    :param service_sid: The SID of the Service to fetch the Function Version resource from.
    :type service_sid: str
    :param function_sid: The SID of the function that is the parent of the Function Version resource to fetch.
    :type function_sid: str
    :param sid: The SID of the Function Version resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_function_version(request: web.Request, service_sid, function_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_function_version

    Retrieve a list of all Function Version resources.

    :param service_sid: The SID of the Service to read the Function Version resources from.
    :type service_sid: str
    :param function_sid: The SID of the function that is the parent of the Function Version resources to read.
    :type function_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
