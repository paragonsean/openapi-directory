from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.not_found import NotFound
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhooks_create_payload import WebhooksCreatePayload
from openapi_server.models.webhooks_list_response import WebhooksListResponse
from openapi_server import util


async def d_elete_webhook(request: web.Request, webhook_id) -> web.Response:
    """Delete a Webhook

    This endpoint will delete the indicated webhook.

    :param webhook_id: The webhook you wish to delete.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def g_et_webhook(request: web.Request, webhook_id) -> web.Response:
    """Show Webhook details

    This call provides the same JSON information provided on Webjhook creation.

    :param webhook_id: The unique webhook you wish to retreive details on.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def l_ist_webhooks(request: web.Request, events=None, current_page=None, page_size=None) -> web.Response:
    """List all webhooks

    Requests to this endpoint return a list of your webhooks (with all their details). You can filter what the webhook list that the API returns using the parameters described below.

    :param events: The webhook event that you wish to filter on.
    :type events: str
    :param current_page: Choose the number of search results to return per page. Minimum value: 1
    :type current_page: int
    :param page_size: Results per page. Allowed values 1-100, default is 25.
    :type page_size: int

    """
    return web.Response(status=200)


async def p_ost_webhooks(request: web.Request, body=None) -> web.Response:
    """Create Webhook

    Webhooks can push notifications to your server, rather than polling api.video for changes. We currently offer four events:  * &#x60;&#x60;&#x60;video.encoding.quality.completed&#x60;&#x60;&#x60;  When a new video is uploaded into your account, it will be encoded into several different HLS sizes/bitrates.  When each version is encoded, your webhook will get a notification.  It will look like &#x60;&#x60;&#x60;{ \\\&quot;type\\\&quot;: \\\&quot;video.encoding.quality.completed\\\&quot;, \\\&quot;emittedAt\\\&quot;: \\\&quot;2021-01-29T16:46:25.217+01:00\\\&quot;, \\\&quot;videoId\\\&quot;: \\\&quot;viXXXXXXXX\\\&quot;, \\\&quot;encoding\\\&quot;: \\\&quot;hls\\\&quot;, \\\&quot;quality\\\&quot;: \\\&quot;720p\\\&quot;} &#x60;&#x60;&#x60;. This request says that the 720p HLS encoding was completed. * &#x60;&#x60;&#x60;live-stream.broadcast.started&#x60;&#x60;&#x60;  When a livestream begins broadcasting, the broadcasting parameter changes from false to true, and this webhook fires. * &#x60;&#x60;&#x60;live-stream.broadcast.ended&#x60;&#x60;&#x60;  This event fores when the livestream has finished broadcasting, and the broadcasting parameter flips from false to true. * &#x60;&#x60;&#x60;video.source.recorded&#x60;&#x60;&#x60;  This event is similar to &#x60;&#x60;&#x60;video.encoding.quality.completed&#x60;&#x60;&#x60;, but tells you if a livestream has been recorded as a VOD.

    :param body: 
    :type body: dict | bytes

    """
    body = WebhooksCreatePayload.from_dict(body)
    return web.Response(status=200)
