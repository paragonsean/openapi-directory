from typing import List, Dict
from aiohttp import web

from openapi_server.models.waterlinked_accoustic_position import WaterlinkedAccousticPosition
from openapi_server.models.wl_satellite_position import WlSatellitePosition
from openapi_server import util


async def position_acoustic_filtered(request: web.Request, ) -> web.Response:
    """AcousticFiltered position

    Get current Kalman filtered acoustic position relative to master acoustics. Expected update frequency: 4 Hz


    """
    return web.Response(status=200)


async def position_acoustic_raw(request: web.Request, ) -> web.Response:
    """AcousticRaw position

    Get current unfiltered acoustic position relative to master acoustics. Expected update frequency: 4 Hz


    """
    return web.Response(status=200)


async def position_get(request: web.Request, ) -> web.Response:
    """Get position

    Get current global position of locator. Locator position is calculated from the current acoustic position and the global position of the master electronics. Expected update frequency: 4 Hz


    """
    return web.Response(status=200)


async def position_get_master(request: web.Request, ) -> web.Response:
    """GetMaster position

    Get current global position of master electronics. Expected update frequency: 1 Hz


    """
    return web.Response(status=200)
