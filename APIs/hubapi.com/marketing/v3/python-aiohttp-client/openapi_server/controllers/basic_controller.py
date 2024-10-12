from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.marketing_event_create_request_params import MarketingEventCreateRequestParams
from openapi_server.models.marketing_event_default_response import MarketingEventDefaultResponse
from openapi_server.models.marketing_event_public_default_response import MarketingEventPublicDefaultResponse
from openapi_server.models.marketing_event_public_read_response import MarketingEventPublicReadResponse
from openapi_server.models.marketing_event_update_request_params import MarketingEventUpdateRequestParams
from openapi_server import util


async def delete_marketing_v3_marketing_events_events_external_event_id_archive(request: web.Request, external_event_id, external_account_id) -> web.Response:
    """Delete a marketing event

    Deletes an existing Marketing Event with the specified id, if one exists.

    :param external_event_id: The id of the marketing event to delete
    :type external_event_id: str
    :param external_account_id: The account id associated with the marketing event
    :type external_account_id: str

    """
    return web.Response(status=200)


async def get_marketing_v3_marketing_events_events_external_event_id_get_by_id(request: web.Request, external_event_id, external_account_id) -> web.Response:
    """Get a marketing event

    Returns the details of the Marketing Event with the specified id, if one exists.

    :param external_event_id: The id of the marketing event to return
    :type external_event_id: str
    :param external_account_id: The account id associated with the marketing event
    :type external_account_id: str

    """
    return web.Response(status=200)


async def patch_marketing_v3_marketing_events_events_external_event_id_update(request: web.Request, external_event_id, external_account_id, body) -> web.Response:
    """Update a marketing event

    Updates an existing Marketing Event with the specified id, if one exists.

    :param external_event_id: The id of the marketing event to update
    :type external_event_id: str
    :param external_account_id: The account id associated with the marketing event
    :type external_account_id: str
    :param body: The details of the marketing event to update
    :type body: dict | bytes

    """
    body = MarketingEventUpdateRequestParams.from_dict(body)
    return web.Response(status=200)


async def post_marketing_v3_marketing_events_events_create(request: web.Request, body) -> web.Response:
    """Create a marketing event

    Creates a new marketing event in HubSpot

    :param body: The details of the marketing event to create
    :type body: dict | bytes

    """
    body = MarketingEventCreateRequestParams.from_dict(body)
    return web.Response(status=200)


async def post_marketing_v3_marketing_events_events_external_event_id_cancel_do_cancel(request: web.Request, external_event_id, external_account_id) -> web.Response:
    """Mark a marketing event as cancelled

    Mark a marketing event as cancelled.

    :param external_event_id: The id of the marketing event to mark as cancelled
    :type external_event_id: str
    :param external_account_id: The account id associated with the marketing event
    :type external_account_id: str

    """
    return web.Response(status=200)


async def put_marketing_v3_marketing_events_events_external_event_id_replace(request: web.Request, external_event_id, body) -> web.Response:
    """Create or update a marketing event

    Upsets a Marketing Event. If there is an existing Marketing event with the specified id, it will be updated; otherwise a new event will be created.

    :param external_event_id: The id of the marketing event to upsert
    :type external_event_id: str
    :param body: The details of the marketing event to upsert
    :type body: dict | bytes

    """
    body = MarketingEventCreateRequestParams.from_dict(body)
    return web.Response(status=200)
