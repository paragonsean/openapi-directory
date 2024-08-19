from typing import List, Dict
from aiohttp import web

from openapi_server.models.all_campaigns200_response import AllCampaigns200Response
from openapi_server.models.campaign_details import CampaignDetails
from openapi_server.models.delete_campaign200_response import DeleteCampaign200Response
from openapi_server.models.delete_campaign_event200_response import DeleteCampaignEvent200Response
from openapi_server.models.get_all_campaign_events200_response import GetAllCampaignEvents200Response
from openapi_server.models.get_campaign200_response import GetCampaign200Response
from openapi_server.models.get_events_campaign200_response import GetEventsCampaign200Response
from openapi_server.models.save_campaign200_response import SaveCampaign200Response
from openapi_server.models.save_campaign_event200_response import SaveCampaignEvent200Response
from openapi_server.models.schedule_campaign200_response import ScheduleCampaign200Response
from openapi_server import util


async def all_campaigns(request: web.Request, campaign_type=None, status=None) -> web.Response:
    """Get all campaigns details

    Get all campaigns details

    :param campaign_type: Type of the campaigns we want
    :type campaign_type: str
    :param status: Status of the campaigns we want
    :type status: str

    """
    return web.Response(status=200)


async def delete_campaign(request: web.Request, id) -> web.Response:
    """Delete a campaign

    Delete a campaign

    :param id: Id of the campaign
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def delete_campaign_event(request: web.Request, id) -> web.Response:
    """Delete a campaign event details

    Delete a campaign event details

    :param id: Id of the campaign event
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_all_campaign_events(request: web.Request, campaign_type=None, state=None, campaign_id=None, limit=None, offset=None, before=None, after=None, order=None, asc=None) -> web.Response:
    """Get all campaign events

    Get all campaign events

    :param campaign_type: Type of the campaigns we want
    :type campaign_type: str
    :param state: Status of the campaign events we want
    :type state: str
    :param campaign_id: id of the campaigns we want
    :type campaign_id: str
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


async def get_campaign(request: web.Request, id) -> web.Response:
    """Get a campaign details

    Get a campaign details

    :param id: Id of the campaign
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_campaign_event(request: web.Request, id) -> web.Response:
    """Get a campaign event details

    Get a campaign event details

    :param id: Id of the campaign event
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_events_campaign(request: web.Request, id, campaign_type=None, state=None, limit=None, offset=None, before=None, after=None, order=None, asc=None) -> web.Response:
    """Get campaign events for a campaign

    Get campaign events for a campaign

    :param id: Id of the campaign
    :type id: str
    :type id: str
    :param campaign_type: Type of the campaigns we want
    :type campaign_type: str
    :param state: Status of the campaign events we want
    :type state: str
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


async def save_campaign(request: web.Request, body) -> web.Response:
    """Save a campaign

    Save a campaign details

    :param body: 
    :type body: dict | bytes

    """
    body = CampaignDetails.from_dict(body)
    return web.Response(status=200)


async def save_campaign_event(request: web.Request, id) -> web.Response:
    """Update an existing event

    Update an existing event

    :param id: Id of the campaign event
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def schedule_campaign(request: web.Request, id) -> web.Response:
    """Schedule a campaign event for a campaign

    Schedule a campaign event for a campaign

    :param id: Id of the campaign
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
