from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_results_dto import AddressResultsDto
from openapi_server import util


async def reversegeocode(request: web.Request, lat, lng, format=None, _from=None, to=None, param_callback=None, indent=None) -> web.Response:
    """Reverse geocode an address

    The Reverse geocoding service allows to search for an address for a given GPS position.

    :param lat: The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates
    :type lat: float
    :param lng: TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates.
    :type lng: float
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
