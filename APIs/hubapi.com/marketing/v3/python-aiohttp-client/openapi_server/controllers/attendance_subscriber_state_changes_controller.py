from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_input_marketing_event_email_subscriber import BatchInputMarketingEventEmailSubscriber
from openapi_server.models.batch_input_marketing_event_subscriber import BatchInputMarketingEventSubscriber
from openapi_server.models.batch_response_subscriber_email_response import BatchResponseSubscriberEmailResponse
from openapi_server.models.batch_response_subscriber_vid_response import BatchResponseSubscriberVidResponse
from openapi_server.models.error import Error
from openapi_server import util


async def post_marketing_v3_marketing_events_attendance_external_event_id_subscriber_state_create_create(request: web.Request, external_event_id, subscriber_state, body, external_account_id=None) -> web.Response:
    """Record

    Record a subscription state between multiple HubSpot contacts and a marketing event, using HubSpot contact ids.

    :param external_event_id: The id of the marketing event
    :type external_event_id: str
    :param subscriber_state: The new subscriber state for the HubSpot contacts and the specified marketing event. For example: &#39;register&#39;, &#39;attend&#39; or &#39;cancel&#39;.
    :type subscriber_state: str
    :param body: The details of the contacts to subscribe to the event. Parameters of join and left time if state is Attended.
    :type body: dict | bytes
    :param external_account_id: The account id associated with the marketing event
    :type external_account_id: str

    """
    body = BatchInputMarketingEventSubscriber.from_dict(body)
    return web.Response(status=200)


async def post_marketing_v3_marketing_events_attendance_external_event_id_subscriber_state_email_create_create_by_email(request: web.Request, external_event_id, subscriber_state, body, external_account_id=None) -> web.Response:
    """Record

    Record a subscription state between multiple HubSpot contacts and a marketing event, using contact email addresses. If contact is not present it will be automatically created.

    :param external_event_id: The id of the marketing event
    :type external_event_id: str
    :param subscriber_state: The new subscriber state for the HubSpot contacts and the specified marketing event. For example: &#39;register&#39;, &#39;attend&#39; or &#39;cancel&#39;.
    :type subscriber_state: str
    :param body: The details of the contacts to subscribe to the event. Parameters of join and left time if state is Attended.
    :type body: dict | bytes
    :param external_account_id: The account id associated with the marketing event
    :type external_account_id: str

    """
    body = BatchInputMarketingEventEmailSubscriber.from_dict(body)
    return web.Response(status=200)
