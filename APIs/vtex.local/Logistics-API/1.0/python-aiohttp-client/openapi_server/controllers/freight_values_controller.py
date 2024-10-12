from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_update_freight_values_request import CreateUpdateFreightValuesRequest
from openapi_server.models.freight_values200_response_inner import FreightValues200ResponseInner
from openapi_server import util


async def create_update_freight_values(request: web.Request, content_type, accept, carrier_id, body) -> web.Response:
    """Create/update freight values

    Creates or updates the freight values of your store&#39;s carriers. Learn more in [Shipping rate template](https://help.vtex.com/en/tutorial/planilha-de-frete--tutorials_127#).

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param carrier_id: 
    :type carrier_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [CreateUpdateFreightValuesRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def freight_values(request: web.Request, content_type, accept, carrier_id, cep) -> web.Response:
    """List freight values

    Lists freight values apointed to your store&#39;s carriers, searching by carrier ID and postal code (&#x60;cep&#x60;).

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param carrier_id: Carrier ID
    :type carrier_id: str
    :param cep: Postal code.
    :type cep: str

    """
    return web.Response(status=200)
