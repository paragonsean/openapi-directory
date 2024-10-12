from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.marketing_event_complete_request_params import MarketingEventCompleteRequestParams
from openapi_server.models.marketing_event_default_response import MarketingEventDefaultResponse
from openapi_server import util


async def post_marketing_v3_marketing_events_events_external_event_id_complete_complete(request: web.Request, external_event_id, external_account_id, body) -> web.Response:
    """post_marketing_v3_marketing_events_events_external_event_id_complete_complete

    

    :param external_event_id: 
    :type external_event_id: str
    :param external_account_id: 
    :type external_account_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MarketingEventCompleteRequestParams.from_dict(body)
    return web.Response(status=200)
