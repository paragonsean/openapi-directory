from typing import List, Dict
from aiohttp import web

from openapi_server.models.describetheregionwithin5minutedrive_timeofageographicpoint import Describetheregionwithin5minutedriveTimeofageographicpoint
from openapi_server.models.fetch_administrative_regionsusing_lat_lng import FetchAdministrativeRegionsusingLatLng
from openapi_server import util


async def fetch_administrative_regionsusing_lat_lng(request: web.Request, latitude, longitude, x_rapid_api_key, x_rapid_api_host) -> web.Response:
    """Fetch Administrative Regions using Lat/Lng

    For given latitude and longitude, find intersecting administrative regions. Region polygons are simplified for web mapping.

    :param latitude: (Required) Search coordinate latitude
    :type latitude: float
    :param longitude: (Required) Search coordinate longitude
    :type longitude: float
    :param x_rapid_api_key: (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    :type x_rapid_api_key: str
    :param x_rapid_api_host: 
    :type x_rapid_api_host: str

    """
    return web.Response(status=200)


async def fetch_geometries(request: web.Request, location, x_rapid_api_key, x_rapid_api_host) -> web.Response:
    """Fetch Geometries

    Fetch location GeoJSON

    :param location: (Required) Represents a buffer, region, or custom polygon specification. Accepts the &#x60;Location&#x60; model (as a &#x60;Buffer&#x60;, &#x60;Region&#x60;, or &#x60;Custom Polygon&#x60;) formatted as a JSON string. Multiple &#x60;location&#x60; query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. &#x60;?location[]&#x3D;...&amp;location[]&#x3D;...&#x60;). If not included, only the last location will be used.
    :type location: str
    :param x_rapid_api_key: (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    :type x_rapid_api_key: str
    :param x_rapid_api_host: 
    :type x_rapid_api_host: str

    """
    return web.Response(status=200)
