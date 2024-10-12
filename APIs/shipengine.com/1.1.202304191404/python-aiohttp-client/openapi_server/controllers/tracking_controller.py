from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_tracking_log_response_body import GetTrackingLogResponseBody
from openapi_server import util


async def get_tracking_log(request: web.Request, carrier_code=None, tracking_number=None) -> web.Response:
    """Get Tracking Information

    Retrieve package tracking information

    :param carrier_code: Carrier code used to retrieve tracking information
    :type carrier_code: str
    :param tracking_number: The tracking number associated with a shipment
    :type tracking_number: str

    """
    return web.Response(status=200)


async def start_tracking(request: web.Request, carrier_code=None, tracking_number=None) -> web.Response:
    """Start Tracking a Package

    Allows you to subscribe to tracking updates for a package. You specify the carrier_code and tracking_number of the package, and receive notifications via webhooks whenever the shipping status changes. 

    :param carrier_code: Carrier code used to retrieve tracking information
    :type carrier_code: str
    :param tracking_number: The tracking number associated with a shipment
    :type tracking_number: str

    """
    return web.Response(status=200)


async def stop_tracking(request: web.Request, carrier_code=None, tracking_number=None) -> web.Response:
    """Stop Tracking a Package

    Unsubscribe from tracking updates for a package.

    :param carrier_code: Carrier code used to retrieve tracking information
    :type carrier_code: str
    :param tracking_number: The tracking number associated with a shipment
    :type tracking_number: str

    """
    return web.Response(status=200)
