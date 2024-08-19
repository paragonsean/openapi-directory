from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.organization_details_output_model import OrganizationDetailsOutputModel
from openapi_server.models.organization_settings_model import OrganizationSettingsModel
from openapi_server.models.visma_financials_company_model import VismaFinancialsCompanyModel
from openapi_server import util


async def organization_details_get_organization_details(request: web.Request, ) -> web.Response:
    """Get the details of organization.

    


    """
    return web.Response(status=200)


async def organization_settings_get_organization_settings(request: web.Request, ) -> web.Response:
    """Get the settings of organization.

    


    """
    return web.Response(status=200)


async def organizations_get_visma_financials_company_info(request: web.Request, ) -> web.Response:
    """Get Visma.net Financials integration company information.

    


    """
    return web.Response(status=200)
