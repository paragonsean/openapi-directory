from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.item_list_webhook_resource import ItemListWebhookResource
from openapi_server.models.resource_id import ResourceId
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_page import WebhookPage
from openapi_server.models.webhook_resource import WebhookResource
from openapi_server import util


async def create_webhook(request: web.Request, body=None) -> web.Response:
    """Create a webhook

    Create a Webhook for notification in the CallFire system. Use the webhooks API to receive notifications of important CallFire events. Select the resource to listen to, and then choose the resource events to receive notifications on. When an event triggers, a POST will be made to the callback URL with a payload of notification information. Available resources and their events include &#39;CccCampaign&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;CallBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;TextBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;OutboundCall&#39;: [&#39;finished&#39;], &#39;InboundCall&#39;: [&#39;finished&#39;], &#39;OutboundText&#39;: [&#39;finished&#39;], &#39;InboundText&#39;: [&#39;finished&#39;], &#39;ContactList&#39;: [&#39;validationFinished&#39;, &#39;validationFailed&#39;], &#39;MonthlyRenewal&#39;: [&#39;failed&#39;, &#39;finished&#39;], &#39;LowBalance&#39;: [&#39;failed&#39;, &#39;finished&#39;]. Webhooks support secret token which is used as signing key to HmacSHA1 hash of json payload which is returned in &#39;X-CallFire-Signature&#39; header. This header can be used to verify callback POST is coming from CallFire. See [security guide](https://developers.callfire.com/security-guide.html)

    :param body: A webhook object
    :type body: dict | bytes

    """
    body = Webhook.from_dict(body)
    return web.Response(status=200)


async def delete_webhook(request: web.Request, id) -> web.Response:
    """Delete a webhook

    Deletes a webhook instance. Will be removed permanently

    :param id: An Id of a webhook
    :type id: int

    """
    return web.Response(status=200)


async def find_webhook_resources(request: web.Request, fields=None) -> web.Response:
    """Find webhook resources

    Searches for webhook resources. Available resources include &#39;CccCampaign&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;CallBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;TextBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;OutboundCall&#39;: [&#39;finished&#39;], &#39;InboundCall&#39;: [&#39;finished&#39;], &#39;OutboundText&#39;: [&#39;finished&#39;], &#39;InboundText&#39;: [&#39;finished&#39;], &#39;ContactList&#39;: [&#39;validationFinished&#39;, &#39;validationFailed&#39;], &#39;MonthlyRenewal&#39;: [&#39;failed&#39;, &#39;finished&#39;], &#39;LowBalance&#39;: [&#39;failed&#39;, &#39;finished&#39;]

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def find_webhooks(request: web.Request, fields=None, limit=None, offset=None, name=None, resource=None, event=None, param_callback=None, enabled=None) -> web.Response:
    """Find webhooks

    Searches all webhooks available for a current user. Searches by name, resource, event, callback URL, or whether they are enabled. Returns a paged list of Webhooks

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param name: A name of a webhook
    :type name: str
    :param resource: A name of a resource, available values: &#39;CccCampaign&#39;, &#39;CallBroadcast&#39;, &#39;TextBroadcast&#39;,  &#39;OutboundCall&#39;, &#39;OutboundText&#39;, &#39;InboundCall&#39;, &#39;InboundText&#39;, &#39;ContactList&#39;
    :type resource: str
    :param event: A name of event, available values: &#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;
    :type event: str
    :param param_callback: A callback URL
    :type param_callback: str
    :param enabled: Specifies whether webhook is enabled
    :type enabled: bool

    """
    return web.Response(status=200)


async def get_webhook(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific webhook

    Returns a single Webhook instance for a given webhook id

    :param id: An id of a webhook
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_webhook_resource(request: web.Request, resource, fields=None) -> web.Response:
    """Find specific webhook resource

    Returns information about supported events for a given webhook resource

    :param resource: A name of a webhook resource. Available resources include &#39;CccCampaign&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;CallBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;TextBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;OutboundCall&#39;: [&#39;finished&#39;], &#39;InboundCall&#39;: [&#39;finished&#39;], &#39;OutboundText&#39;: [&#39;finished&#39;], &#39;InboundText&#39;: [&#39;finished&#39;], &#39;ContactList&#39;: [&#39;validationFinished&#39;, &#39;validationFailed&#39;], &#39;MonthlyRenewal&#39;: [&#39;failed&#39;, &#39;finished&#39;], &#39;LowBalance&#39;: [&#39;failed&#39;, &#39;finished&#39;]
    :type resource: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def update_webhook(request: web.Request, id, body=None) -> web.Response:
    """Update a webhook

    Updates the information in existing webhook

    :param id: An id of a webhook
    :type id: int
    :param body: A webhook object
    :type body: dict | bytes

    """
    body = Webhook.from_dict(body)
    return web.Response(status=200)
