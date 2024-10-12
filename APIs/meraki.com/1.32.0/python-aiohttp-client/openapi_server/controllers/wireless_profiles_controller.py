from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_camera_wireless_profile_request import CreateNetworkCameraWirelessProfileRequest
from openapi_server.models.update_device_camera_wireless_profiles_request import UpdateDeviceCameraWirelessProfilesRequest
from openapi_server.models.update_network_camera_wireless_profile_request import UpdateNetworkCameraWirelessProfileRequest
from openapi_server import util


async def create_network_camera_wireless_profile_1(request: web.Request, network_id, body) -> web.Response:
    """Creates a new camera wireless profile for this network.

    Creates a new camera wireless profile for this network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkCameraWirelessProfileRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_camera_wireless_profile_1(request: web.Request, network_id, wireless_profile_id) -> web.Response:
    """Delete an existing camera wireless profile for this network.

    Delete an existing camera wireless profile for this network.

    :param network_id: 
    :type network_id: str
    :param wireless_profile_id: 
    :type wireless_profile_id: str

    """
    return web.Response(status=200)


async def get_device_camera_wireless_profiles_1(request: web.Request, serial) -> web.Response:
    """Returns wireless profile assigned to the given camera

    Returns wireless profile assigned to the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_camera_wireless_profile_1(request: web.Request, network_id, wireless_profile_id) -> web.Response:
    """Retrieve a single camera wireless profile.

    Retrieve a single camera wireless profile.

    :param network_id: 
    :type network_id: str
    :param wireless_profile_id: 
    :type wireless_profile_id: str

    """
    return web.Response(status=200)


async def get_network_camera_wireless_profiles_1(request: web.Request, network_id) -> web.Response:
    """List the camera wireless profiles for this network.

    List the camera wireless profiles for this network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_device_camera_wireless_profiles_1(request: web.Request, serial, body) -> web.Response:
    """Assign wireless profiles to the given camera

    Assign wireless profiles to the given camera. Incremental updates are not supported, all profile assignment need to be supplied at once.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraWirelessProfilesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_camera_wireless_profile_1(request: web.Request, network_id, wireless_profile_id, body=None) -> web.Response:
    """Update an existing camera wireless profile in this network.

    Update an existing camera wireless profile in this network.

    :param network_id: 
    :type network_id: str
    :param wireless_profile_id: 
    :type wireless_profile_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCameraWirelessProfileRequest.from_dict(body)
    return web.Response(status=200)
