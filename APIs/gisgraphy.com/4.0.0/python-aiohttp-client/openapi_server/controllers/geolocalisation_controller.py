from typing import List, Dict
from aiohttp import web

from openapi_server.models.geoloc_results_dto import GeolocResultsDto
from openapi_server import util


async def geoloc(request: web.Request, lat, lng, radius=None, distance=None, placetype=None, format=None, _from=None, to=None, param_callback=None, indent=None) -> web.Response:
    """Geocode an address

    The geolocalisation service allows to search for features around a earth location. you can Specify GPS position, Limit the results to a specific place type (e.g : search all monuments around a point), Limit the results to a specified radius, Paginate the results, Tells if you want the output to be indented (currently, applies only for XML, not JSON for performance reasons. May change in next version)

    :param lat: The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates
    :type lat: float
    :param lng: TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates.
    :type lng: float
    :param radius: distance from the location point in meters we&#39;d like to search around. The value is a number &gt; 0 if it is not specify or incorrect.
    :type radius: float
    :param distance: Whether (or not) we want the distance field to be output. This option is useful to improve the performance if we don&#39;t care about the distance (e.g : we search for name). Of course, the results won&#39;t be sorted by distance. If you use a checkbox in a form to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so to simplify the use : the value for the web service can be &#39;true&#39; or &#39;on&#39;
    :type distance: bool
    :param placetype: filter search for a given placetype
    :type placetype: str
    :param format: The output format.
    :type format: str
    :param _from: The first pagination index. Numbered from 1. If the number is &lt; 1 or not specified, it will be set to the default value : 1
    :type _from: int
    :param to: The last pagination index. if &lt; 1 or not specified, it will be set to startindex + 10. Max &#x3D; 10 (can be changed)
    :type to: int
    :param param_callback: The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
    :type param_callback: str
    :param indent: indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39;
    :type indent: bool

    """
    return web.Response(status=200)
