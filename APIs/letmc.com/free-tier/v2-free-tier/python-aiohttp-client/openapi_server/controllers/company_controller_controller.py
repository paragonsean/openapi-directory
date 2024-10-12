from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_model import CompanyModel
from openapi_server import util


async def company_controller_get_company(request: web.Request, short_name) -> web.Response:
    """Information about a specific company

    

    :param short_name: The unique client short-name
    :type short_name: str

    """
    return web.Response(status=200)
