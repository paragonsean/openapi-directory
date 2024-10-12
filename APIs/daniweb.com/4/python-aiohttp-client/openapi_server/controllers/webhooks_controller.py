from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_delete_webhooks_id import EndpointDeleteWebhooksID
from openapi_server.models.endpoint_get_webhooks import EndpointGetWebhooks
from openapi_server.models.endpoint_post_webhooks import EndpointPostWebhooks
from openapi_server import util


async def webhooks_get(request: web.Request, ) -> web.Response:
    """webhooks_get

    Fetch a listing of all webhooks owned by the current user/bubble combination.


    """
    return web.Response(status=200)


async def webhooks_iddelete(request: web.Request, id) -> web.Response:
    """webhooks_iddelete

    Delete a webhook that was previously registered by the current user/bubble combination.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def webhooks_post(request: web.Request, event, name, uri, bubbled=None, object_id=None) -> web.Response:
    """webhooks_post

    Register a new webhook for the current user/bubble combination. Specify an object_id to only be notified on an event related to that specific Conversation ID, Group ID, or User ID. Your access token must have access to the user being tracked, user you are in the conversation with, or user who created the group. You must be connected with a user in order to keep track of their online status. Alternatively, do not specify an object_id to be notified on all events that are related to conversations you&#39;re in, groups you&#39;re a member of, or users you are in conversations with. You may only have one webhook for each object_id/event. The webhook URI must reside on your own server. Webhooks do not expire when the access token used to create them expires. However, they will temporarily cease to function if the user who created them deauthorizes access to the application (effectively no longer existing within the bubble), unless/until the user reauthorizes the application using OAuth.

    :param event: 
    :type event: str
    :param name: 
    :type name: str
    :param uri: 
    :type uri: str
    :param bubbled: 
    :type bubbled: bool
    :param object_id: 
    :type object_id: int

    """
    return web.Response(status=200)
