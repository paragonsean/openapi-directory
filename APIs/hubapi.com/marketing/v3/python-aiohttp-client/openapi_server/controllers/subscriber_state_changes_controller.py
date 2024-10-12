from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_input_marketing_event_email_subscriber import BatchInputMarketingEventEmailSubscriber
from openapi_server.models.batch_input_marketing_event_subscriber import BatchInputMarketingEventSubscriber
from openapi_server.models.error import Error
from openapi_server import util


async def post_marketing_v3_marketing_events_events_external_event_id_subscriber_state_email_upsert_do_email_upsert_by_id(request: web.Request, external_event_id, subscriber_state, external_account_id, body) -> web.Response:
    """Record

    Record a subscription state between multiple HubSpot contacts and a marketing event, using contact email addresses. Note that the contact must already exist in HubSpot; a contact will not be created.

    :param external_event_id: The id of the marketing event
    :type external_event_id: str
    :param subscriber_state: The new subscriber state for the HubSpot contacts and the specified marketing event
    :type subscriber_state: str
    :param external_account_id: The account id associated with the marketing event
    :type external_account_id: str
    :param body: The details of the contacts to subscribe to the event
    :type body: dict | bytes

    """
    body = BatchInputMarketingEventEmailSubscriber.from_dict(body)
    return web.Response(status=200)


async def post_marketing_v3_marketing_events_events_external_event_id_subscriber_state_upsert_do_upsert_by_id(request: web.Request, external_event_id, subscriber_state, external_account_id, body) -> web.Response:
    """Record

    Record a subscription state between multiple HubSpot contacts and a marketing event, using HubSpot contact ids. Note that the contact must already exist in HubSpot; a contact will not be create.

    :param external_event_id: The id of the marketing event
    :type external_event_id: str
    :param subscriber_state: The new subscriber state for the HubSpot contacts and the specified marketing event
    :type subscriber_state: str
    :param external_account_id: The account id associated with the marketing event
    :type external_account_id: str
    :param body: The details of the contacts to subscribe to the event
    :type body: dict | bytes

    """
    body = BatchInputMarketingEventSubscriber.from_dict(body)
    return web.Response(status=200)
