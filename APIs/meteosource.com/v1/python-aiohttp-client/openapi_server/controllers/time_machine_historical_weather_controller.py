from typing import List, Dict
from aiohttp import web

from openapi_server.models.general_request_error import GeneralRequestError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.time_machine_time_machine import TimeMachineTimeMachine
from openapi_server.models.units import Units
from openapi_server import util


async def time_machine_time_machine_get(request: web.Request, _date, place_id=None, lat=None, lon=None, timezone=None, units=None, key=None) -> web.Response:
    """Returns weather data for a single location and given day in the past

    ## Actual weather data for a single location and day in the past  The output contains actual weather data for each day up to 20 years in the past, and long-term statistics of selected weather variables aggregated over 40 years.  ### Location specification The location of the weather data must be specified. There are two ways to do this: 1. Specify the GPS coordinates of the location using the parameters &#x60;lat&#x60; and &#x60;lon&#x60;. 2. **OR** specify the name of the place using the parameter &#x60;place_id&#x60;. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name).  *Note: For mountains, it is usually better to specify the &#x60;place_id&#x60; rather than the &#x60;lat&#x60; and &#x60;lon&#x60;. When you use &#x60;place_id&#x60;, you are guaranteed to receive data for the precise elevation of the peak. When you specify the coordinates, the elevation can be less precise.*

    :param _date: The day of the data in the past. Specify in &#x60;YYYY-MM-DD&#x60; format, e.g. &#x60;2021-08-24&#x60;. 
    :type _date: str
    :param place_id: Identifier of a place. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name).
    :type place_id: str
    :param lat: Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4
    :type lat: str
    :param lon: Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4
    :type lon: str
    :param timezone: Timezone to be used for the date fields. If not specified, local timezone of the location will be used. The format is according to the tzinfo database, so values like &#x60;Europe/Prague&#x60; or &#x60;UTC&#x60; can be used. Alternatively you may use the value &#x60;&#x60;auto&#x60;&#x60; in which case the local timezone of the location is used. The full list of valid timezone strings can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). 
    :type timezone: str
    :param units: Unit system to be used. The available values are:  * &#x60;auto&#x60;: Select the system automatically, based on the forecast location. * &#x60;metric&#x60;: Metric (SI) units (&#x60;°C&#x60;, &#x60;mm/h&#x60;, &#x60;m/s&#x60;, &#x60;cm&#x60;, &#x60;km&#x60;, &#x60;hPa&#x60;). * &#x60;us&#x60;: Imperial units (&#x60;°F&#x60;, &#x60;in/h&#x60;, &#x60;mph&#x60;, &#x60;in&#x60;, &#x60;mi&#x60;, &#x60;Hg&#x60;). * &#x60;uk&#x60;: Same as &#x60;&#x60;metric&#x60;&#x60;, except that visibility is in &#x60;miles&#x60; and wind speeds are in &#x60;mph&#x60;. * &#x60;ca&#x60;: Same as &#x60;&#x60;metric&#x60;&#x60;, except that wind speeds are in &#x60;km/h&#x60; and pressure is in &#x60;kPa&#x60;. 
    :type units: dict | bytes
    :param key: Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header.
    :type key: str

    """
    _date = util.deserialize_date(_date)
    units = .from_dict(units)
    return web.Response(status=200)
