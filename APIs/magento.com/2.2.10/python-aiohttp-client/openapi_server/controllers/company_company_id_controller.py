from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_company_repository_v1_save_post_request import CompanyCompanyRepositoryV1SavePostRequest
from openapi_server.models.company_data_company_interface import CompanyDataCompanyInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_company_repository_v1_delete_by_id_delete(request: web.Request, company_id) -> web.Response:
    """company/{companyId}

    Delete a company. Customers belonging to a company are not deleted with this request.

    :param company_id: 
    :type company_id: int

    """
    return web.Response(status=200)


async def company_company_repository_v1_get_get(request: web.Request, company_id) -> web.Response:
    """company/{companyId}

    Returns company details.

    :param company_id: 
    :type company_id: int

    """
    return web.Response(status=200)


async def company_company_repository_v1_save_put(request: web.Request, company_id, body=None) -> web.Response:
    """company/{companyId}

    Create or update a company account.

    :param company_id: 
    :type company_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompanyCompanyRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
