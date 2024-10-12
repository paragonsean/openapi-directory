from typing import List, Dict
from aiohttp import web

from openapi_server.models.hooks_get200_response import HooksGet200Response
from openapi_server.models.hooks_post200_response import HooksPOST200Response
from openapi_server import util


async def hooks_get(request: web.Request, action) -> web.Response:
    """hooks_get

    

    :param action: Determines the action to execute.
    :type action: str

    """
    return web.Response(status=200)


async def hooks_post(request: web.Request, action, id=None, target_url=None, event_type=None, request_method=None) -> web.Response:
    """hooks_post

    

    :param action: Determines the action to execute.
    :type action: str
    :param id: The Webhook ID you wish to unsubscribe.
    :type id: int
    :param target_url: Target URL of your Webhook.
    :type target_url: str
    :param event_type: Type of event for which you would like to receive a webhook.
    :type event_type: str
    :param request_method: Request method in which you want to receive the webhook.
    :type request_method: str

    """
    return web.Response(status=200)
