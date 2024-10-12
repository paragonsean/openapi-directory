from typing import List, Dict
from aiohttp import web

from openapi_server.models.campaign_request import CampaignRequest
from openapi_server.models.campaign_response import CampaignResponse
from openapi_server.models.campaigns_remove200_response import CampaignsRemove200Response
from openapi_server.models.campaigns_response import CampaignsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def campaigns_create(request: web.Request, account_id, body=None) -> web.Response:
    """Create campaign

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CampaignRequest.from_dict(body)
    return web.Response(status=200)


async def campaigns_fetch(request: web.Request, account_id, campaign_id) -> web.Response:
    """Fetch campaign by ID

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param campaign_id: ID of campaign to return
    :type campaign_id: str

    """
    return web.Response(status=200)


async def campaigns_fetch_all(request: web.Request, account_id, offset=None, limit=None, name=None) -> web.Response:
    """Fetch campaigns

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param offset: Results to skip when paginating through a result set
    :type offset: int
    :param limit: Maximum number of results to return
    :type limit: int
    :param name: Filter by name or part of
    :type name: str

    """
    return web.Response(status=200)


async def campaigns_remove(request: web.Request, account_id, campaign_id) -> web.Response:
    """Deletes a campaign

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param campaign_id: Campaign id to delete
    :type campaign_id: str

    """
    return web.Response(status=200)


async def campaigns_update(request: web.Request, account_id, campaign_id) -> web.Response:
    """Updates a campaign

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param campaign_id: ID of campaign
    :type campaign_id: str

    """
    return web.Response(status=200)
