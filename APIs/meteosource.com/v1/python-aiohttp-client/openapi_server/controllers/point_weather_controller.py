from typing import List, Dict
from aiohttp import web

from openapi_server.models.air_quality_point_data import AirQualityPointData
from openapi_server.models.general_request_error import GeneralRequestError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.language import Language
from openapi_server.models.point_point_data import PointPointData
from openapi_server.models.units import Units
from openapi_server import util


async def air_quality_air_quality_get(request: web.Request, place_id=None, lat=None, lon=None, timezone=None, key=None) -> web.Response:
    """Returns air quality data for a single point (geographic name or GPS)

    ## Air quality forecast for a single location  ### Location specification The location of the weather data is the only parameter that is required and must be specified. There are two ways to do this: 1. Specify the GPS coordinates of the location using the parameters &#x60;lat&#x60; and &#x60;lon&#x60;. 2. **OR** specify the name of the place using the parameter &#x60;place_id&#x60;. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name).  ### Notes * **For a detailed description of variables, please consult ⚠️ &lt;a href&#x3D;\&quot;https://www.meteosource.com/documentation#description_aq\&quot; target&#x3D;\&quot;_blank\&quot;&gt;description of variables&lt;/a&gt; ⚠️ in Documentation or &#x60;Schema&#x60; of the response (link next to Example value in the Responses section below).** * Do **not** make any assumptions about the number and ordering of the variables. New variables and sections may be introduced in the future. Always check the data are present before you try to use them. * The response contains an &#x60;Expires&#x60; header, which defines the point at which the API response will not change for the same request. We highly recommend using this to avoid unnecessary requests and **increase the performance of your app**. * Meteosource API supports HTTP compression. To enable it, simply add an &#x60;Accept-Encoding: gzip&#x60; header to your request. * When daylight saving time starts, one hourly record will be missing (typically &#x60;2:00:00 AM&#x60;). When daylight saving time ends, the hourly forecast will contain two records with duplicate times (typically &#x60;2:00:00 AM&#x60;).

    :param place_id: Identifier of a place. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name).
    :type place_id: str
    :param lat: Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4
    :type lat: str
    :param lon: Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4
    :type lon: str
    :param timezone: Timezone to be used for the date fields. If not specified, local timezone of the forecast location will be used. The format is according to the tzinfo database, so values like &#x60;Europe/Prague&#x60; or &#x60;UTC&#x60; can be used. Alternatively you may use the value &#x60;&#x60;auto&#x60;&#x60; in which case the local timezone of the location is used. The full list of valid timezone strings can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). 
    :type timezone: str
    :param key: Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header.
    :type key: str

    """
    return web.Response(status=200)


