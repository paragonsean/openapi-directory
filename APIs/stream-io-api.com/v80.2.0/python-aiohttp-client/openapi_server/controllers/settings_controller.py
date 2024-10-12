from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.check_push_request import CheckPushRequest
from openapi_server.models.check_push_response import CheckPushResponse
from openapi_server.models.check_sqs_request import CheckSQSRequest
from openapi_server.models.check_sqs_response import CheckSQSResponse
from openapi_server.models.create_block_list_request import CreateBlockListRequest
from openapi_server.models.create_channel_type_request import CreateChannelTypeRequest
from openapi_server.models.create_channel_type_response import CreateChannelTypeResponse
from openapi_server.models.get_application_response import GetApplicationResponse
from openapi_server.models.get_block_list_response import GetBlockListResponse
from openapi_server.models.get_rate_limits_response import GetRateLimitsResponse
from openapi_server.models.list_block_list_response import ListBlockListResponse
from openapi_server.models.list_channel_types_response import ListChannelTypesResponse
from openapi_server.models.list_push_providers_response import ListPushProvidersResponse
from openapi_server.models.response import Response
from openapi_server.models.update_app_request import UpdateAppRequest
from openapi_server.models.update_block_list_request import UpdateBlockListRequest
from openapi_server.models.update_channel_type_request import UpdateChannelTypeRequest
from openapi_server.models.update_channel_type_response import UpdateChannelTypeResponse
from openapi_server.models.upsert_push_provider_request import UpsertPushProviderRequest
from openapi_server.models.upsert_push_provider_response import UpsertPushProviderResponse
from openapi_server import util


async def check_push(request: web.Request, body) -> web.Response:
    """Check push

    Sends a test message via push, this is a test endpoint to verify your push settings 

    :param body: 
    :type body: dict | bytes

    """
    body = CheckPushRequest.from_dict(body)
    return web.Response(status=200)


async def check_sqs(request: web.Request, body) -> web.Response:
    """Check SQS

    Validates Amazon SQS credentials 

    :param body: 
    :type body: dict | bytes

    """
    body = CheckSQSRequest.from_dict(body)
    return web.Response(status=200)


async def create_block_list(request: web.Request, body) -> web.Response:
    """Create block list

    Creates a new application blocklist, once created the blocklist can be used by any channel type 

    :param body: Block list
    :type body: dict | bytes

    """
    body = CreateBlockListRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel_type(request: web.Request, body) -> web.Response:
    """Create channel type

    Creates new channel type 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateChannelTypeRequest.from_dict(body)
    return web.Response(status=200)


async def delete_block_list(request: web.Request, name) -> web.Response:
    """Delete block list

    Deletes previously created application blocklist 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def delete_channel_type(request: web.Request, name) -> web.Response:
    """Delete channel type

    Deletes channel type 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def delete_push_provider_0(request: web.Request, type, name) -> web.Response:
    """Delete a push provider

    Delete a push provider from v2 with multi bundle/package support. v1 isn&#39;t supported in this endpoint 

    :param type: 
    :type type: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_app(request: web.Request, ) -> web.Response:
    """Get App Settings

    This method returns the application settings 


    """
    return web.Response(status=200)


async def get_block_list(request: web.Request, name) -> web.Response:
    """Get block list

    Returns block list by given name 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_channel_type(request: web.Request, name) -> web.Response:
    """Get channel type

    Gets channel type 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_rate_limits(request: web.Request, server_side=None, android=None, ios=None, web=None, endpoints=None) -> web.Response:
    """Get rate limits

    Get rate limits usage and quotas 

    :param server_side: 
    :type server_side: bool
    :param android: 
    :type android: bool
    :param ios: 
    :type ios: bool
    :param web: 
    :type web: bool
    :param endpoints: 
    :type endpoints: str

    """
    return web.Response(status=200)


async def list_block_lists(request: web.Request, ) -> web.Response:
    """List block lists

    Returns all available block lists 


    """
    return web.Response(status=200)


async def list_channel_types(request: web.Request, ) -> web.Response:
    """List channel types

    Lists all available channel types 


    """
    return web.Response(status=200)


async def list_push_providers_0(request: web.Request, ) -> web.Response:
    """List push providers

    List details of all push providers. 


    """
    return web.Response(status=200)


async def update_app(request: web.Request, body) -> web.Response:
    """Update App Settings

    This method updates one or more application settings 

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAppRequest.from_dict(body)
    return web.Response(status=200)


async def update_block_list(request: web.Request, name, body) -> web.Response:
    """Update block list

    Updates contents of the block list 

    :param name: 
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateBlockListRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel_type(request: web.Request, name, body) -> web.Response:
    """Update channel type

    Updates channel type 

    :param name: 
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateChannelTypeRequest.from_dict(body)
    return web.Response(status=200)


async def upsert_push_provider_0(request: web.Request, body) -> web.Response:
    """Upsert a push provider

    Upsert a push provider for v2 with multi bundle/package support 

    :param body: 
    :type body: dict | bytes

    """
    body = UpsertPushProviderRequest.from_dict(body)
    return web.Response(status=200)
