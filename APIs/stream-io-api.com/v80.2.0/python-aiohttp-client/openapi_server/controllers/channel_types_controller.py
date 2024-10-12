from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_channel_type_request import CreateChannelTypeRequest
from openapi_server.models.create_channel_type_response import CreateChannelTypeResponse
from openapi_server.models.list_channel_types_response import ListChannelTypesResponse
from openapi_server.models.response import Response
from openapi_server.models.update_channel_type_request import UpdateChannelTypeRequest
from openapi_server.models.update_channel_type_response import UpdateChannelTypeResponse
from openapi_server import util


async def create_channel_type_0(request: web.Request, body) -> web.Response:
    """Create channel type

    Creates new channel type 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateChannelTypeRequest.from_dict(body)
    return web.Response(status=200)


async def delete_channel_type_0(request: web.Request, name) -> web.Response:
    """Delete channel type

    Deletes channel type 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_channel_type_0(request: web.Request, name) -> web.Response:
    """Get channel type

    Gets channel type 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def list_channel_types_0(request: web.Request, ) -> web.Response:
    """List channel types

    Lists all available channel types 


    """
    return web.Response(status=200)


async def update_channel_type_0(request: web.Request, name, body) -> web.Response:
    """Update channel type

    Updates channel type 

    :param name: 
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateChannelTypeRequest.from_dict(body)
    return web.Response(status=200)
