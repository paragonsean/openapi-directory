from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_campaign_request import CreateCampaignRequest
from openapi_server.models.create_campaign_response import CreateCampaignResponse
from openapi_server.models.create_segment_request import CreateSegmentRequest
from openapi_server.models.create_segment_response import CreateSegmentResponse
from openapi_server.models.delete_campaign_response import DeleteCampaignResponse
from openapi_server.models.delete_segment_response import DeleteSegmentResponse
from openapi_server.models.query_campaigns_request import QueryCampaignsRequest
from openapi_server.models.query_campaigns_response import QueryCampaignsResponse
from openapi_server.models.query_recipients_request import QueryRecipientsRequest
from openapi_server.models.query_recipients_response import QueryRecipientsResponse
from openapi_server.models.query_segments_request import QuerySegmentsRequest
from openapi_server.models.query_segments_response import QuerySegmentsResponse
from openapi_server.models.resume_campaign_response import ResumeCampaignResponse
from openapi_server.models.schedule_campaign_request import ScheduleCampaignRequest
from openapi_server.models.schedule_campaign_response import ScheduleCampaignResponse
from openapi_server.models.stop_campaign_response import StopCampaignResponse
from openapi_server.models.test_campaign_request import TestCampaignRequest
from openapi_server.models.test_campaign_response import TestCampaignResponse
from openapi_server.models.update_campaign_request import UpdateCampaignRequest
from openapi_server.models.update_campaign_response import UpdateCampaignResponse
from openapi_server.models.update_segment_request import UpdateSegmentRequest
from openapi_server.models.update_segment_response import UpdateSegmentResponse
from openapi_server import util


async def create_campaign(request: web.Request, body) -> web.Response:
    """Create campaign

    Creates a new campaign 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateCampaignRequest.from_dict(body)
    return web.Response(status=200)


async def create_segment(request: web.Request, body) -> web.Response:
    """Create segment

    Create a segment 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateSegmentRequest.from_dict(body)
    return web.Response(status=200)


async def delete_campaign(request: web.Request, id, recipients=None) -> web.Response:
    """Delete campaign

    Delete a campaign 

    :param id: 
    :type id: str
    :param recipients: 
    :type recipients: bool

    """
    return web.Response(status=200)


async def delete_segment(request: web.Request, id) -> web.Response:
    """Delete segment

    Delete a segment 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def query_campaigns(request: web.Request, payload=None) -> web.Response:
    """Query campaigns

    Query campaigns 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def query_recipients(request: web.Request, payload=None) -> web.Response:
    """Query recipients

    Query recipients 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def query_segments(request: web.Request, payload=None) -> web.Response:
    """Query segments

    Query segments 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def resume_campaign(request: web.Request, id) -> web.Response:
    """Resume campaign

    Resume a stopped campaign 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def schedule_campaign(request: web.Request, id, body) -> web.Response:
    """Schedule campaign

    Schedule a campaign 

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScheduleCampaignRequest.from_dict(body)
    return web.Response(status=200)


async def stop_campaign(request: web.Request, id) -> web.Response:
    """Stop campaign

    Stop a running campaign 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def test_campaign(request: web.Request, id, body) -> web.Response:
    """Test campaign

    Test a campaign 

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TestCampaignRequest.from_dict(body)
    return web.Response(status=200)


async def update_campaign(request: web.Request, id, body) -> web.Response:
    """Update campaign

    Update an existing campaign 

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCampaignRequest.from_dict(body)
    return web.Response(status=200)


async def update_segment(request: web.Request, id, body) -> web.Response:
    """Update segment

    Update an existing segment 

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSegmentRequest.from_dict(body)
    return web.Response(status=200)
