from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_webhook import AutopilotV1AssistantWebhook
from openapi_server.models.list_webhook_response import ListWebhookResponse
from openapi_server import util


async def create_webhook(request: web.Request, assistant_sid, events, unique_name, webhook_url, webhook_method=None) -> web.Response:
    """create_webhook

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource.
    :type assistant_sid: str
    :param events: The list of space-separated events that this Webhook will subscribe to.
    :type events: str
    :param unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. This value must be unique and 64 characters or less in length.
    :type unique_name: str
    :param webhook_url: The URL associated with this Webhook.
    :type webhook_url: str
    :param webhook_method: The method to be used when calling the webhook&#39;s URL.
    :type webhook_method: str

    """
    return web.Response(status=200)


async def delete_webhook(request: web.Request, assistant_sid, sid) -> web.Response:
    """delete_webhook

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_webhook(request: web.Request, assistant_sid, sid) -> web.Response:
    """fetch_webhook

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_webhook(request: web.Request, assistant_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_webhook

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
    :type assistant_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_webhook(request: web.Request, assistant_sid, sid, events=None, unique_name=None, webhook_method=None, webhook_url=None) -> web.Response:
    """update_webhook

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
    :type sid: str
    :param events: The list of space-separated events that this Webhook will subscribe to.
    :type events: str
    :param unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. This value must be unique and 64 characters or less in length.
    :type unique_name: str
    :param webhook_method: The method to be used when calling the webhook&#39;s URL.
    :type webhook_method: str
    :param webhook_url: The URL associated with this Webhook.
    :type webhook_url: str

    """
    return web.Response(status=200)
