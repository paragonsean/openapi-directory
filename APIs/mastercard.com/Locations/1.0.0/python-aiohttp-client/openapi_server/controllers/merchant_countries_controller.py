from typing import List, Dict
from aiohttp import web

from openapi_server.models.countries_response import CountriesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def merchants_v1_country_get(request: web.Request, details) -> web.Response:
    """Returns countries that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

    Returns countries that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

    :param details: This is the type of merchant location. Options  \&quot;acceptance.paypass\&quot; \&quot;topup.repower\&quot;  \&quot;products.prepaidtravelcard\&quot;  and \&quot;offers.easysavings\&quot;
    :type details: str

    """
    return web.Response(status=200)
