from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_external_campaign import MessagingV1ExternalCampaign
from openapi_server import util


async def create_external_campaign(request: web.Request, campaign_id, messaging_service_sid) -> web.Response:
    """create_external_campaign

    

    :param campaign_id: ID of the preregistered campaign.
    :type campaign_id: str
    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) that the resource is associated with.
    :type messaging_service_sid: str

    """
    return web.Response(status=200)
