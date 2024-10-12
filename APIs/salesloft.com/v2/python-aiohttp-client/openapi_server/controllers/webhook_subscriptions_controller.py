from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription import Subscription
from openapi_server import util


async def v2_webhook_subscriptions_get(request: web.Request, enabled=None) -> web.Response:
    """List webhook subscriptions

    Fetches all of the customer&#39;s webhook subscriptions for your application.

    :param enabled: Filters webhook subscriptions by whether is enabled or not.
    :type enabled: bool

    """
    return web.Response(status=200)


async def v2_webhook_subscriptions_id_delete(request: web.Request, id) -> web.Response:
    """Delete a webhook subscription

    Deletes a webhook subscription. This operation is not reversible without contacting support. This operation can be called multiple times successfully.

    :param id: The id of the Webhook Subscription to delete
    :type id: int

    """
    return web.Response(status=200)


async def v2_webhook_subscriptions_id_get(request: web.Request, id) -> web.Response:
    """Fetch a webhook subscription

    Fetches a webhook subscription, by ID only.

    :param id: The id for the Webhook Subscription
    :type id: int

    """
    return web.Response(status=200)


async def v2_webhook_subscriptions_id_put(request: web.Request, id, enabled=None) -> web.Response:
    """Update a webhook subscription

    Updates a webhook subscription. Request must be made with a valid Oauth token or API key.

    :param id: The Webhook Suscription id to update
    :type id: int
    :param enabled: Enable or disable the webhook subscription
    :type enabled: bool

    """
    return web.Response(status=200)


async def v2_webhook_subscriptions_post(request: web.Request, callback_token, callback_url, event_type) -> web.Response:
    """Create a webhook subscription

    Creates a webhook subscription. Visit the &lt;a href&#x3D;\&quot;/webhooks.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;webhooks page&lt;/a&gt; for additional details and a list of available webhooks. Request must be made with a valid Oauth token or API key.

    :param callback_token: Any string to be used as a shared secret when subscription events are published. SalesLoft will send the value of this callback_token in the payload of each event so the receiver may verify it matches the original value. This ensures webhook events are being delivered by SalesLoft.
    :type callback_token: str
    :param callback_url: URL for your callback handler
    :type callback_url: str
    :param event_type: Type of event the subscription is for. Visit the \\\&quot;Event Types\\\&quot; section of the webhooks page to find a list of supported event types.
    :type event_type: str

    """
    return web.Response(status=200)
