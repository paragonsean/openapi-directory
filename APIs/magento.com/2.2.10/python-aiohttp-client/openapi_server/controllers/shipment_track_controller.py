from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_shipment_track_interface import SalesDataShipmentTrackInterface
from openapi_server.models.sales_shipment_track_repository_v1_save_post_request import SalesShipmentTrackRepositoryV1SavePostRequest
from openapi_server import util


async def sales_shipment_track_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """shipment/track

    Performs persist operations for a specified shipment track.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesShipmentTrackRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
