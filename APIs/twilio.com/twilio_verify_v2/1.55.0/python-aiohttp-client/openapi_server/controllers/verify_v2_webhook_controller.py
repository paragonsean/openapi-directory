from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_webhook_response import ListWebhookResponse
from openapi_server.models.verify_v2_service_webhook import VerifyV2ServiceWebhook
from openapi_server.models.webhook_enum_status import WebhookEnumStatus
from openapi_server.models.webhook_enum_version import WebhookEnumVersion
from openapi_server import util


async def create_webhook(request: web.Request, service_sid, event_types, friendly_name, webhook_url, status=None, version=None) -> web.Response:
    """create_webhook

    Create a new Webhook for the Service

    :param service_sid: The unique SID identifier of the Service.
    :type service_sid: str
    :param event_types: The array of events that this Webhook is subscribed to. Possible event types: &#x60;*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied&#x60;
    :type event_types: List[str]
    :param friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
    :type friendly_name: str
    :param webhook_url: The URL associated with this Webhook.
    :type webhook_url: str
    :param status: 
    :type status: str
    :param version: 
    :type version: str

    """
    return web.Response(status=200)


async def delete_webhook(request: web.Request, service_sid, sid) -> web.Response:
    """delete_webhook

    Delete a specific Webhook.

    :param service_sid: The unique SID identifier of the Service.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_webhook(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_webhook

    Fetch a specific Webhook.

    :param service_sid: The unique SID identifier of the Service.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_webhook(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_webhook

    Retrieve a list of all Webhooks for a Service.

    :param service_sid: The unique SID identifier of the Service.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_webhook(request: web.Request, service_sid, sid, event_types=None, friendly_name=None, status=None, version=None, webhook_url=None) -> web.Response:
    """update_webhook

    

    :param service_sid: The unique SID identifier of the Service.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
    :type sid: str
    :param event_types: The array of events that this Webhook is subscribed to. Possible event types: &#x60;*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied&#x60;
    :type event_types: List[str]
    :param friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
    :type friendly_name: str
    :param status: 
    :type status: str
    :param version: 
    :type version: str
    :param webhook_url: The URL associated with this Webhook.
    :type webhook_url: str

    """
    return web.Response(status=200)
