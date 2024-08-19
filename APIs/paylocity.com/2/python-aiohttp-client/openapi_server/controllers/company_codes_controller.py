from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_codes import CompanyCodes
from openapi_server.models.error import Error
from openapi_server import util


async def get_all_company_codes_and_descriptions_by_resource(request: web.Request, company_id, code_resource) -> web.Response:
    """Get All Company Codes

    Get All Company Codes for the selected company and resource

    :param company_id: Company Id
    :type company_id: str
    :param code_resource: Type of Company Code. Common values costcenter1, costcenter2, costcenter3, deductions, earnings, taxes, paygrade, positions.
    :type code_resource: str

    """
    return web.Response(status=200)
