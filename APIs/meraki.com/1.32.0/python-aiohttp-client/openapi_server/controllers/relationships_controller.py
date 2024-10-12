from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_device_sensor_relationships200_response_inner import GetDeviceSensorRelationships200ResponseInner
from openapi_server.models.get_network_sensor_relationships200_response_inner import GetNetworkSensorRelationships200ResponseInner
from openapi_server.models.update_device_sensor_relationships_request import UpdateDeviceSensorRelationshipsRequest
from openapi_server import util


async def get_device_sensor_relationships_1(request: web.Request, serial) -> web.Response:
    """List the sensor roles for a given sensor or camera device.

    List the sensor roles for a given sensor or camera device.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_sensor_relationships_1(request: web.Request, network_id) -> web.Response:
    """List the sensor roles for devices in a given network

    List the sensor roles for devices in a given network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_device_sensor_relationships_1(request: web.Request, serial, body=None) -> web.Response:
    """Assign one or more sensor roles to a given sensor or camera device.

    Assign one or more sensor roles to a given sensor or camera device.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSensorRelationshipsRequest.from_dict(body)
    return web.Response(status=200)