async def point_point_get(request: web.Request, place_id=None, lat=None, lon=None, sections=None, timezone=None, language=None, units=None, key=None) -> web.Response:
    """Returns weather data for a single point (geographic name or GPS)

    ## Current weather and forecast for single location  ### Location specification The location of the weather data is the only parameter that is required and must be specified. There are two ways to do this: 1. Specify the GPS coordinates of the location using the parameters &#x60;lat&#x60; and &#x60;lon&#x60;. 2. **OR** specify the name of the place using the parameter &#x60;place_id&#x60;. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name).  *Note: For mountains, it is usually better to specify the &#x60;place_id&#x60; rather than the &#x60;lat&#x60; and &#x60;lon&#x60;. When you use &#x60;place_id&#x60;, you are guaranteed to receive forecasts for the precise elevation of the peak. When you specify the coordinates, the elevation can be less precise.*  ### Sections The endpoint can return multiple sections of data. To obtain the best performance, we advise only requesting the sections you actually need. The available sections are as follows:  * Current weather situation * Hourly forecast (for 24/48/96/168 hours, depending on the tier) * Daily forecast (for 7/10/30 days, depending on the tier) * Minutely precipitation forecast (for 60 minutes in the following hour, only for higher tiers) * Weather alerts (only for higher tiers)  By default, only the current and hourly sections are returned. The division into daily parts (morning, afternoon and evening) is only available for the first 7 days of the forecast. For details regarding available parameters, see the parameter description below.  ### Notes * **For a detailed description of variables (e.g. icons), please consult ⚠️ &lt;a href&#x3D;\&quot;https://www.meteosource.com/documentation#description\&quot; target&#x3D;\&quot;_blank\&quot;&gt;description of variables&lt;/a&gt; ⚠️ in Documentation or &#x60;Schema&#x60; of the response (link next to Example value in the Responses section below).** * Variables can be instantaneous, averaged, or accumulated over certain time. For example, &#x60;precipitation&#x60; forecast provides the precipitation accumulated until the next hour (data with timestamp as &#x60;12:00:00&#x60; is rain accumulated from &#x60;12:00:00&#x60; to &#x60;13:00:00&#x60;). * Do **not** make any assumptions about the number and ordering of the variables. New variables and sections may be introduced in the future. Always check the data are present before you try to use them. * The response contains an &#x60;Expires&#x60; header, which defines the point at which the API response will not change for the same request. We highly recommend using this to avoid unnecessary requests and **increase the performance of your app**. * Meteosource API supports HTTP compression. To enable it, simply add an &#x60;Accept-Encoding: gzip&#x60; header to your request. * When daylight saving time starts, one hourly record will be missing (typically &#x60;2:00:00 AM&#x60;). When daylight saving time ends, the hourly forecast will contain two records with duplicate times (typically &#x60;2:00:00 AM&#x60;). * The detailed description of weather alerts is only available in English. The alert category is translated into selected language.

    :param place_id: Identifier of a place. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name).
    :type place_id: str
    :param lat: Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4
    :type lat: str
    :param lon: Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4
    :type lon: str
    :param sections: Sections to be included in the response. You can specify more section by separating the values with a comma. The available values are:  * &#x60;&#x60;current&#x60;&#x60;: Current weather situation * &#x60;&#x60;daily&#x60;&#x60;: Forecasts for each whole day, without the daily parts * &#x60;&#x60;daily-parts&#x60;&#x60;: Forecasts for each whole day, morning, afternoon and evening     * Important: forecast for the morning, afternoon and evening is available only for the first       7 days in the forecast * &#x60;&#x60;hourly&#x60;&#x60;: Forecasts with hourly resolution * &#x60;&#x60;minutely&#x60;&#x60;: Precipitation forecast with 1 minute resolution * &#x60;&#x60;alerts&#x60;&#x60;: The weather alerts * &#x60;&#x60;all&#x60;&#x60;: All sections 
    :type sections: str
    :param timezone: Timezone to be used for the date fields. If not specified, local timezone of the forecast location will be used. The format is according to the tzinfo database, so values like &#x60;Europe/Prague&#x60; or &#x60;UTC&#x60; can be used. Alternatively you may use the value &#x60;&#x60;auto&#x60;&#x60; in which case the local timezone of the location is used. The full list of valid timezone strings can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). 
    :type timezone: str
    :param language: The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech 
    :type language: dict | bytes
    :param units: Unit system to be used. The available values are:  * &#x60;auto&#x60;: Select the system automatically, based on the forecast location. * &#x60;metric&#x60;: Metric (SI) units (&#x60;°C&#x60;, &#x60;mm/h&#x60;, &#x60;m/s&#x60;, &#x60;cm&#x60;, &#x60;km&#x60;, &#x60;hPa&#x60;). * &#x60;us&#x60;: Imperial units (&#x60;°F&#x60;, &#x60;in/h&#x60;, &#x60;mph&#x60;, &#x60;in&#x60;, &#x60;mi&#x60;, &#x60;Hg&#x60;). * &#x60;uk&#x60;: Same as &#x60;&#x60;metric&#x60;&#x60;, except that visibility is in &#x60;miles&#x60; and wind speeds are in &#x60;mph&#x60;. * &#x60;ca&#x60;: Same as &#x60;&#x60;metric&#x60;&#x60;, except that wind speeds are in &#x60;km/h&#x60; and pressure is in &#x60;kPa&#x60;. 
    :type units: dict | bytes
    :param key: Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header.
    :type key: str

    """
    language = .from_dict(language)
    units = .from_dict(units)
    return web.Response(status=200)
