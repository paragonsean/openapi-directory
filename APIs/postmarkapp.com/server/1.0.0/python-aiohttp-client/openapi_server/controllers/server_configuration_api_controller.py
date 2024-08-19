from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit_server_configuration_request import EditServerConfigurationRequest
from openapi_server.models.server_configuration_response import ServerConfigurationResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server import util


async def edit_current_server_configuration(request: web.Request, x_postmark_server_token, body=None) -> web.Response:
    """Edit Server Configuration

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: The settings that should be modified for the current server.
    :type body: dict | bytes

    """
    body = EditServerConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def get_current_server_configuration(request: web.Request, x_postmark_server_token) -> web.Response:
    """Get Server Configuration

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str

    """
    return web.Response(status=200)
