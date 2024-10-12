from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_sellers_by_region200_response import GetSellersByRegion200Response
from openapi_server import util


async def get_sellers_by_region(request: web.Request, content_type, accept, region_id, country, postal_code=None, geo_coordinates=None) -> web.Response:
    """Get sellers by region or address

    Retrieve a list of sellers that cater to a specific region or address, according to your set up of our [regionalization feature](https://help.vtex.com/en/tutorial/setting-up-price-and-availability-of-skus-by-region--12ne58BmvYsYuGsimmugoc#). Learn more about [Region v2](https://developers.vtex.com/vtex-developer-docs/changelog/region-v2).    To access the list of sellers, you must choose one of the following methods:    1. Send the identification of the list of sellers (&#x60;regionId&#x60;) as a path parameter through the URL. Or;  2. Send the &#x60;country&#x60; (3-digit ISO code) and at least one of the two values (&#x60;postal Code&#x60; or &#x60;geo Coordinates&#x60;) as query parameters through the URL. For this method, it is also allowed to send both values (&#x60;postalCode&#x60; or &#x60;geoCoordinates&#x60;) in the same request.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param region_id: ID of the region corresponding to the shopper&#39;s location.
    :type region_id: str
    :param country: Three letter country code refering to the &#x60;postalCode&#x60; field.
    :type country: str
    :param postal_code: Postal code corresponding to the shopper&#39;s location.
    :type postal_code: str
    :param geo_coordinates: Geocoordinates (first longitude, semicolon, then latitude) corresponding to the shopper&#39;s location.
    :type geo_coordinates: List[]

    """
    return web.Response(status=200)
