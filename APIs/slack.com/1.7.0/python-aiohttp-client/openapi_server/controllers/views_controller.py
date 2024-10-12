from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def views_open(request: web.Request, token, trigger_id, view) -> web.Response:
    """views_open

    Open a view for a user.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param trigger_id: Exchange a trigger to post to the user.
    :type trigger_id: str
    :param view: A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.
    :type view: str

    """
    return web.Response(status=200)


async def views_publish(request: web.Request, token, user_id, view, hash=None) -> web.Response:
    """views_publish

    Publish a static view for a User.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param user_id: &#x60;id&#x60; of the user you want publish a view to.
    :type user_id: str
    :param view: A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.
    :type view: str
    :param hash: A string that represents view state to protect against possible race conditions.
    :type hash: str

    """
    return web.Response(status=200)


async def views_push(request: web.Request, token, trigger_id, view) -> web.Response:
    """views_push

    Push a view onto the stack of a root view.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param trigger_id: Exchange a trigger to post to the user.
    :type trigger_id: str
    :param view: A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.
    :type view: str

    """
    return web.Response(status=200)


async def views_update(request: web.Request, token, view_id=None, external_id=None, view=None, hash=None) -> web.Response:
    """views_update

    Update an existing view.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param view_id: A unique identifier of the view to be updated. Either &#x60;view_id&#x60; or &#x60;external_id&#x60; is required.
    :type view_id: str
    :param external_id: A unique identifier of the view set by the developer. Must be unique for all views on a team. Max length of 255 characters. Either &#x60;view_id&#x60; or &#x60;external_id&#x60; is required.
    :type external_id: str
    :param view: A [view object](/reference/surfaces/views). This must be a JSON-encoded string.
    :type view: str
    :param hash: A string that represents view state to protect against possible race conditions.
    :type hash: str

    """
    return web.Response(status=200)
