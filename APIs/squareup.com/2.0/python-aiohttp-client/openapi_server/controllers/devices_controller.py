from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_device_code_request import CreateDeviceCodeRequest
from openapi_server.models.create_device_code_response import CreateDeviceCodeResponse
from openapi_server.models.get_device_code_response import GetDeviceCodeResponse
from openapi_server.models.list_device_codes_response import ListDeviceCodesResponse
from openapi_server import util


async def create_device_code(request: web.Request, body) -> web.Response:
    """CreateDeviceCode

    Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected terminal mode.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateDeviceCodeRequest.from_dict(body)
    return web.Response(status=200)


async def get_device_code(request: web.Request, id) -> web.Response:
    """GetDeviceCode

    Retrieves DeviceCode with the associated ID.

    :param id: The unique identifier for the device code.
    :type id: str

    """
    return web.Response(status=200)


async def list_device_codes(request: web.Request, cursor=None, location_id=None, product_type=None, status=None) -> web.Response:
    """ListDeviceCodes

    Lists all DeviceCodes associated with the merchant.

    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    :type cursor: str
    :param location_id: If specified, only returns DeviceCodes of the specified location. Returns DeviceCodes of all locations if empty.
    :type location_id: str
    :param product_type: If specified, only returns DeviceCodes targeting the specified product type. Returns DeviceCodes of all product types if empty.
    :type product_type: str
    :param status: If specified, returns DeviceCodes with the specified statuses. Returns DeviceCodes of status &#x60;PAIRED&#x60; and &#x60;UNPAIRED&#x60; if empty.
    :type status: str

    """
    return web.Response(status=200)
