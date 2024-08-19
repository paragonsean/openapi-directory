from typing import List, Dict
from aiohttp import web

from openapi_server.models.atms_response import AtmsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def atms_v1_atm_get(request: web.Request, page_offset, page_length, address_line1=None, address_line2=None, city=None, country_subdivision=None, postal_code=None, country=None, latitude=None, longitude=None, distance_unit=None, radius=None, support_emv=None, international_maestro_accepted=None) -> web.Response:
    """Returns detailed information about an ATM location.  This information can be used to display ATMs on a map, provide driving directions, or show special ATM features.

    Returns detailed information about an ATM location.  This information can be used to display ATMs on a map, provide driving directions, or show special ATM features. 

    :param page_offset: Zero-based offset where the response will start. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests.
    :type page_offset: int
    :param page_length: Maximum number of items to retrieve within the current \&quot;page\&quot; of results.
    :type page_length: int
    :param address_line1: Line 1 of the street address for the merchant location.  Usually includes the street number and name. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
    :type address_line1: str
    :param address_line2: Line 2 of the street address usually an apartment number or suite number. This parameter is used rarely and is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
    :type address_line2: str
    :param city: The name of the city for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
    :type city: str
    :param country_subdivision: The state or province for a merchant location (only supported for US and Canada locations).  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
    :type country_subdivision: str
    :param postal_code: The zip code or postal code for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
    :type postal_code: str
    :param country: Any three digit country code for an ATM location.  Valid values are Three digit alpha country code as defined in ISO 3166-1.  This parameter is ignored if latitude and longitude are provided. This parameter is required if any other address information is provided including AddressLine1 AddressLine2 City PostalCode or CountrySubdivision.
    :type country: str
    :param latitude: The latitude of a merchant location.  If latitude is provided longitude must also be provided.
    :type latitude: float
    :param longitude: The longitude of a merchant location.  If longitude is provided latitude must also be provided.
    :type longitude: float
    :param distance_unit: Indicates the unit for the radius as well as the units of the distance of each location from the basepoint in the response.
    :type distance_unit: str
    :param radius: This is the radius from the search point in the distance unit you set.  For example if you want to search for locations within 50 miles of a certain point you would set DistanceUnit&#x3D;mile and Radius&#x3D;50.  This parameter is ignored in non-geocoded countries.
    :type radius: int
    :param support_emv: This indicates whether the ATM should have the ability to read chip cards or not.
    :type support_emv: int
    :param international_maestro_accepted: This field will provide ATM Terminals which can still process Maestro transactions but are not yet EMV chip reader enabled. Information available only for USA and Argentina till October 2014.
    :type international_maestro_accepted: int

    """
    return web.Response(status=200)
