from typing import List, Dict
from aiohttp import web

from openapi_server.models.source_control import SourceControl
from openapi_server.models.source_control_collection import SourceControlCollection
from openapi_server.models.user import User
from openapi_server import util


async def provider_get_publishing_user(request: web.Request, api_version) -> web.Response:
    """Gets publishing user

    

    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def provider_get_source_control(request: web.Request, source_control_type, api_version) -> web.Response:
    """Gets source control token

    

    :param source_control_type: Type of source control
    :type source_control_type: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def provider_get_source_controls(request: web.Request, api_version) -> web.Response:
    """Gets the source controls available for Azure websites

    

    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def provider_update_publishing_user(request: web.Request, api_version, request_message) -> web.Response:
    """Updates publishing user

    

    :param api_version: API Version
    :type api_version: str
    :param request_message: Details of publishing user
    :type request_message: dict | bytes

    """
    request_message = User.from_dict(request_message)
    return web.Response(status=200)


async def provider_update_source_control(request: web.Request, source_control_type, api_version, request_message) -> web.Response:
    """Updates source control token

    

    :param source_control_type: Type of source control
    :type source_control_type: str
    :param api_version: API Version
    :type api_version: str
    :param request_message: Source control token information
    :type request_message: dict | bytes

    """
    request_message = SourceControl.from_dict(request_message)
    return web.Response(status=200)
