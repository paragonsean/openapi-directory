from typing import List, Dict
from aiohttp import web

from openapi_server.models.credas_api_models_companies_company_detail import CredasApiModelsCompaniesCompanyDetail
from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server import util


async def get_company(request: web.Request, company_id, apikey) -> web.Response:
    """get_company

    

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def search_company(request: web.Request, apikey, company_number=None) -> web.Response:
    """Searches for a company based on its Company Number and returns its details.

    If a company appears multiple times within the structure, it will only be detailed in full (i.e. with significant ownership details) in its first instance. Subsequent instances will be               marked as duplicates.              Whilst duplicate instances of companies can and will be identified, it is not possible to categorically identify duplicated people.

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param company_number: The company registration number of the company that should be searched.
    :type company_number: str

    """
    return web.Response(status=200)
