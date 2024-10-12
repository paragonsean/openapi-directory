from typing import List, Dict
from aiohttp import web

from openapi_server.models.getcampaignaudiences200_response_inner import Getcampaignaudiences200ResponseInner
from openapi_server.models.getcampaignconfiguration200_response import Getcampaignconfiguration200Response
from openapi_server.models.setcampaignconfiguration200_response import Setcampaignconfiguration200Response
from openapi_server.models.setcampaignconfiguration_request import SetcampaignconfigurationRequest
from openapi_server import util


async def getcampaignaudiences(request: web.Request, content_type, accept) -> web.Response:
    """Get all campaign audiences

    Retrieves a list of all campaign audiences and their respective configurations.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def getcampaignconfiguration(request: web.Request, content_type, accept, campaign_id) -> web.Response:
    """Get campaign audience configuration

    Retrieves a specific campaign audience configuration by its ID. This API uses the campaign ID, not the campaign name.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param campaign_id: Campaign audience unique identifier.
    :type campaign_id: str

    """
    return web.Response(status=200)


async def setcampaignconfiguration(request: web.Request, content_type, accept, body) -> web.Response:
    """Create campaign audience

    Creates a new campaign audience.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SetcampaignconfigurationRequest.from_dict(body)
    return web.Response(status=200)
