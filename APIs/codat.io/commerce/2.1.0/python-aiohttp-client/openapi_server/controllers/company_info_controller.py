from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_info import CompanyInfo
from openapi_server import util


async def get_company_info(request: web.Request, company_id, connection_id) -> web.Response:
    """Get company info

    Retrieve information about the company, as seen in the commerce platform.  This may include information like addresses, tax registration details and social media or website information.

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param connection_id: 
    :type connection_id: str
    :type connection_id: str

    """
    return web.Response(status=200)
