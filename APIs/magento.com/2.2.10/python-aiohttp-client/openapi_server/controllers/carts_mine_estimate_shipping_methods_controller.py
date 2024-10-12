from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface
from openapi_server.models.quote_shipment_estimation_v1_estimate_by_extended_address_post_request import QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest
from openapi_server import util


async def quote_shipment_estimation_v1_estimate_by_extended_address_post(request: web.Request, body=None) -> web.Response:
    """carts/mine/estimate-shipping-methods

    Estimate shipping by address and return list of available shipping methods

    :param body: 
    :type body: dict | bytes

    """
    body = QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest.from_dict(body)
    return web.Response(status=200)
