from typing import List, Dict
from aiohttp import web

from openapi_server.models.pricing_countries_response import PricingCountriesResponse
from openapi_server.models.pricing_country_response import PricingCountryResponse
from openapi_server.models.retrieve_pricing_all_countries400_response import RetrievePricingAllCountries400Response
from openapi_server.models.retrieve_pricing_all_countries401_response import RetrievePricingAllCountries401Response
from openapi_server import util


async def retrieve_prefix_pricing(request: web.Request, type, api_key, api_secret, prefix) -> web.Response:
    """Retrieve outbound pricing for a specific dialing prefix.

    Retrieves the pricing information based on the dialing prefix. 

    :param type: The type of service you wish to retrieve data about: either &#x60;sms&#x60;, &#x60;sms-transit&#x60; or &#x60;voice&#x60;.
    :type type: str
    :param api_key: Your Nexmo API key.
    :type api_key: str
    :param api_secret: Your Nexmo API secret.
    :type api_secret: str
    :param prefix: The numerical dialing prefix to look up pricing for. Examples include 44, 1 and so on.
    :type prefix: str

    """
    return web.Response(status=200)


async def retrieve_pricing_all_countries(request: web.Request, type, api_key, api_secret) -> web.Response:
    """Retrieve outbound pricing for all countries.

    Retrieves the pricing information for all countries. 

    :param type: The type of service you wish to retrieve data about: either &#x60;sms&#x60;, &#x60;sms-transit&#x60; or &#x60;voice&#x60;.
    :type type: str
    :param api_key: Your Nexmo API key.
    :type api_key: str
    :param api_secret: Your Nexmo API secret.
    :type api_secret: str

    """
    return web.Response(status=200)


async def retrieve_pricing_country(request: web.Request, type, api_key, api_secret, country) -> web.Response:
    """Retrieve outbound pricing for a specific country.

    Retrieves the pricing information based on the specified country. 

    :param type: The type of service you wish to retrieve data about: either &#x60;sms&#x60;, &#x60;sms-transit&#x60; or &#x60;voice&#x60;.
    :type type: str
    :param api_key: Your Nexmo API key.
    :type api_key: str
    :param api_secret: Your Nexmo API secret.
    :type api_secret: str
    :param country: A two letter [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). For example, &#x60;CA&#x60;.
    :type country: str

    """
    return web.Response(status=200)
