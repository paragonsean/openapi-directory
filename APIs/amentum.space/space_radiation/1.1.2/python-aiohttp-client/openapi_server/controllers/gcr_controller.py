from typing import List, Dict
from aiohttp import web

from openapi_server.models.flux_at_energy import FluxAtEnergy
from openapi_server import util


async def app_api_endpoints_gcr_calculate_dlr_flux(request: web.Request, year, month, day, z, energy) -> web.Response:
    """Calculate particle flux  

    for the given energy, atomic number, and date. 

    :param year: &lt;br&gt;
    :type year: int
    :param month: &lt;br&gt;
    :type month: int
    :param day: &lt;br&gt;
    :type day: int
    :param z: &lt;br&gt;Particle atomic number
    :type z: 
    :param energy: &lt;br&gt;Particle energy in MeV/n&lt;br&gt; Valid range: [0, 10&lt;sup&gt;6&lt;/sup&gt;] MeV/n&lt;br&gt;  
    :type energy: 

    """
    return web.Response(status=200)
