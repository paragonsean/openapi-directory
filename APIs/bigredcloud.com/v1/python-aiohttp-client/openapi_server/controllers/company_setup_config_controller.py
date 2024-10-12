from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_option_dto import CompanyOptionDto
from openapi_server.models.company_setup_config_view_model import CompanySetupConfigViewModel
from openapi_server.models.financial_year_dto import FinancialYearDto
from openapi_server import util


async def company_setup_config_get(request: web.Request, ) -> web.Response:
    """Returns the company configuration settings.

    


    """
    return web.Response(status=200)


async def company_setup_config_get_company_options(request: web.Request, ) -> web.Response:
    """Returns the company option setting.

    


    """
    return web.Response(status=200)


async def company_setup_config_get_financial_year(request: web.Request, ) -> web.Response:
    """Returns the financial year.

    


    """
    return web.Response(status=200)
