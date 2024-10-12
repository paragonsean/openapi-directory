from typing import List, Dict
from aiohttp import web

from openapi_server.models.calculate_sla200_response_inner_inner import CalculateSLA200ResponseInnerInner
from openapi_server.models.calculate_sla_request1 import CalculateSLARequest1
from openapi_server import util


async def calculate_sla(request: web.Request, content_type, accept, body) -> web.Response:
    """Calculate SLA

    Endpoint used by the checkout to calculate the Service Level Agreement (SLA), a contract between the store and shoppers on the order&#39;s fulfillment conditions, such as the shipping estimated date.     The calculation of the estimated date considers the [shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140) and [loading dock](https://help.vtex.com/en/tutorial/loading-dock--5DY8xHEjOLYDVL41Urd5qj) related to the order.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: list | bytes

    """
    body = [CalculateSLARequest1.from_dict(d) for d in body]
    return web.Response(status=200)
