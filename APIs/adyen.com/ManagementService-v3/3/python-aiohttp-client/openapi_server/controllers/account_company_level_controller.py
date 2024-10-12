from typing import List, Dict
from aiohttp import web

from openapi_server.models.company import Company
from openapi_server.models.list_company_response import ListCompanyResponse
from openapi_server.models.list_merchant_response import ListMerchantResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def get_companies(request: web.Request, page_number=None, page_size=None) -> web.Response:
    """Get a list of company accounts

    Returns the list of company accounts that your API credential has access to. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Account read

    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
    :type page_size: int

    """
    return web.Response(status=200)


async def get_companies_company_id(request: web.Request, company_id) -> web.Response:
    """Get a company account

    Returns the company account specified in the path. Your API credential must have access to the company account.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Account read

    :param company_id: The unique identifier of the company account.
    :type company_id: str

    """
    return web.Response(status=200)


async def get_companies_company_id_merchants(request: web.Request, company_id, page_number=None, page_size=None) -> web.Response:
    """Get a list of merchant accounts

    Returns the list of merchant accounts under the company account specified in the path. The list only includes merchant accounts that your API credential has access to. The list is grouped into pages as defined by the query parameters.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Account read

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
    :type page_size: int

    """
    return web.Response(status=200)
