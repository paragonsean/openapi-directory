from typing import List, Dict
from aiohttp import web

from openapi_server.models.waterlinked_about import WaterlinkedAbout
from openapi_server.models.waterlinked_operation_response import WaterlinkedOperationResponse
from openapi_server.models.waterlinked_status import WaterlinkedStatus
from openapi_server.models.waterlinked_temperature import WaterlinkedTemperature
from openapi_server.models.wupdater_apiversion import WupdaterApiversion
from openapi_server import util


async def about_api_version(request: web.Request, ) -> web.Response:
    """ApiVersion about

    


    """
    return web.Response(status=200)


async def about_factory_reset(request: web.Request, ) -> web.Response:
    """FactoryReset about

    Reset all settings on master electronics


    """
    return web.Response(status=200)


async def about_get(request: web.Request, ) -> web.Response:
    """Get about

    Get about information


    """
    return web.Response(status=200)


async def about_led(request: web.Request, ) -> web.Response:
    """LED about

    Flash LED1 on master electronics


    """
    return web.Response(status=200)


async def about_status(request: web.Request, ) -> web.Response:
    """Status about

    Get current IMU and GPS status


    """
    return web.Response(status=200)


async def about_temperature(request: web.Request, ) -> web.Response:
    """Temperature about

    Get board temperature


    """
    return web.Response(status=200)
