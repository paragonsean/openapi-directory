from typing import List, Dict
from aiohttp import web

from openapi_server.models.impact_smart_list_read import ImpactSmartListRead
from openapi_server.models.impact_smart_list_write import ImpactSmartListWrite
from openapi_server import util


async def get_impact_smart_list_item(request: web.Request, id) -> web.Response:
    """Retrieves a ImpactSmartList resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_impact_smart_list_collection(request: web.Request, impact_smart_list=None) -> web.Response:
    """Creates a ImpactSmartList resource.

    

    :param impact_smart_list: The new ImpactSmartList resource
    :type impact_smart_list: dict | bytes

    """
    impact_smart_list = ImpactSmartListWrite.from_dict(impact_smart_list)
    return web.Response(status=200)
