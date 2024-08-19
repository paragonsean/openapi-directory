from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_campaign_event_result200_response import GetCampaignEventResult200Response
from openapi_server.models.get_campaign_event_result_for_node200_response import GetCampaignEventResultForNode200Response
from openapi_server.models.get_campaign_history200_response import GetCampaignHistory200Response
from openapi_server import util


async def get_campaign_event_result(request: web.Request, id) -> web.Response:
    """Get a campaign event result

    Get a campaign event result

    :param id: Id of the campaign event
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_campaign_event_result_for_node(request: web.Request, id, node_id) -> web.Response:
    """Get detailed campaign event result for a Node

    Get detailed campaign event result for a Node

    :param id: Id of the campaign event
    :type id: str
    :type id: str
    :param node_id: Id of the target node
    :type node_id: str

    """
    return web.Response(status=200)


async def get_campaign_history(request: web.Request, id, limit=None, offset=None, before=None, after=None, order=None, asc=None) -> web.Response:
    """Get a campaign result history

    Get a campaign result history

    :param id: Id of the campaign
    :type id: str
    :type id: str
    :param limit: Max number of elements in response
    :type limit: int
    :param offset: Offset of data in response (skip X elements)
    :type offset: int
    :param before: 
    :type before: str
    :param after: 
    :type after: str
    :param order: 
    :type order: str
    :param asc: 
    :type asc: str

    """
    before = util.deserialize_date(before)
    after = util.deserialize_date(after)
    return web.Response(status=200)
