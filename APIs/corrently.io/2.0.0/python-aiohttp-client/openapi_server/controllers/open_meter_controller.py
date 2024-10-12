from typing import List, Dict
from aiohttp import web

from openapi_server.models.ommeters import Ommeters
from openapi_server import util


async def om_activities(request: web.Request, ) -> web.Response:
    """Public shared smart meters installed in Germany and available for subservices and exploration.

    Provides a list of available meterrs in the OpenMETER project ( https://www.openmeter.de/ ) which grants access for analytics as data discovery. 


    """
    return web.Response(status=200)


async def om_meters(request: web.Request, ) -> web.Response:
    """Public shared smart meters installed in Germany and available for subservices and exploration.

    Provides a list of available meterrs in the OpenMETER project ( https://www.openmeter.de/ ) which grants access for analytics as data discovery. 


    """
    return web.Response(status=200)


async def om_readings(request: web.Request, ) -> web.Response:
    """Public shared smart meters installed in Germany and available for subservices and exploration.

    Provides a list of available meterrs in the OpenMETER project ( https://www.openmeter.de/ ) which grants access for analytics as data discovery. 


    """
    return web.Response(status=200)
