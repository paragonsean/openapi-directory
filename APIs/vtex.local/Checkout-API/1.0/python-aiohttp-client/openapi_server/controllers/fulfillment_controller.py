from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_address_by_postal_code(request: web.Request, content_type, accept, country_code, postal_code) -> web.Response:
    """Get address by postal code

    Retrieves address information for a given postal code and country.    This request can be used to implement auto complete functionality when a customer needs to fill in an address.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param country_code: Three letter country code refering to the &#x60;postalCode&#x60; field.
    :type country_code: str
    :param postal_code: Postal code.
    :type postal_code: str

    """
    return web.Response(status=200)


async def list_pickup_ppoints_by_location(request: web.Request, content_type, accept, geo_coordinates=None, postal_code=None, country_code=None) -> web.Response:
    """List pickup points by location

    Retrieves information on pickup points close to a given location determined by geocoordinates or postal code.    The pickup points returned are not necessarily all active ones. Make sure to validate the information consumed by integrations.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param geo_coordinates: Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes.
    :type geo_coordinates: List[]
    :param postal_code: Postal code around which to search for pickup points. If you use this type of search, make sure to pass a &#x60;countryCode&#x60; and do not pass &#x60;geoCoordinates&#x60;.
    :type postal_code: str
    :param country_code: Three letter country code refering to the &#x60;postalCode&#x60; field. Pass the country code only if you are searching pickup points by postal code.
    :type country_code: str

    """
    return web.Response(status=200)
