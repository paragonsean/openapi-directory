from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.shared_catalog_company_management_v1_assign_companies_post_request import SharedCatalogCompanyManagementV1AssignCompaniesPostRequest
from openapi_server import util


async def shared_catalog_company_management_v1_assign_companies_post(request: web.Request, shared_catalog_id, body=None) -> web.Response:
    """sharedCatalog/{sharedCatalogId}/assignCompanies

    Assign companies to a shared catalog.

    :param shared_catalog_id: 
    :type shared_catalog_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.from_dict(body)
    return web.Response(status=200)
