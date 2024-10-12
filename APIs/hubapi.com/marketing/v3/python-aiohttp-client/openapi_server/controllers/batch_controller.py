from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_input_marketing_event_create_request_params import BatchInputMarketingEventCreateRequestParams
from openapi_server.models.batch_input_marketing_event_external_unique_identifier import BatchInputMarketingEventExternalUniqueIdentifier
from openapi_server.models.batch_response_marketing_event_public_default_response import BatchResponseMarketingEventPublicDefaultResponse
from openapi_server.models.error import Error
from openapi_server import util


async def post_marketing_v3_marketing_events_events_delete_archive(request: web.Request, body) -> web.Response:
    """Delete multiple marketing events

    Bulk delete a number of marketing events in HubSpot

    :param body: The details of the marketing events to delete
    :type body: dict | bytes

    """
    body = BatchInputMarketingEventExternalUniqueIdentifier.from_dict(body)
    return web.Response(status=200)


async def post_marketing_v3_marketing_events_events_upsert_do_upsert(request: web.Request, body) -> web.Response:
    """Create or update multiple marketing events

    Upset multiple Marketing Event. If there is an existing Marketing event with the specified id, it will be updated; otherwise a new event will be created.

    :param body: The details of the marketing events to upsert
    :type body: dict | bytes

    """
    body = BatchInputMarketingEventCreateRequestParams.from_dict(body)
    return web.Response(status=200)
