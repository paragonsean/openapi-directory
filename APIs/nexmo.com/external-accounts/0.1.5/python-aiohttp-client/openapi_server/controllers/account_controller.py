from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_all_accounts200_response import GetAllAccounts200Response
from openapi_server.models.model401_response import Model401Response
from openapi_server import util


async def get_all_accounts(request: web.Request, provider=None, page_number=None, page_size=None) -> web.Response:
    """Retrieve all accounts you own

    

    :param provider: Filter by provider
    :type provider: str
    :param page_number: Page number of the results
    :type page_number: int
    :param page_size: Page size of the results
    :type page_size: int

    """
    return web.Response(status=200)
