from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_organization_webhooks_alert_types_2(request: web.Request, organization_id, product_type=None) -> web.Response:
    """Return a list of alert types to be used with managing webhook alerts

    Return a list of alert types to be used with managing webhook alerts

    :param organization_id: 
    :type organization_id: str
    :param product_type: Filter sample alerts to a specific product type
    :type product_type: str

    """
    return web.Response(status=200)
