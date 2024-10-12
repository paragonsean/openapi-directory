from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_order import CertificateOrder
from openapi_server.models.certificate_order_collection import CertificateOrderCollection
from openapi_server import util


async def global_certificate_order_get_all_certificate_orders(request: web.Request, subscription_id, api_version) -> web.Response:
    """Lists all domains in a subscription

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_certificate_order_validate_certificate_purchase_information(request: web.Request, subscription_id, api_version, certificate_order) -> web.Response:
    """Validate certificate purchase information

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param certificate_order: Certificate order
    :type certificate_order: dict | bytes

    """
    certificate_order = CertificateOrder.from_dict(certificate_order)
    return web.Response(status=200)
