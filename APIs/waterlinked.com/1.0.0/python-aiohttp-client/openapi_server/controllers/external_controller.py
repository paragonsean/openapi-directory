from typing import List, Dict
from aiohttp import web

from openapi_server.models.set_depth_external_payload import SetDepthExternalPayload
from openapi_server.models.set_master_external_payload import SetMasterExternalPayload
from openapi_server.models.set_orientation_external_payload import SetOrientationExternalPayload
from openapi_server.models.set_vehicle_imu_external_payload import SetVehicleIMUExternalPayload
from openapi_server.models.waterlinked_operation_response import WaterlinkedOperationResponse
from openapi_server.models.wl_external_locator_orientation import WlExternalLocatorOrientation
from openapi_server.models.wl_external_vehicle_imu import WlExternalVehicleImu
from openapi_server import util


async def external_get_orientation(request: web.Request, ) -> web.Response:
    """GetOrientation external

    Get orientation of Vehicle/ROV/Locator set by SetOrientation


    """
    return web.Response(status=200)


async def external_get_vehicle_imu(request: web.Request, ) -> web.Response:
    """GetVehicleIMU external

    [DEPRECATED]Get rotation and acceleration of vehicle Locator is mounted on which was previously set


    """
    return web.Response(status=200)


async def external_set_depth(request: web.Request, payload) -> web.Response:
    """SetDepth external

    Set depth from external source. If Locator A1 is used, this is required to get a position

    :param payload: Current locator depth and temperature
    :type payload: dict | bytes

    """
    payload = SetDepthExternalPayload.from_dict(payload)
    return web.Response(status=200)


async def external_set_master(request: web.Request, payload) -> web.Response:
    """SetMaster external

    Set current global position of master electronics from external source. Values are only used if GPS mode is set to use external GPS

    :param payload: Global master position from external source
    :type payload: dict | bytes

    """
    payload = SetMasterExternalPayload.from_dict(payload)
    return web.Response(status=200)


async def external_set_orientation(request: web.Request, payload) -> web.Response:
    """SetOrientation external

    Set orientation/compass heading of Vehicle/ROV/Locator. This is used only for visualization in GUI

    :param payload: Set current compass heading of ROV/locator
    :type payload: dict | bytes

    """
    payload = SetOrientationExternalPayload.from_dict(payload)
    return web.Response(status=200)


async def external_set_vehicle_imu(request: web.Request, payload) -> web.Response:
    """SetVehicleIMU external

    [DEPRECATED]Set rotation and acceleration of vehicle Locator is mounted on. This is used to improve positioning of vehicle

    :param payload: Set current rotation and acceleration of vehicle
    :type payload: dict | bytes

    """
    payload = SetVehicleIMUExternalPayload.from_dict(payload)
    return web.Response(status=200)
