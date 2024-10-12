from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def apps_event_authorizations_list(request: web.Request, token, event_context, cursor=None, limit=None) -> web.Response:
    """apps_event_authorizations_list

    Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

    :param token: Authentication token. Requires scope: &#x60;authorizations:read&#x60;
    :type token: str
    :param event_context: 
    :type event_context: str
    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)
