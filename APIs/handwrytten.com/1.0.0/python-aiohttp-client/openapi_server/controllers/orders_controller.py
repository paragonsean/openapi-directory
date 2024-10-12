from typing import List, Dict
from aiohttp import web

from openapi_server.models.single_step_order200_response import SingleStepOrder200Response
from openapi_server.models.single_step_order_request import SingleStepOrderRequest
from openapi_server import util


async def single_step_order(request: web.Request, body) -> web.Response:
    """sends an order in a single step.  This is much easier than using other order commands

    Sends an order in one step.  No need to create then process order.  Optionally include a gift card.

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = SingleStepOrderRequest.from_dict(body)
    return web.Response(status=200)
