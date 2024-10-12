from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_create_request import DeviceCreateRequest
from openapi_server.models.device_response import DeviceResponse
from openapi_server.models.device_update_request import DeviceUpdateRequest
from openapi_server.models.devices_response import DevicesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def devices_create_instance(request: web.Request, body) -> web.Response:
    """devices_create_instance

    

    :param body: Device representation
    :type body: dict | bytes

    """
    body = DeviceCreateRequest.from_dict(body)
    return web.Response(status=200)


async def devices_get_collection(request: web.Request, filter_name=None, filter_platform=None, filter_status=None, filter_udid=None, filter_id=None, sort=None, fields_devices=None, limit=None) -> web.Response:
    """devices_get_collection

    

    :param filter_name: filter by attribute &#39;name&#39;
    :type filter_name: List[str]
    :param filter_platform: filter by attribute &#39;platform&#39;
    :type filter_platform: List[str]
    :param filter_status: filter by attribute &#39;status&#39;
    :type filter_status: List[str]
    :param filter_udid: filter by attribute &#39;udid&#39;
    :type filter_udid: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_devices: the fields to include for returned resources of type devices
    :type fields_devices: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def devices_get_instance(request: web.Request, id, fields_devices=None) -> web.Response:
    """devices_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_devices: the fields to include for returned resources of type devices
    :type fields_devices: List[str]

    """
    return web.Response(status=200)


async def devices_update_instance(request: web.Request, id, body) -> web.Response:
    """devices_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: Device representation
    :type body: dict | bytes

    """
    body = DeviceUpdateRequest.from_dict(body)
    return web.Response(status=200)
