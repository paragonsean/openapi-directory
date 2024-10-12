from typing import List, Dict
from aiohttp import web

from openapi_server.models.generate_network_camera_snapshot_request import GenerateNetworkCameraSnapshotRequest
from openapi_server.models.update_device_camera_video_settings_request import UpdateDeviceCameraVideoSettingsRequest
from openapi_server import util


async def generate_network_camera_snapshot(request: web.Request, network_id, serial, body=None) -> web.Response:
    """Generate a snapshot of what the camera sees at the specified time and return a link to that image.

    Generate a snapshot of what the camera sees at the specified time and return a link to that image.

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = GenerateNetworkCameraSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def get_device_camera_video_settings(request: web.Request, serial) -> web.Response:
    """Returns video settings for the given camera

    Returns video settings for the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_camera_schedules(request: web.Request, network_id) -> web.Response:
    """Returns a list of all camera recording schedules.

    Returns a list of all camera recording schedules.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_camera_video_link(request: web.Request, network_id, serial, timestamp=None) -> web.Response:
    """Returns video link to the specified camera

    Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.

    :param network_id: 
    :type network_id: str
    :param serial: 
    :type serial: str
    :param timestamp: [optional] The video link will start at this timestamp. The timestamp is in UNIX Epoch time (milliseconds). If no timestamp is specified, we will assume current time.
    :type timestamp: str

    """
    return web.Response(status=200)


async def update_device_camera_video_settings(request: web.Request, serial, body=None) -> web.Response:
    """Update video settings for the given camera

    Update video settings for the given camera

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraVideoSettingsRequest.from_dict(body)
    return web.Response(status=200)
