from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_rate import BulkRate
from openapi_server.models.calculate_rates_request_body import CalculateRatesRequestBody
from openapi_server.models.calculate_rates_response_body import CalculateRatesResponseBody
from openapi_server.models.compare_bulk_rates_request_body import CompareBulkRatesRequestBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.estimate_rates_request_body import EstimateRatesRequestBody
from openapi_server.models.get_rate_by_id_response_body import GetRateByIdResponseBody
from openapi_server.models.rate_estimate import RateEstimate
from openapi_server import util


async def calculate_rates(request: web.Request, body) -> web.Response:
    """Get Shipping Rates

    It&#39;s not uncommon that you want to give your customer the choice between whether they want to ship the fastest, cheapest, or the most trusted route. Most companies don&#39;t solely ship things using a single shipping option; so we provide functionality to show you all your options! 

    :param body: 
    :type body: dict | bytes

    """
    body = CalculateRatesRequestBody.from_dict(body)
    return web.Response(status=200)


async def compare_bulk_rates(request: web.Request, body) -> web.Response:
    """Get Bulk Rates

    Get Bulk Shipment Rates

    :param body: 
    :type body: dict | bytes

    """
    body = CompareBulkRatesRequestBody.from_dict(body)
    return web.Response(status=200)


async def estimate_rates(request: web.Request, body) -> web.Response:
    """Estimate Rates

    Get Rate Estimates

    :param body: 
    :type body: dict | bytes

    """
    body = EstimateRatesRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_rate_by_id(request: web.Request, rate_id) -> web.Response:
    """Get Rate By ID

    Retrieve a previously queried rate by its ID

    :param rate_id: Rate ID
    :type rate_id: str

    """
    return web.Response(status=200)
