from typing import List, Dict
from aiohttp import web

from openapi_server.models.atm_definition_meta import ATMDefinitionMeta
from openapi_server.models.error_definition400 import ErrorDefinition400
from openapi_server.models.error_definition408 import ErrorDefinition408
from openapi_server.models.error_definition429 import ErrorDefinition429
from openapi_server.models.error_definition500 import ErrorDefinition500
from openapi_server.models.error_definition503 import ErrorDefinition503
from openapi_server import util


async def open_banking_v22_atms_get(request: web.Request, ) -> web.Response:
    """open_banking_v22_atms_get

    This API will return data about all our ATMs and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.


    """
    return web.Response(status=200)


async def x_open_banking_v22_atms_country_country_get(request: web.Request, country) -> web.Response:
    """x_open_banking_v22_atms_country_country_get

    This extended API will return data about all ATMs in the specified country. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

    :param country: The ISO country code e.g. &amp;quot;GB&amp;quot;
    :type country: str

    """
    return web.Response(status=200)


async def x_open_banking_v22_atms_country_country_town_town_get(request: web.Request, country, town) -> web.Response:
    """x_open_banking_v22_atms_country_country_town_town_get

    This extended API will return data about all ATMs in the specified town. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

    :param country: The ISO country code e.g. &amp;quot;GB&amp;quot;
    :type country: str
    :param town: Town name, not case sensitive
    :type town: str

    """
    return web.Response(status=200)


async def x_open_banking_v22_atms_geo_location_lat_latitude_long_longitude_get(request: web.Request, latitude, longitude, radius) -> web.Response:
    """x_open_banking_v22_atms_geo_location_lat_latitude_long_longitude_get

    This extended API will data about all ATMs within a specified radius (1 to 10 miles) of the specified latitude and longitude. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

    :param latitude: Positive or negative decimal value in degrees. eg &amp;quot;51.50551621597067&amp;quot;
    :type latitude: str
    :param longitude: Positive or negative decimal value in degrees. eg &amp;quot;-0.0180120225995&amp;quot;
    :type longitude: str
    :param radius: Number of miles (1 to 10) as an integer. Default &#x3D; 1
    :type radius: 

    """
    return web.Response(status=200)


async def x_open_banking_v22_atms_postcode_postcode_get(request: web.Request, postcode) -> web.Response:
    """x_open_banking_v22_atms_postcode_postcode_get

    This extended API will return data about all ATMs within a 5 mile radius of the specified postcode. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

    :param postcode: Letters and numerals only. No spaces or special characters. eg  &amp;quot;SW1A1AA&amp;quot;
    :type postcode: str

    """
    return web.Response(status=200)
