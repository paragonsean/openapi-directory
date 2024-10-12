from typing import List, Dict
from aiohttp import web

from openapi_server.models.calibrate_imu_payload import CalibrateImuPayload
from openapi_server.models.set_north_imu_payload import SetNorthImuPayload
from openapi_server.models.waterlinked_imu import WaterlinkedImu
from openapi_server import util


async def imu_calibrate(request: web.Request, payload) -> web.Response:
    """Calibrate imu

    [DEPRECATED]Start calibration

    :param payload: IMU calibration action
    :type payload: dict | bytes

    """
    payload = CalibrateImuPayload.from_dict(payload)
    return web.Response(status=200)


async def imu_get(request: web.Request, ) -> web.Response:
    """Get imu

    Get IMU status and orientation


    """
    return web.Response(status=200)


async def imu_reset_gyro(request: web.Request, ) -> web.Response:
    """ResetGyro imu

    Reset Gyro


    """
    return web.Response(status=200)


async def imu_set_north(request: web.Request, payload) -> web.Response:
    """SetNorth imu

    Set north point

    :param payload: IMU set north
    :type payload: dict | bytes

    """
    payload = SetNorthImuPayload.from_dict(payload)
    return web.Response(status=200)
