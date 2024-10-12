from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_webhook_request import CreateWebhookRequest
from openapi_server.models.create_webhook_response import CreateWebhookResponse
from openapi_server.models.get_webhook_response import GetWebhookResponse
from openapi_server.models.list_webhook_delivery_logs_response import ListWebhookDeliveryLogsResponse
from openapi_server.models.list_webhooks_response import ListWebhooksResponse
from openapi_server.models.webhook_event_callback import WebhookEventCallback
from openapi_server import util


async def webhooks_get(request: web.Request, page_size=None) -> web.Response:
    """List webhooks

    Retrieve a list of configured webhooks. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered oldest first to newest last. 

    :param page_size: The number of records to return in each page. 
    :type page_size: int

    """
    return web.Response(status=200)


async def webhooks_id_delete(request: web.Request, id) -> web.Response:
    """Delete webhook

    Delete a specific webhook by providing its unique identifier. Once deleted, webhook events will no longer be sent to the configured URL. 

    :param id: The unique identifier for the webhook. 
    :type id: str

    """
    return web.Response(status=200)


async def webhooks_id_get(request: web.Request, id) -> web.Response:
    """Retrieve webhook

    Retrieve a specific webhook by providing its unique identifier. 

    :param id: The unique identifier for the webhook. 
    :type id: str

    """
    return web.Response(status=200)


async def webhooks_post(request: web.Request, body=None) -> web.Response:
    """Create webhook

    Create a new webhook with a given URL. The URL will receive webhook events as JSON-encoded &#x60;POST&#x60; requests. The URL must respond with a HTTP &#x60;200&#x60; status on success.  There is currently a limit of 10 webhooks at any given time. Once this limit is reached, existing webhooks will need to be deleted before new webhooks can be created.  Event delivery is retried with exponential backoff if the URL is unreachable or it does not respond with a &#x60;200&#x60; status. The response includes a &#x60;secretKey&#x60; attribute, which is used to sign requests sent to the webhook URL. It will not be returned from any other endpoints within the Up API. If the &#x60;secretKey&#x60; is lost, simply create a new webhook with the same URL, capture its &#x60;secretKey&#x60; and then delete the original webhook. See [Handling webhook events](#callback_post_webhookURL) for details on how to process webhook events.  It is probably a good idea to test the webhook by [sending it a &#x60;PING&#x60; event](#post_webhooks_webhookId_ping) after creating it. 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def webhooks_webhook_id_logs_get(request: web.Request, webhook_id, page_size=None) -> web.Response:
    """List webhook logs

    Retrieve a list of delivery logs for a webhook by providing its unique identifier. This is useful for analysis and debugging purposes. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered newest first to oldest last. Logs may be automatically purged after a period of time. 

    :param webhook_id: The unique identifier for the webhook. 
    :type webhook_id: str
    :param page_size: The number of records to return in each page. 
    :type page_size: int

    """
    return web.Response(status=200)


async def webhooks_webhook_id_ping_post(request: web.Request, webhook_id) -> web.Response:
    """Ping webhook

    Send a &#x60;PING&#x60; event to a webhook by providing its unique identifier. This is useful for testing and debugging purposes. The event is delivered asynchronously and its data is returned in the response to this request. 

    :param webhook_id: The unique identifier for the webhook. 
    :type webhook_id: str

    """
    return web.Response(status=200)
