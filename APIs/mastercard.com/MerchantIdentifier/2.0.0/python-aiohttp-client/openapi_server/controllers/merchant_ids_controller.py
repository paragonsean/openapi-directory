from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.merchant_ids import MerchantIds
from openapi_server import util


async def get_merchant_identifiers(request: web.Request, merchant_id=None, type=None) -> web.Response:
    """Returns merchant descriptor and locator information based on the criteria you provide.  Information returned includes merchant DBA name, merchant category code (MCC), street address, city, state, postal code, country, and sales channels.

    

    :param merchant_id: Merchant&#39;s name as provided by the issuer found on a cardholder statement. __Important: Please remove all spaces before submitting a API request.__   
    :type merchant_id: str
    :param type: Determines how the search is performed.              ExactMatch returns either the one merchant that best fits the description or no results at all.              FuzzyMatch returns 0-20 merchants that are similar to the transaction descriptor.               If Type is not provided, defaults to ExactMatch.              Example: FuzzyMatch
    :type type: str

    """
    return web.Response(status=200)
