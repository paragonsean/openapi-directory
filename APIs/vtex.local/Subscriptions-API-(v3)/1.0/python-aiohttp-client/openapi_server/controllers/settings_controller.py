from typing import List, Dict
from aiohttp import web

from openapi_server.models.settings import Settings
from openapi_server import util


async def edit_settings(request: web.Request, content_type, accept, body) -> web.Response:
    """Edit Subscriptions settings

    Edits Subscriptions settings in your store.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: Request body
    :type body: dict | bytes

    """
    body = Settings.from_dict(body)
    return web.Response(status=200)


async def get_settings(request: web.Request, content_type, accept) -> web.Response:
    """Get Subscription Settings

    List the details of the settings of a given subscription.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)
