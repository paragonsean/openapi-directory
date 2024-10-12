from typing import List, Dict
from aiohttp import web

from openapi_server.models.codat_error_message import CodatErrorMessage
from openapi_server.models.company_configuration import CompanyConfiguration
from openapi_server import util


async def get_company_configuration(request: web.Request, company_id) -> web.Response:
    """Get company configuration

    Gets a companies expense sync configuration

    :param company_id: 
    :type company_id: str
    :type company_id: str

    """
    return web.Response(status=200)


async def save_company_configuration(request: web.Request, company_id, body=None) -> web.Response:
    """Set company configuration

    Sets a companies expense sync configuration

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompanyConfiguration.from_dict(body)
    return web.Response(status=200)
