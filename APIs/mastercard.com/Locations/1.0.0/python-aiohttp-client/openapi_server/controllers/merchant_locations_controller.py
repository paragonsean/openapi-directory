from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.merchants_response import MerchantsResponse
from openapi_server import util


async def merchants_v1_merchant_get(request: web.Request, details, page_offset, page_length, category=None, address_line1=None, address_line2=None, city=None, country_subdivision=None, postal_code=None, country=None, latitude=None, longitude=None, distance_unit=None, radius=None, offer_merchant_id=None) -> web.Response:
    """Returns merchant location information for merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, participate in the MasterCard Easy Savings program, and offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

    Returns merchant location information for merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, participate in the MasterCard Easy Savings program, and offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

    :param details: Type of merchant location. Options are \&quot;acceptance.paypass\&quot; \&quot;topup.repower\&quot; \&quot;products.prepaidtravelcard\&quot; \&quot;offers.easysavings\&quot; and \&quot;features.cashback\&quot;. Cash Back is currently only available in the US.
    :type details: str
    :param page_offset: Zero-based offset where the response will start. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests.
    :type page_offset: int
    :param page_length: Maximum number of items to retrieve within the current \&quot;page\&quot; of results.
    :type page_length: int
    :param category: Category of the merchant location. See the Categories (Merchant) resource for a list of valid categories. This parameter is only valid for merchant queries with Details &#x3D; \&quot;acceptance.paypass\&quot; or \&quot;features.cashback\&quot;.
    :type category: str
    :param address_line1: Line 1 of the street address for the merchant location.  Usually includes the street number and name. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
    :type address_line1: str
    :param address_line2: Line 2 of the street address usually an apartment number or suite number. This parameter is used rarely and is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
    :type address_line2: str
    :param city: Name of the city for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
    :type city: str
    :param country_subdivision: State or province for a merchant location (only supported for US and Canada locations).  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
    :type country_subdivision: str
    :param postal_code: Zip code or postal code for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
    :type postal_code: str
    :param country: Any three digit country code for an ATM location.  Valid values are Three digit alpha country code as defined in ISO 3166-1.  This parameter is ignored if latitude and longitude are provided. This parameter is required if any other address information is provided including AddressLine1 AddressLine2 City PostalCode or CountrySubdivision. By default we supply ATM location data for United States ATMs for up to twenty-five records per request.
    :type country: str
    :param latitude: Latitude of a merchant location.  If latitude is provided longitude must also be provided.
    :type latitude: float
    :param longitude: Longitude of a merchant location.  If longitude is provided latitude must also be provided.
    :type longitude: float
    :param distance_unit: Indicates the unit for the radius as well as the units of the distance of each location from the basepoint in the response.
    :type distance_unit: str
    :param radius: This is the radius from the search point in the distance unit you set.  For example if you want to search for locations within 50 miles of a certain point you would set DistanceUnit&#x3D;mile and Radius&#x3D;50.  This parameter is ignored in non-geocoded countries.
    :type radius: int
    :param offer_merchant_id: Unique identifier that represents the merhcant sponsor of an offer. Any valid merchant ID.
    :type offer_merchant_id: str

    """
    return web.Response(status=200)
