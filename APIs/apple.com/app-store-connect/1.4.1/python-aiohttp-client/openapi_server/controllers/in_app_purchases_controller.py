from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.in_app_purchase_response import InAppPurchaseResponse
from openapi_server import util


async def in_app_purchases_get_instance(request: web.Request, id, fields_in_app_purchases=None, include=None, limit_apps=None) -> web.Response:
    """in_app_purchases_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_in_app_purchases: the fields to include for returned resources of type inAppPurchases
    :type fields_in_app_purchases: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param limit_apps: maximum number of related apps returned (when they are included)
    :type limit_apps: int

    """
    return web.Response(status=200)
