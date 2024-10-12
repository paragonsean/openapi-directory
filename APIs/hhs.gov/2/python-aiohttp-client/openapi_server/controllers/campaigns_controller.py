from typing import List, Dict
from aiohttp import web

from openapi_server.models.campaign_wrapped import CampaignWrapped
from openapi_server.models.media_item_wrapped import MediaItemWrapped
from openapi_server.models.syndicate_marshaller_wrapped import SyndicateMarshallerWrapped
from openapi_server import util


async def resources_campaigns_id_json_get(request: web.Request, id) -> web.Response:
    """Get Campaign by ID

    Information about a specific campaign

    :param id: The id of the record to look up
    :type id: int

    """
    return web.Response(status=200)


async def resources_campaigns_id_media_json_get(request: web.Request, id, sort=None, max=None, offset=None) -> web.Response:
    """Get MediaItems by Campaign ID

    Campaign Listings

    :param id: The id of the campaign to find media items for
    :type id: int
    :param sort: The name of the property to which sorting will be applied
    :type sort: str
    :param max: The maximum number of records to return
    :type max: int
    :param offset: The offset of the records set to return for pagination
    :type offset: int

    """
    return web.Response(status=200)


async def resources_campaigns_id_syndicate_format_get(request: web.Request, id, format, display_method=None) -> web.Response:
    """Get MediaItems for Campaign

    MediaItem

    :param id: The id of the record to look up
    :type id: int
    :param format: Automatically added
    :type format: str
    :param display_method: Method used to render an html request. Accepts one: [mv, list, feed]
    :type display_method: str

    """
    return web.Response(status=200)


async def resources_campaigns_json_get(request: web.Request, max=None, offset=None, sort=None) -> web.Response:
    """Get Campaigns

    Media Listings for a specific campaign

    :param max: The maximum number of records to return
    :type max: int
    :param offset: The offset of the records set to return for pagination
    :type offset: int
    :param sort: * Set of fields to sort the records by.
    :type sort: str

    """
    return web.Response(status=200)
