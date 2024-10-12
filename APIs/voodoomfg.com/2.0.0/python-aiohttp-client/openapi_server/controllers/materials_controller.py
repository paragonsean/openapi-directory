from typing import List, Dict
from aiohttp import web

from openapi_server.models.material import Material
from openapi_server import util


async def materials_get(request: web.Request, ) -> web.Response:
    """Voodoo Manufacturing offers printing in a number of different materials, with different color options for each. Your organization can expose as many or as few material options as you want to your end-customer. 

    The Materials endpoint returns a list of materials that are currently available for production for your account. The responses include display details about each material, along with the unique id required to request a print in a specific material. 


    """
    return web.Response(status=200)
