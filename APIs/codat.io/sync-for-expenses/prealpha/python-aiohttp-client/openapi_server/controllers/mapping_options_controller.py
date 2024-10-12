from typing import List, Dict
from aiohttp import web

from openapi_server.models.mapping_options import MappingOptions
from openapi_server import util


async def get_mapping_options(request: web.Request, company_id) -> web.Response:
    """Mapping options

    Gets the expense mapping options for a companies accounting software

    :param company_id: 
    :type company_id: str
    :type company_id: str

    """
    return web.Response(status=200)
