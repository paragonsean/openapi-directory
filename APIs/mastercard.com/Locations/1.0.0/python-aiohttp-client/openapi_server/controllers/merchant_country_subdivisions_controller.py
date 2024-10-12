from typing import List, Dict
from aiohttp import web

from openapi_server.models.country_subdivision_response import CountrySubdivisionResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def merchants_v1_countrysubdivision_get(request: web.Request, details, country) -> web.Response:
    """Returns country subdivisions that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. A country subdivision is a segment within a country (ex  state or province).  Please note country subdivisions are only available for the US and Canada. 

    Returns country subdivisions that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. A country subdivision is a segment within a country (ex  state or province).  Please note country subdivisions are only available for the US and Canada. 

    :param details: This is the type of merchant location. Options  \&quot;acceptance.paypass\&quot; \&quot;topup.repower\&quot;  \&quot;products.prepaidtravelcard\&quot;  and \&quot;offers.easysavings\&quot;
    :type details: str
    :param country: Any three digit country code as defined in ISO 3166-1. For example \&quot;USA or \&quot;CAN\&quot;
    :type country: str

    """
    return web.Response(status=200)
