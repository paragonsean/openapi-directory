from typing import List, Dict
from aiohttp import web

from openapi_server.models.delivery_prediction_payload import DeliveryPredictionPayload
from openapi_server.models.delivery_prediction_response import DeliveryPredictionResponse
from openapi_server.models.error import Error
from openapi_server import util


async def get_delivery_prediction(request: web.Request, body=None) -> web.Response:
    """Get a delivery prediction for a project

    Get a delivery prediction for a project

    :param body: 
    :type body: dict | bytes

    """
    body = DeliveryPredictionPayload.from_dict(body)
    return web.Response(status=200)
