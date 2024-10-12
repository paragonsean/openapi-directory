from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_results_dto import AddressResultsDto
from openapi_server import util


async def geocode(request: web.Request, address, country=None, postal=None, format=None, _from=None, to=None, param_callback=None, indent=None) -> web.Response:
    """Geocode an address

    The Gisgraphy geocoding service allows you to transform postal addresses or other descriptions (a street, a city, a postal code, a country, or a combination) of a location into a (latitude, longitude) coordinate.

    :param address: A postal address, structured or not, a street, a city, a postal code, a country, or a combination.
    :type address: str
    :param country: The country where the place/address is. It is used to determine the postal address format and to improve performance. It will probably be optional in next version to ease the usability. The value must be the ISO 3166 Alpha 2 code of the country.
    :type country: str
    :param postal: Whether the given address is a postal address. default to false. In other words, if the address follow the specification or if it is a well-formed address as it was written on an envelope. This parameter will enable the parsing of the address by the address parser before geocoding, this way, the relevance will be better because because if parsing is successful, we will know the meaning of each word. Note that you can also specify each field if you already know them.
    :type postal: str
    :param format: The output format.
    :type format: str
    :param _from: The first pagination index. Numbered from 1. If the number is &lt; 1 or not specified, it will be set to the default value : 1
    :type _from: int
    :param to: The last pagination index. if &lt; 1 or not specified, it will be set to startindex + 10. Max &#x3D; 10 (can be changed)
    :type to: int
    :param param_callback: The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
    :type param_callback: str
    :param indent: indents the results. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39;
    :type indent: bool

    """
    return web.Response(status=200)
