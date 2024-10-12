from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_results_dto import AddressResultsDto
from openapi_server import util


async def addressparsing(request: web.Request, address, country=None, format=None, param_callback=None, indent=None, standardize=None, geocode=None) -> web.Response:
    """split a raw address into several parts

    The address parser and address standardizer, are part of the Gisgraphy project (free open source worldwide geocoder). Address parsing is the process of dividing a single address string into its individual component parts. Please visit [http://www.address-parser.net](http://www.address-parser.net) for more details 

    :param address: A postal address.
    :type address: str
    :param country: The ISO 3166 Alpha 2 code of the country.
    :type country: str
    :param format: The output format.
    :type format: str
    :param param_callback: The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
    :type param_callback: str
    :param indent: indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39;
    :type indent: bool
    :param standardize: Whether the address should be standardized after parsing, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39;
    :type standardize: bool
    :param geocode: UNUSED YET. Whether the address should be geocoded after parsing, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39;
    :type geocode: bool

    """
    return web.Response(status=200)
