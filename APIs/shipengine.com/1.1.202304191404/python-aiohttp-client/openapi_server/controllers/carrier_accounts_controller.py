from typing import List, Dict
from aiohttp import web

from openapi_server.models.carrier_name import CarrierName
from openapi_server.models.carrier_name_with_settings import CarrierNameWithSettings
from openapi_server.models.connect_carrier_request_body import ConnectCarrierRequestBody
from openapi_server.models.connect_carrier_response_body import ConnectCarrierResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_carrier_settings_response_body import GetCarrierSettingsResponseBody
from openapi_server.models.update_carrier_settings_request_body import UpdateCarrierSettingsRequestBody
from openapi_server import util


async def connect_carrier(request: web.Request, carrier_name, body) -> web.Response:
    """Connect a carrier account

    Connect a carrier account

    :param carrier_name: The carrier name, such as &#x60;stamps_com&#x60;, &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;.
    :type carrier_name: dict | bytes
    :param body: 
    :type body: dict | bytes

    """
    carrier_name = .from_dict(carrier_name)
    body = ConnectCarrierRequestBody.from_dict(body)
    return web.Response(status=200)


async def disconnect_carrier(request: web.Request, carrier_name, carrier_id) -> web.Response:
    """Disconnect a carrier

    Disconnect a carrier

    :param carrier_name: The carrier name, such as &#x60;stamps_com&#x60;, &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;.
    :type carrier_name: dict | bytes
    :param carrier_id: Carrier ID
    :type carrier_id: str

    """
    carrier_name = .from_dict(carrier_name)
    return web.Response(status=200)


async def get_carrier_settings(request: web.Request, carrier_name, carrier_id) -> web.Response:
    """Get carrier settings

    Get carrier settings

    :param carrier_name: The carrier name, such as &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;.
    :type carrier_name: dict | bytes
    :param carrier_id: Carrier ID
    :type carrier_id: str

    """
    carrier_name = .from_dict(carrier_name)
    return web.Response(status=200)


async def update_carrier_settings(request: web.Request, carrier_name, carrier_id, body) -> web.Response:
    """Update carrier settings

    Update carrier settings

    :param carrier_name: The carrier name, such as &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;.
    :type carrier_name: dict | bytes
    :param carrier_id: Carrier ID
    :type carrier_id: str
    :param body: 
    :type body: dict | bytes

    """
    carrier_name = .from_dict(carrier_name)
    body = UpdateCarrierSettingsRequestBody.from_dict(body)
    return web.Response(status=200)
