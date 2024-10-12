from typing import List, Dict
from aiohttp import web

from openapi_server.models.fleet_fleetname_get200_response import FleetFleetnameGet200Response
from openapi_server import util


async def fleet_fleetname_get(request: web.Request, fleetname) -> web.Response:
    """Get a Fleet

    Use this endpoint to generate a random group of clients. The feleet is generated in a deterministic way, on the basis of a fleet name given as a path parameter. In the case of identical fleet names, the endpoint will generate the same fleet object. The properties of the generated fleet object are randomly generated on the basis of the fleet name. In lack of a fleet name, all calls generate a different fleet object to the randomly generated fleet name.

    :param fleetname:  The identifier or email address of the fleet; it is integrated in the &#x60;sub&#x60; property and is the basis of the other generated properties. 
    :type fleetname: str

    """
    return web.Response(status=200)
