from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.geocode_address_response import GeocodeAddressResponse
from openapi_server.models.geocode_reverse_response import GeocodeReverseResponse
from openapi_server.models.ip_info_response import IPInfoResponse
from openapi_server import util


async def geocode_address(request: web.Request, address=None, house_number=None, street=None, city=None, county=None, state=None, postal_code=None, country_code=None, language_code=None, fuzzy_search=None) -> web.Response:
    """Geocode Address

    Geocode an address, partial address or just the name of a place

    :param address: The full address, partial address or name of a place to try and locate. Comma separated address components are preferred.
    :type address: str
    :param house_number: The house/building number to locate
    :type house_number: str
    :param street: The street/road name to locate
    :type street: str
    :param city: The city/town name to locate
    :type city: str
    :param county: The county/region name to locate
    :type county: str
    :param state: The state name to locate
    :type state: str
    :param postal_code: The postal code to locate
    :type postal_code: str
    :param country_code: Limit result to this country (the default is no country bias)
    :type country_code: str
    :param language_code: The language to display results in, available languages are: &lt;ul&gt; &lt;li&gt;de, en, es, fr, it, pt, ru, zh&lt;/li&gt; &lt;/ul&gt;
    :type language_code: str
    :param fuzzy_search: If no matches are found for the given address, start performing a recursive fuzzy search until a geolocation is found. This option is recommended for processing user input or implementing auto-complete. We use a combination of approximate string matching and data cleansing to find possible location matches
    :type fuzzy_search: bool

    """
    return web.Response(status=200)


async def geocode_reverse(request: web.Request, latitude, longitude, language_code=None, zoom=None) -> web.Response:
    """Geocode Reverse

    Convert a geographic coordinate (latitude and longitude) into a real world address

    :param latitude: The location latitude in decimal degrees format
    :type latitude: str
    :param longitude: The location longitude in decimal degrees format
    :type longitude: str
    :param language_code: The language to display results in, available languages are: &lt;ul&gt; &lt;li&gt;de, en, es, fr, it, pt, ru&lt;/li&gt; &lt;/ul&gt;
    :type language_code: str
    :param zoom: The zoom level to respond with: &lt;br&gt; &lt;ul&gt; &lt;li&gt;address - the most precise address available&lt;/li&gt; &lt;li&gt;street - the street level&lt;/li&gt; &lt;li&gt;city - the city level&lt;/li&gt; &lt;li&gt;state - the state level&lt;/li&gt; &lt;li&gt;country - the country level&lt;/li&gt; &lt;/ul&gt;
    :type zoom: str

    """
    return web.Response(status=200)


async def i_p_info(request: web.Request, ip, reverse_lookup=None) -> web.Response:
    """IP Info

    Get location information about an IP address and do reverse DNS (PTR) lookups

    :param ip: IPv4 or IPv6 address
    :type ip: str
    :param reverse_lookup: Do a reverse DNS (PTR) lookup. This option can add extra delay to the request so only use it if you need it
    :type reverse_lookup: bool

    """
    return web.Response(status=200)
