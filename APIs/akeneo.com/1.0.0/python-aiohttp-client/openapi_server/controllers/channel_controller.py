from typing import List, Dict
from aiohttp import web

from openapi_server.models.channels import Channels
from openapi_server.models.channels_post_request import ChannelsPostRequest
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.several_channels_patch_request import SeveralChannelsPatchRequest
from openapi_server import util


async def channels_patch(request: web.Request, code, body) -> web.Response:
    """Update/create a channel

    This endpoint allows you to update a given channel. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no channel exists for the given code, it creates it.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChannelsPostRequest.from_dict(body)
    return web.Response(status=200)


async def channels_post(request: web.Request, body=None) -> web.Response:
    """Create a new channel

    This endpoint allows you to create a new channel.

    :param body: 
    :type body: dict | bytes

    """
    body = ChannelsPostRequest.from_dict(body)
    return web.Response(status=200)


async def get_channels(request: web.Request, page=None, limit=None, with_count=None) -> web.Response:
    """Get a list of channels

    This endpoint allows you to get a list of channels. Channels are paginated and sorted by code.

    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)


async def get_channels_code(request: web.Request, code) -> web.Response:
    """Get a channel

    This endpoint allows you to get the information about a given channel.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def several_channels_patch(request: web.Request, body=None) -> web.Response:
    """Update/create several channels

    This endpoint allows you to update and/or create several channels at once.

    :param body: 
    :type body: dict | bytes

    """
    body = SeveralChannelsPatchRequest.from_dict(body)
    return web.Response(status=200)
