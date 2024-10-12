from typing import List, Dict
from aiohttp import web

from openapi_server.models.offering_response import OfferingResponse
from openapi_server import util


async def get_event_offers(request: web.Request, event_id, x_ssl_cert_uid=None, x_tm_access_token=None, access_token=None, api_key=None, body=None) -> web.Response:
    """Event Offers

    Returns Event Offers.

    :param event_id: Event Identifier
    :type event_id: str
    :param x_ssl_cert_uid: API Key for external API developer
    :type x_ssl_cert_uid: str
    :param x_tm_access_token: Access token for
    :type x_tm_access_token: str
    :param access_token: Query Param Access Token
    :type access_token: str
    :param api_key: Query Param API Key for external API developer
    :type api_key: str
    :param body: displayId to un-hide protected offers
    :type body: str

    """
    return web.Response(status=200)
