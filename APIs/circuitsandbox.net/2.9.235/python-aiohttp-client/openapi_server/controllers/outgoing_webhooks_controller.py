from typing import List, Dict
from aiohttp import web

from openapi_server.models.web_hook import WebHook
from openapi_server import util


async def add_presence_web_hook(request: web.Request, url, user_ids) -> web.Response:
    """Registers Presence WebHook registration

    Registers a webHook that has a presence filter with the given URL and userIds. There is a maximum number of userIds allowed OauthScopes: READ_USER

    :param url: WebHook callback URL
    :type url: str
    :param user_ids: The IDs of the users to subscribe for their presence
    :type user_ids: List[str]

    """
    return web.Response(status=200)


async def add_web_hook(request: web.Request, filter, url) -> web.Response:
    """Registers a WebHook

    Registers the webHook with the given filter and callback URL. OauthScopes: READ_CONVERSATIONS, READ_USER

    :param filter: A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE
    :type filter: List[str]
    :param url: WebHook callback URL
    :type url: str

    """
    return web.Response(status=200)


async def get_web_hook(request: web.Request, ) -> web.Response:
    """Gets a list of webHooks

    Gets the list of webHooks registered for this user or API. OauthScopes: READ_CONVERSATIONS, READ_USER


    """
    return web.Response(status=200)


async def get_web_hook_by_id(request: web.Request, id) -> web.Response:
    """Gets a webHook

    Gets the registered webHook with the given ID. OauthScopes: READ_CONVERSATIONS, READ_USER

    :param id: The unique ID of the webHook to fetch
    :type id: str

    """
    return web.Response(status=200)


async def remove_web_hook(request: web.Request, id) -> web.Response:
    """Removes a registered webHook

    Unregisters the webHook with the given ID. OauthScopes: READ_CONVERSATIONS, READ_USER

    :param id: The unique ID of the webHook to remove
    :type id: str

    """
    return web.Response(status=200)


async def remove_web_hooks(request: web.Request, ) -> web.Response:
    """Removes all webHooks

    Unregisters all webHooks of the authenticated user OauthScopes: READ_CONVERSATIONS, READ_USER


    """
    return web.Response(status=200)


async def update_presence_web_hook(request: web.Request, id, url=None, user_ids=None) -> web.Response:
    """Updates a Presence WebHook registration

    Updates a registration of a webHook that has a presence filter. The update can be performed either on the URL and/or the userIds. The new userIds, if any, will override any existing userIds. OauthScopes: READ_USER

    :param id: The unique ID of the webHook to update
    :type id: str
    :param url: WebHook callback URL
    :type url: str
    :param user_ids: The IDs of the users to subscribe for their presence
    :type user_ids: List[str]

    """
    return web.Response(status=200)


async def update_web_hook(request: web.Request, id, filter=None, url=None) -> web.Response:
    """Updates a WebHook registration

    Updates a webHook registration with the given filter and callback URL. OauthScopes: READ_CONVERSATIONS, READ_USER

    :param id: The unique ID of the webHook to update
    :type id: str
    :param filter: A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE
    :type filter: List[str]
    :param url: WebHook callback URL
    :type url: str

    """
    return web.Response(status=200)
